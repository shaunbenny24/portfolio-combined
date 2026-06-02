from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, Skill, Contact
from .forms import ProjectForm, SkillForm, ContactForm


# --- Page Views ---

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['projects'] = Project.objects.all()
        context['contact_form'] = ContactForm()
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'
    login_url = '/auth/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['skills'] = Skill.objects.all()
        context['contacts'] = Contact.objects.all().order_by('-created_at')
        context['project_form'] = ProjectForm()
        context['skill_form'] = SkillForm()
        # For edit forms, pass a dict of bound forms keyed by pk
        context['project_edit_forms'] = {
            p.pk: ProjectForm(instance=p) for p in context['projects']
        }
        context['skill_edit_forms'] = {
            s.pk: SkillForm(instance=s) for s in context['skills']
        }
        return context


# --- Project CRUD ---

class ProjectCreateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/')


class ProjectUpdateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/')


class ProjectDeleteView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def post(self, request, pk):
        get_object_or_404(Project, pk=pk).delete()
        return redirect('/dashboard/')


# --- Skill CRUD ---

class SkillCreateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def post(self, request):
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/')


class SkillUpdateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def post(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()


class SkillDeleteView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def post(self, request, pk):
        get_object_or_404(Skill, pk=pk).delete()
        return redirect('/dashboard/')


# --- Contact ---

class ContactCreateView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/#contact')


class ContactDeleteView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def post(self, request, pk):
        get_object_or_404(Contact, pk=pk).delete()
        return redirect('/dashboard/')