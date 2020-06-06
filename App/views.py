from django.shortcuts import render
# requirements for sign up generic view
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# to use the forms file import it
from .forms import *


# Create your views here.
def index(request):
    title = 'InOurMindsForever'
    context = {
        'title': title,
    }
    return render(request, 'Index.html', context)


def about(request):
    context = {'title': 'About Us'}
    return render(request, 'about.html', context)


def contact(request):
    thanks = ''
    form = ContactFORM(request.POST or None)
    if form.is_valid():
        form.save()
        thanks = 'Thanks for contacting us we would get back to you shortly'
        form = ''
    context = {
        'title': 'Contact Us',
        'form': form,
        'thanks': thanks,
        'contact': ConDetails.objects.order_by()[:1]
    }
    return render(request, 'contact.html', context)


def plan(request):
    context = {'title': 'Plans'}
    return render(request, 'plan.html', context)


# TODO you need to make this how.html page you did not put it in
def how(request):
    context = {'title': 'How InOurMindsForever works'}
    return render(request, 'how.html', context)


# Todo you need to create a detail html page for the memorial for the view more button
def memorial(request):
    context = {'title': 'Memorials', 'card': Memorial.objects.order_by('-date')}
    return render(request, 'mem-search.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'create_username.html'


def create_memorial(request):
    context = {'title': 'Create a memorial for your loved one'}
    return render(request, 'create-memorial.html', context)


# TODO you need to make that search icon in the UL functional so it can accept my input search
def search(request):
    pass


# TODO you need to make a testimonial html page
def testimonials(request):
    pass


# TODO you need to create a 404.html page for this 4 url types just one
def page404(request, anything):
    title = "Big 404"
    return render(request, 'App/404.html', locals())


def page404_1(request, anything, whatever):
    title = "Big 404"
    return render(request, 'App/404.html', locals())


def page404_2(request, anything, whatever, seriously):
    title = "Big 404"
    return render(request, 'App/404.html', locals())


def page404_3(request, anything, whatever, seriously, i_give_up):
    title = "Big 404"
    return render(request, 'App/404.html', locals())

