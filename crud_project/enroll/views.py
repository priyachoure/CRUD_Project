from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import studentregisration
from .models import student


# Create your views here.
# this function will add new item and show it
def add_show(request):
    if request.method == 'POST':
        fm = studentregisration(request.POST)
        # if fm.is_valid():
        #     fm.save()    --------
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print(nm, em, pw)
            reg = student(name=nm, email=em, password=pw)
            reg.save()
            fm = studentregisration()  # it given bez after adding data should not be save in same field.

    else:
        fm = studentregisration()
    stud = student.objects.all()

    return render(request, 'addandshow.html', {'form': fm, 'all_data': stud})


# This function show delete data
def delete_data(request, id):
    if request.method == "POST":
        pi = student.objects.get(pk=id)
        pi.delete()
        return HttpResponse('/')


def update_data(request, id):
     if request.method=="POST":
        pi = student.objects.get(pk=id)
        print("pi",pi)
        fm=studentregisration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
     else:
        pi = student.objects.get(pk=id)
        fm=studentregisration(instance=pi)
     return render(request, 'update.html', {'form': fm})
