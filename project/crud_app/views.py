from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import Course

@login_required(login_url='login_url')
def add_course(request):
    template_name = 'crud_app/add.html'
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_course(request):
    template_name = 'crud_app/show.html'
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, template_name, context)


def update_course(request,pk):
    template_name = 'crud_app/add.html'
    obj=Course.objects.get(id=pk)
    form = CourseForm(instance=obj)
    if request.method == "POST":
        form = CourseForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def delete_course(request,pk):
    template_name = 'crud_app/confirm.html'
    obj = Course.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
    return render(request, template_name)

