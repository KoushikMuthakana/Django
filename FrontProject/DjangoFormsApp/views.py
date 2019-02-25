from django.shortcuts import render
from . import forms

def index(request):
    
    return render(request,'djangoFormsApp/index.html')

def form_name(request):
    form=forms.FormData()
    
    if request.method=='POST':
        form=forms.FormData(request.POST)
        if form.is_valid():
            print("Validation Successfull..!!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
           

    return render(request,'djangoFormsApp/form_page.html',context={'form':form})