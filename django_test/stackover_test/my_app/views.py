from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import modelformset_factory
from . import forms
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.urls import reverse
import pandas as pd
# from cones.models import Wa

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello Ayesha, I love ayesh. She is my beloved daughter.</h><p><h1> Ayesha</h1></p>')

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = forms.UpdateProfile(request.POST, request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = forms.UpdateProfile()
    context ={
        "p_form":p_form
    }
    return render(request, 'profile_dict/profile.html', context)


