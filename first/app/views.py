from django.shortcuts import render,redirect
from app.models import new,new1,new2
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
            members= new.objects.all()
            
            return render(request, 'studentview.html',{'member':members})
        else:
            return render(request,'student.html')

    else:
         return render(request,'student.html')
        
def alog(request):
        username=request.POST.get("username")
        password1=request.POST.get("password1")
        vars=new1(username=username,password1=password1)
        vars.save()
        
        return render(request, 'settings.html')
def loginadmin(request):
    if request.method=='POST':
        if new1.objects.filter(username=request.POST['uname'], password1=request.POST['psw']).exists():
            
            vars=new.objects.all()
            var=new2.objects.all()
            return render(request, 'adminpage.html',{'vars':vars,'var':var})
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


        vars=new2(cname=cname,cemail=cemail,cnumber=cnumber,csub=csub,cmessage=cmessage)
        vars.save()
        
        return render(request, 'index.html')
def delete(request,id):
    vars1=new.objects.get(id=id)
    vars1.delete()
    return redirect('/adminpage')
def edit(request,id):
    vars=new.objects.get(id=id)
    return render(request,'settings.html',{'var':vars})
    
def update(request,id):
    vars=new.objects.get(id=id)
    vars.name=request.POST.get('name')
    vars.password=request.POST.get('password')
    vars.chemistry=request.POST.get('chemistry')
    vars.physics=request.POST.get('physics')
    vars.maths=request.POST.get('maths')
    vars.english=request.POST.get('english')
    vars.email=request.POST.get('email')
    vars.save()
    
    return redirect('/adminpage')

def loginn(request,id):
    vars=new.objects.filter(id=id)
    return render(request, 'studentview.html',{'var':vars})
    
    