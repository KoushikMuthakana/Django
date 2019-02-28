from django.shortcuts import render
from .forms import FormData,UserForm

def index(request):
    
    return render(request,'djangoFormsApp/index.html')

def form_name(request):
    form=forms.FormData()
    
    if request.method=='POST':
        form=FormData(request.POST)
        if form.is_valid():
            print("Validation Successfull..!!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
           

    return render(request,'djangoFormsApp/form_page.html',context={'form':form})


def users_form(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if  form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form Invalid..!!')


    return render(request,'djangoFormsApp/user_form.html',context={'form':form})