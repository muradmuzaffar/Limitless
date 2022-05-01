from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.


def landing(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect("landing")

    form = ContactForm()

    return render(request, "landing.html", context={"form": form})

def about(request):
    return render(request,"about.html")
