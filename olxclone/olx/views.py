from django.shortcuts import render,redirect
from .forms import CategoryForm
from .models import Category
from user.models import Posts

# Create your views here.

def homepage(request):
    categories = Category.objects.all()
    
    
    query = request.GET.get('q', '')

    
    if query:
        ads = Posts.objects.filter(title__icontains=query)
    else:
        ads = Posts.objects.all()

    return render(request, 'home.html', {'ads': ads, 'categories': categories, 'query': query})

    


def addcategory(request):
    if request.method=='POST':
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(manage_category)

    else:        
        form = CategoryForm()
    return render(request,'addcategory.html',{'form':form})





def categories_page(request):
    categories = Category.objects.all()
    return render(request,'home.html',{'categories':categories})





def manage_category(request):
    category_list = Category.objects.all()
    return render(request,'managecategory.html',{'category_list':category_list})






def editcategory(request,categoryname):
    category = Category.objects.get(name=categoryname)

    if request.method=='POST':
        form= CategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            form.save()
            return redirect(manage_category)
    form = CategoryForm(instance=category)
    return render(request,'editcategory.html',{'form':form})









def deletecategory(request,categoryname):
    category = Category.objects.get(name=categoryname)
    if request.method=='POST':
        category.delete()
        return redirect(manage_category)
    return render(request,'categorydelete.html',{'category':category})














