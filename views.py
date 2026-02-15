from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Testimonial, Lead


def home(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'home.html', {
        'services': services,
        'testimonials': testimonials
    })


def about(request):
    return render(request, "about.html")


def services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        Lead.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        return redirect("home")

    return render(request, "contact.html")


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, "service_detail.html", {"service": service})