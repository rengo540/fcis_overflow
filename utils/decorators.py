from django.shortcuts import render,redirect
from django.contrib import messages



def if_authenticated(view_func):
    def wrapper_func (request,*args,**kwargs):
        if request.user.is_authenticated :
            messages.info(request,'please logout to log with anothar account')
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func



def must_be_login (view_func):
    def wrapper_fun(request,*args,**kwargs):
        if request.user.is_authenticated:
            return view_func(request,*args,**kwargs)
        else:
            messages.info(request,'must be login before')
            return redirect('login')
    return wrapper_fun