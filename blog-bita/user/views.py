from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from user.models import User,Post






def index(request):
    data=Post.objects.all()
    print(data)
    value={
        "op":data
    }
    
    return render(request,'index.html',value)

    
@login_required(login_url='/login')
def allpost(request):
    data=Post.objects.filter(user=request.user)
    value={
        "posts":data

    }
    return render(request,'user/allpost.html',value)


@login_required(login_url='/login')
def post(request):



    if request.method=='POST':

        title=request.POST.get('title')
        image=request.FILES.get('image')
        content=request.POST.get('content')
        highlight=request.POST.get('highlight')

        if title=="" or image=="" or content=="" or highlight=="":


            messages.warning(request,"don't live black field item registration")
            return redirect('post')
        else:
            # shop=Post.objects.get(user=request.user)
            # id=getattr(shop,'id')
            creat=Post(title=title,content=content,postpic=image,  user=request.user,highlight=highlight)   
            creat.save()
            return redirect('allpost')

    return render(request,'user/post.html')




@login_required(login_url='/login')
def profile(request):
    

   
    
    return render(request,'user/profile.html')

def profileview(request,id):
    user=User.objects.get(id=id)
    post=Post.objects.filter(user=user)
    print(user)
    print("user")
    print(post)

    data={
        "user":user,
        "post":post,
    }
    return render(request,'profileview.html',data)

@login_required(login_url='/login')
def logouthere(request):
    # if request.method=='POST':
        
        logout(request)
        # messages.info(request,'logout successfully')
        return redirect('/login')






def register(request):
     if request.method=='POST':

        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        
        if username=="" or email=="" or password=="" or password2=="":
            messages.warning(request,"don't live black field")
            return redirect('/register')

        elif password != password2:
            messages.warning(request,'password not match')
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.warning(request,'username taken')
            return redirect('/register')
        elif User.objects.filter(email=email    ).exists():
            messages.warning(request,'email used')
            return redirect('/register')
        else:

            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            messages.success(request,'Registered! You can login now') 
            return redirect('login')

     return render(request,'user/register.html')

def login(request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        if username=="" or password=="":
            messages.warning(request,"don't live black field")
            return redirect('login')
        else:
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('profile')
            else:
                messages.info(request,'invailide user details')
        return redirect('login')
    return render(request,'user/login.html')
    # return render(request,'user/login.html')





# Create your views here.

# @login_required(login_url='/login')
def readmore(request,id):
    data=Post.objects.get(id=id)
    value={
        "post":data

    }
    return render(request,'user/readmore.html',value)


def profileedit(request):
     if request.method=='POST':

        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        image=request.FILES.get('image')
        
        about=request.POST.get('bio')

      
        
        # if fname=="" or email=="" or lname=="" or image=="None" or about=="":
        #     messages.warning(request,"don't live black field")
        #     return redirect('/profileedit')
        # if User.objects.filter(email=email).exclude(email__in=request.user.email).exists():
        #     messages.warning(request,'taken by another person!')
        #     return redirect('/profileedit')
        # else:

        us=User.objects.get(id=request.user.id)
        print(us.first_name)
        us.first_name=fname
        us.last_name=lname
        us.email=email
        us.bio=about
        us.udp=image
        us.save()
        messages.success(request,'Updated!') 
        return redirect('/profileedit')

     return render(request,'user/profileedit.html')


@login_required(login_url='/login')
def postedit(request,id):

    if request.method=='POST':
        print(id)

        title=request.POST.get('title')
        image=request.FILES.get('image')
        content=request.POST.get('content')
        highlight=request.POST.get('highlight')

            # shop=Post.objects.get(user=request.user)
            # id=getattr(shop,'id')
        # creat=Post(title=title,content=content,postpic=image,highlight=highlight)
        creat=Post.objects.get(id=id)
        creat.title=title
        creat.content=content
        creat.postpic=image
        creat.highlight=highlight
        
        creat.save()
        return redirect(request.path_info)
    data=Post.objects.get(id=id)
    value={
        "post":data
    }

    return render(request,'user/postedit.html',value)


@login_required(login_url='/login')
def postdelete(request,id):
    user=request.user
    idd=Post.objects.get(user=user,id=id)
    # idd=id
    # cart=Cart.objects.filter(user=user,shopiteam=idd)
    idd.delete()
    return redirect('/allpost')