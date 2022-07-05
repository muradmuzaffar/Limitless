from django.shortcuts import render, redirect, get_object_or_404
#from requests import get
from .forms import ContactForm, SubscribtionForm
from .models import Blogs, Category, Jobs, Products, ProductCategory

# Create your views here.


def landing(request):
    if request.method == "POST":
        form = SubscribtionForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
            return redirect("landing")

    form = SubscribtionForm()
    blogs = Blogs.objects.all()[:6]

    return render(request, "landing.html", context={"form": form, "blogs": blogs})


def about(request):
    return render(request, "about.html")


def job_posting(request):
    if "q" in request.GET:
        q = request.GET["q"]
        jobs = Jobs.objects.filter(name__icontains=q)
    else:
        jobs = Jobs.objects.all().order_by("-id")

    return render(request, "job-posting.html", {"jobs": jobs})


def job_single(request, id):
    job = get_object_or_404(Jobs, id=id)
    return render(request, "job-single.html", {"job": job})


def store(request):
    if "q" in request.GET:
        q = request.GET["q"]
        products = Products.objects.filter(name__icontains=q)

    else:
        products = Products.objects.all().order_by("-id")

    categories = ProductCategory.objects.all()

    return render(request, "store.html", {"products": products, "categories": categories})


def store_single(request, id):
    product = get_object_or_404(Products, id=id)
    products = Products.objects.all()
    return render(request, "store-single.html", {"product": product, "products": products[:7]})


def store_by_category(request, category_slug):
    products = Products.objects.filter(
        category__slug=category_slug)

    return render(request, 'store_by_category.html', {'products': products})


def blogs(request):
    if "q" in request.GET:
        q = request.GET["q"]
        blogs = Blogs.objects.filter(name__icontains=q)

    else:
        blogs = Blogs.objects.all().order_by("-id")
    category = Category.objects.all()
    return render(request, "blogs.html", {"blogs": blogs, "category": category})


def blogs_detail(request, id):
    blog = get_object_or_404(Blogs, id=id)
    return render(request, "single-blog.html", {"blog": blog})


def privacy_policy(request):
    return render(request, "privacy-policy.html")


def terms_conditions(request):
    return render(request, 'terms-conditions.html')


def contact(request):
    return render(request, 'contact.html')
