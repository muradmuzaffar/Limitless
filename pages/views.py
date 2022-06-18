from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Blogs, Category, Jobs

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
# muveqqeti


def job_posting(request):
    jobs = Jobs.objects.all()
    query = request.GET.get('q')
    if query:
        jobs = Jobs.objects.filter(name__icontains=query)
        print(jobs)
    return render(request, "job-posting.html", {"jobs": jobs})


def job_single(request, id):
    job = get_object_or_404(Jobs, id=id)
    print(job)
    return render(request, "job-single.html", {"job": job})


def store(request):
    return render(request, "store.html")


def store_single(request):
    return render(request, "store-single.html")
# muveqqeti


def blogs(request):
    blogs = Blogs.objects.all()
    category = Category.objects.all()
    return render(request, "blogs.html", {"blogs": blogs, "category": category})


def blogs_detail(request, id):
    blog = get_object_or_404(Blogs, id=id)
    return render(request, "single-blog.html", {"blog": blog})
