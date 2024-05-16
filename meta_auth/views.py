"""Meta_auth related views"""
from django.contrib.auth import login
from django.shortcuts import redirect, render
from rest_framework import viewsets

from .form import SignupForm


class UserViewSet(viewsets.ViewSet):

    def register(self, *args, **kwargs):
        form = SignupForm(self.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.email
            user.is_staff = True
            user.allow_metadatax_edition()
            user.save()
            login(self, user)
            return redirect('/admin/')
        return render(self, 'home.html', {
            'register_form': form,
            'isConnected': self.user.is_staff
        })
