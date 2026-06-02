from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json


class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:dashboard')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('core:dashboard')
        messages.error(request, 'Invalid credentials or not an admin.')
        return render(request, self.template_name)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('core:index')


class TokenObtainView(View):
    """Simple JWT token endpoint — wire up djangorestframework-simplejwt later"""
    def post(self, request):
        data = json.loads(request.body)
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user and user.is_staff:
            # Placeholder — replace with simplejwt token generation
            return JsonResponse({'token': 'jwt-token-here'})
        return JsonResponse({'error': 'Invalid credentials'}, status=401)