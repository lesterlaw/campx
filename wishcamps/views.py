from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views import generic
from .models import WishCamp, PersonalInfo
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from .forms import WishForm, WishJoinForm
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# def home(request):
#     return render(request, 'wishcamps/base.html', {})
# Create a new class that redirects the user to the index page, if successful at logging

def faq(request):
    return render(request, 'wishcamps/faq.html', {})

class WishList(generic.ListView):
    template_name = 'wishcamps/wishlist.html'
    context_object_name = 'wishcamps'
    paginate_by = 12
    def get_queryset(self):
        return WishCamp.objects.order_by('-published_date')

class WishDetail(generic.DetailView):
    model = WishCamp
    template_name = 'wishcamps/wishdetail.html'

# @csrf_protect
# def WishJoin(request, wishcamp_id):
#     c = get_object_or_404(WishCamp, pk=wishcamp_id)
#     if request.method == 'POST':
#         return HttpResponseRedirect(reverse('wishcamps:wishjoindetails'))
#         # c.number_of_people += 1
#         # c.save()
#     else:
#         return render(request, 'wishcamps/fail.html', {})
#     return HttpResponseRedirect(reverse('wishcamps:wishdetail', args=(c.id,)))

def WishJoinDetails(request, wishcamp_id):
    if request.method == 'POST':
        form = WishJoinForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.camp_id = wishcamp_id
            try:
                post.save()
            except IntegrityError or ValidationError:
                return render(request, 'wishcamps/alreadyregistered.html', {})
            else:
                form = WishJoinForm()
            c = get_object_or_404(WishCamp, pk=wishcamp_id)
            c.number_of_people += 1
            c.save()
            return redirect('wishcamps:wishdetail', pk=wishcamp_id)
    else:
        form = WishJoinForm()
    return render(request, 'wishcamps/wishjoindetails.html', {'form':form})

def WishNew(request):
    if request.method == "POST":
        form = WishForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('wishcamps:wishdetail', pk=post.pk)
    else:
        form = WishForm()
    return render(request, 'wishcamps/wishedit.html', {'form': form})

def WishEdit(request, wishcamp_id):
    post = get_object_or_404(WishCamp, pk=wishcamp_id)
    if request.method == "POST":
        form = WishForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('wishcamps:wishdetail', pk=wishcamp_id)
    else:
        form = WishForm(instance=post)
    return render(request, 'wishcamps/wishedit.html', {'form': form})

def WishDelete(request, wishcamp_id):
    post = get_object_or_404(WishCamp, pk=wishcamp_id).delete()
    return redirect('wishcamps:wishlist')

class userlist(generic.DetailView):
    model = WishCamp
    template_name = 'wishcamps/userlist.html'
