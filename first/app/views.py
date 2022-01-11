from django.shortcuts import render,redirect
from app.models import new,new1
# Create your views here.
def index(request):
    return render(request,'index.html')
def student(request):
    return render(request,'student.html')
def admins(request):
    return render(request,'admins.html')
def adminpage(request):
     
     vars=new.objects.all()
     return render(request, 'adminpage.html',{'vars':vars})
     
def studentview(request):
    return render(request,'studentview.html')
def settings(request):
    return render(request,'settings.html')

def save(request):
        name=request.POST.get("name")
        password=request.POST.get("password")
        chemistry=request.POST.get("chemistry")
        physics=request.POST.get("physics")
        maths=request.POST.get("maths")
        english=request.POST.get("english")
        email=request.POST.get("email")

        vars=new(name=name,password=password,email=email,chemistry=chemistry,physics=physics,maths=maths,english=english)
        vars.save()
        vars=new.objects.all()
        return render(request, 'adminpage.html',{'vars':vars})

def login(request):
    if request.method=='POST':
        if new.objects.filter(email=request.POST['email1'], password=request.POST['password1']).exists():
            members= new.objects.get(email=request.POST['email1'], password=request.POST['password1'])
            vars=new.objects.all()
            return render(request, 'studentview.html',{'member':members,'vars':vars})
        else:
            return render(request,'student.html')

    else:
         return render(request,'student.html')
def alog(request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        vars=new1(username=username,password=password)
        vars.save()
        vars=new1.objects.all()
        return render(request, 'settings.html',{'vars':vars})
def loginadmin(request):
    if request.method=='POST':
        if new1.objects.filter(username=request.POST['uname'], password1=request.POST['psw']).exists():
            
            vars=new.objects.all()
            return render(request, 'adminpage.html',{'vars':vars})
        else:
            return render(request,'admins.html')

    else:
         return render(request,'admins.html')

def message(request):
        cname=request.POST.get("cname")
        cemail=request.POST.get("cemail")
        cnumber=request.POST.get("cnumber")
        csub=request.POST.get("csub")
        cmessage=request.POST.get("cmessage")


        vars=new1(cname=cname,cemail=cemail,cnumber=cnumber,csub=csub,cmessage=cmessage)
        vars.save()
        vars=new1.objects.all()
        return render(request, 'adminpage.html',{'vars':vars})
def delete(request,id):
    vars1=new.objects.get(id=id)
    vars1.delete()
    return redirect('/adminpage')