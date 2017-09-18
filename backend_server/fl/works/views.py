from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.

from .models import Work, WorkCategory

def all(request):
    works = Work.objects.select_related()
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    categories = WorkCategory.objects.all
    return render(request, 'works/index.html', {'works': works, 'title': 'Works', 'user': user, 'categories': categories})

def category(request, work_category_slug):
    category = get_object_or_404(WorkCategory, category_slug = work_category_slug)
    works = Work.objects.filter(work_category = category).select_related()
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    categories = WorkCategory.objects.all
    return render(request, 'works/index.html', {'works': works, 'title': category.category_name, 'user': user, 'categories': categories})

def detail(request, work_category_slug, work_id):
    category = get_object_or_404(WorkCategory, category_slug = work_category_slug)
    work = Work.objects.select_related().filter(work_category = category).get(id=work_id)
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    return render(request, 'works/detail.html', {'work': work})

def create(request):
    category = get_object_or_404(category_slug = request.POST['category_slug'])
    if request.user.is_authenticated:
        user = request.user
    else:
        return HttpResponseRedirect('/auth')
    newWork = Work(work_title = request.POST['work_title'], work_content = request.POST['work_content'],
                   work_category = category, work_employee = user, date_of_pub = timezone('now'), done = False)
    newWork.save()
    return HttpResponseRedirect('/works')
