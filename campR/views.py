from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import JoinForm
from django.core.exceptions import ValidationError
from django.db import IntegrityError
# Create your views here.
def JoinCamp(request):
    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('thankyou')
    else:
        form = JoinForm()
    return render(request, 'campR/mainpage.html', {'form':form})

def ThankYou(request):
	return render(request, 'campR/thankyou.html', {})