from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, Skill, Contact
from .forms import ProjectForm, SkillForm, ContactForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from core.models import Project
from core.forms import ProjectForm



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


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    login_url = '/auth/login/'
    success_url = reverse_lazy('core:dashboard') 

    def form_valid(self, form):
        messages.success(self.request, f"Project '{form.instance.title}' updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update project. Please check your inputs.")
        return redirect(self.success_url)


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
    
class SkillUpdateView(LoginRequiredMixin,UpdateView):
    model = Skill
    form_class = SkillForm
    login_url = '/auth/login/'
    success_url = reverse_lazy('core:dashboard')


    def form_valid(self, form):
        messages.success(self.request, f"Skill '{form.instance.skill_name}' updated succesfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "failed to updatew skill, Please check yoiur Input!.")
        return redirect(self.success_url)
    

# class SkillUpdateView(LoginRequiredMixin, View):
#     login_url = '/auth/login/'

#     def post(self, request, pk):
#         skill = get_object_or_404(Skill, pk=pk)
#         form = SkillForm(request.POST, instance=skill)
#         if form.is_valid():
#             form.save()


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