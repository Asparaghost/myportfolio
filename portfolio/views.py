from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.signing import BadSignature
from django.core import signing
from .models import *

# Create your views here.
def index(request): 
    informations = Information.objects.all() 
    context = {
        'informations':informations
    }
    return render(request, "portfolio/index.html", context)


def works(request):
    category = request.GET.get('category')  
    if category and category != 'All':
        works = Project.objects.filter(category=category)
    else:
        works = Project.objects.all()
    context = {
        'works': works,
        'active_category': category or 'All'
    }
    return render(request, "portfolio/works.html", context)


def proj_info(request, proj_hash):
    try:
        proj_id = signing.loads(proj_hash)
        project = Project.objects.get(proj_id=proj_id)
    except (BadSignature, Project.DoesNotExist):
        return HttpResponse("Invalid project link", status=404)

    context = {
        'project': project,
    }
    return render(request, "portfolio/details.html", context)