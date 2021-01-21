from django.shortcuts import render,get_object_or_404
from .models import Category,Product,Subcat

def products_list(request,Category_slug=None,subcat_slug=None):
    category=None
    products=None
    categories = Category.objects.all()
    if Category_slug!=None and subcat_slug == None:
        category=get_object_or_404(Category,slug=Category_slug)
        products=Product.objects.filter(category=category,available=True)
    elif Category_slug!=None and subcat_slug!=None :
        category=get_object_or_404(Category,slug=Category_slug)
        subcat=get_object_or_404(Subcat,slug=subcat_slug)
        products=Product.objects.filter(category=category,subcat=subcat,available=True)

    else:
        products=Product.objects.filter(available=True)
    context={
    'category':category,
    'products':products,
    'categories':categories,
    }
    return render(request,'shop/index.html',context)

def product_detail(request,c_slug,subcat_slug,p_slug):
    categories=Category.objects.all()
    try:
        product=Product.objects.get(category__slug=c_slug,subcat__slug=subcat_slug,slug=p_slug)
        cat=product.category.name

    except Exception as e:
        raise e
    return render(request,'shop/product_detail.html',{'cat':cat,'product':product,'categories':categories})
