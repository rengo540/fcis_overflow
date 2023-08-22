from django.shortcuts import render , redirect
from django.views import View
from .forms import  UserForm

# Create your views here.
class SignUpView(View):
    def get(self,request):
        user_form = UserForm()
        context = {'user_form':user_form}
        return render(request,'accounts/signup.html',context)

    def post(self,request):
        user_form = UserForm(request.POST)
        if user_form.is_valid() :
            user= user_form.save()
            
            return redirect('login')
        
        context = {'user_form':user_form}
        return render(request,'accounts/signup.html',context)




class LoginView(View):
    def get(self,request):
        pass
     
    def post(self,request):
        pass



