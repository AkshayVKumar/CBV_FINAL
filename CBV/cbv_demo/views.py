from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,
                                    DetailView,CreateView,UpdateView,
                                    DeleteView)
from . import forms
from cbv_demo.models import School
from django.urls import reverse_lazy,reverse
# Create your views here.

def index(request):
    return HttpResponse("Function Based Views")

class IndexView(View):
    def get(self,request):
        return HttpResponse("Class Based Views")

def temp1(request):
    return render(request,'temp1.html',context={'data':"hello world"})

class TemplateDemoView(TemplateView):
    template_name='temp1.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['data']="Data for CBV"
        return context

class Form_Demo(View):
    def get(self,request):
        return render(request,'temp2.html',context={'form':forms.Form_name()})
    
    def post(self,request):
        form=forms.Form_name(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return HttpResponse("Form Submission Successful")
        #return render(request,'temp2.html',context={'form':form})
class TempView(TemplateView):
    template_name='cbv_demo/base.html'

class SchoolListView(ListView):
    model=School
    context_object_name="schools"

class SchoolDetailView(DetailView):
    model=School
    template_name='cbv_demo/school_detail.html'
    context_object_name='school_detail'

class SchoolCreateView(CreateView):
    model=School
    fields=('name','principal','location')

class SchoolUpdateView(UpdateView):
    model=School
    fields=('name','principal','location')

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("cbv_demo:list")