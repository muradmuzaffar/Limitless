from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Blogs, Category

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


def blogs(request):
    blogs = Blogs.objects.all()
    category = Category.objects.all()
    return render(request, "blogs.html", {"blogs": blogs, "category": category})
