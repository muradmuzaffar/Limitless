from django.shortcuts import render, redirect, get_object_or_404
from requests import get
from .forms import ContactForm
from .models import Blogs, Category, Jobs, Products

# Create your views here.


def landing(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
            return redirect("landing")

    form = ContactForm()

    return render(request, "landing.html", context={"form": form})


def about(request):
    return render(request, "about.html")


def job_posting(request):
    jobs = Jobs.objects.all().order_by("-id")
    query = request.GET.get('q')
    if query:
        jobs = Jobs.objects.filter(name__icontains=query)
        print(jobs)
    return render(request, "job-posting.html", {"jobs": jobs})


def job_single(request, id):
    job = get_object_or_404(Jobs, id=id)
    return render(request, "job-single.html", {"job": job})


def store(request):
    products = Products.objects.all().order_by("-id")
    query = request.GET.get('q')
    if query:
        products = Products.objects.filter(name__icontains=query)
    return render(request, "store.html", {"products": products})


def store_single(request, id):
    product = get_object_or_404(Products, id=id)
    products = Products.objects.all()
    return render(request, "store-single.html", {"product": product, "products": products[:7]})


def blogs(request):
    blogs = Blogs.objects.all().order_by("-id")
    category = Category.objects.all()
    return render(request, "blogs.html", {"blogs": blogs, "category": category})


def blogs_detail(request, id):
    blog = get_object_or_404(Blogs, id=id)
    return render(request, "single-blog.html", {"blog": blog})
