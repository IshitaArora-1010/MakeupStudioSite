from django.shortcuts import render, redirect, get_object_or_404
from .models import gallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import Appointment_form
from django.views.generic import DetailView
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index1.html')

def gallery_display(request):
    images = gallery.objects.all()

    paginator = Paginator(images, 12)
    page = request.GET.get('page')
    try:
        gallery_imgs = paginator.page(page)
    except PageNotAnInteger:
        gallery_imgs = paginator.page(1)
    except EmptyPage:
        gallery_imgs = paginator.page(paginator.num_pages)
    return render(request, 'pages/gallery.html', {'pagi': gallery_imgs})

def services(request):
    return render(request, 'pages/services.html')

def courses(request):
    return render(request, 'pages/courses.html')

def enquiry_feed(request):
    msg = ""
    if request.method == "POST":
        form = Appointment_form(request.POST)
        if form.is_valid():
            form.save()
            # subject = "Website Inquiry"
            # body = {
            #     'Name': form.cleaned_data['Name'],
            #     'Instagram_handle': form.cleaned_data['Instagram_handle'],
            #     'Makeup': form.cleaned_data['Makeup'],
            #     'Feedback': form.cleaned_data['Feedback'],
            # }
            # message = "\n".join(body.values())
            # try:
            #     send_mail(subject, message, 'ambikagarg1101@gmail.com', ['ambikagarg1101@gmail.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            msg = 'Thanks for your feedback!'
            # return redirect('/enquireorfeed')
    else:
        form = Appointment_form()
    return render(request, 'pages/enquiry_feed.html', {'form': form, 'msg': msg})

def galleryDetail(request, image_id):
    theta_image = get_object_or_404(gallery, pk = image_id)
    return render(
        request,
        "pages/details.html",
        {'theta_image': theta_image}
    )