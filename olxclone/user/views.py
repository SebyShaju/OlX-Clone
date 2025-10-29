from django.shortcuts import render,redirect
from .forms import Reguser,ProfileForm,Postform,Interestedform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from olx.views import homepage
from .models import Profile,Posts,Interested


# Create your views here.


def adduser(request):
    if request.method=='POST':
        form=Reguser(request.POST)
        if form.is_valid():
            a = form.save()
            Profile.objects.create(user=a)

            messages.success(request,'User has been registered')
            return redirect(homepage)
    else:
        form = Reguser()
    return render(request,'register.html',{'form':form})


def loginpage(request):
    if request.method=='POST':
        usern = request.POST['user']
        passw = request.POST['pass']
        
        user=authenticate(request,username=usern,password=passw)
        if user:
            login(request,user)
            print('login successfully')
            messages.success(request,'User has been signed in')
            return redirect(homepage)
        else:
            print('No Such User')    

    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    messages.success(request,'User has been signed out')
    return redirect(homepage)


def profilepage(request):

    usr = request.user
    pro = Profile.objects.get(user=usr)
    ads = Posts.objects.filter(user=usr)
    return render(request,'profile.html',{'pro':pro,'ads':ads})

def editprofile(request,eid):
    pro = Profile.objects.get(id=eid)
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES, instance=pro)
        if form.is_valid():
            form.save()
            return redirect(profilepage)
    else:

        form = ProfileForm(instance=pro)
    return render(request,'editprofile.html',{'form':form})



def addpost(request):
    if request.method=='POST':
        form = Postform(request.POST,request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect(homepage)

    else:
        form = Postform()
    return render(request,'addposts.html',{'form':form})






def mypost(request):

    usr = request.user
    ads = Posts.objects.filter(user=usr)
    return render(request,'myposts.html',{'ads':ads})

def post_page(request,name):
    ads = Posts.objects.filter(category=name)
    return render (request,'home.html',{'ads':ads})

def allpost(request):
    ads = Posts.objects.all()
    return render (request,'home.html',{'ads':ads})

def manage_post(request):

    usr = request.user
    ads_list = Posts.objects.filter(user=usr)
    return render(request,'manageposts.html',{'ads_list':ads_list})


def editpost(request,postid):
    ads = Posts.objects.get(id=postid)

    if request.method=='POST':
        form= Postform(request.POST,request.FILES,instance=ads)
        if form.is_valid():
            form.save()
            return redirect(manage_post)
    form = Postform(instance=ads)
    return render(request,'editpost.html',{'form':form})


def postdetails(request,postid):
    ads_details = Posts.objects.get(id=postid)
    return render (request,'postdetails.html',{'ads_details':ads_details})


def deletepost(request,postid):
    ads = Posts.objects.get(id=postid)
    if request.method=='POST':
        ads.delete()
        return redirect(manage_post)
    return render(request,'postdelete.html',{'ads':ads})




def addinterest(request, postid):
    ad = Posts.objects.get(id=postid)  
    receiver = ad.user 

    if request.method == 'POST':
        form = Interestedform(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.sender = request.user 
            a.receiver = receiver 
            a.ad = ad  
            a.save()
            return redirect(homepage)

    else:
        form = Interestedform()

    return render(request, 'addinterest.html', {'form': form})





def notifications(request):
    usr = request.user  
    messages_received = Interested.objects.filter(receiver=usr) 

    return render(request, 'messages.html', {'mssgs': messages_received})

