from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import Http404
from .models import Note
import uuid
import hashlib
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




def generate_random_hashed_id():
    random_uuid = uuid.uuid4()
    hashed_id = hashlib.sha256(str(random_uuid).encode()).hexdigest()
    return hashed_id

class index(LoginRequiredMixin,ListView):
    login_url='login'
    model = Note
    template_name = 'to_do_list/note_list.html'

    def get_queryset(self):
            return Note.objects.filter(user=self.request.user.id)
        

class CreateNewNote(LoginRequiredMixin,CreateView):
    login_url='login'
    model = Note
    template_name = 'to_do_list/note_create.html'
    success_url = '/to-do/notes'
    fields = ['title', 'content', 'user']

    def form_valid(self, form):
        form.instance.hashed_id = generate_random_hashed_id()
        return super().form_valid(form)

class update_note(LoginRequiredMixin,UpdateView):
    login_url='login'
    model = Note
    fields = ["title", "content"]
    template_name = 'to_do_list/note_update.html'

    def form_valid(self, form):
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        hashed_id = self.kwargs.get('hashed_id')
        return get_object_or_404(Note, hashed_id=hashed_id)

    def get_success_url(self):
        return '/to-do/notes'

class ModelDeleteView(LoginRequiredMixin,DeleteView):
    login_url='login'
    model = Note
    success_url = "/to-do/notes"

    def get_object(self, queryset=None):
        hashed_id = self.kwargs.get('hashed_id')
        return get_object_or_404(Note, hashed_id=hashed_id)

class ModelDetailView(LoginRequiredMixin,DetailView):
    login_url='login'
    model = Note
    
    def get_object(self, queryset=None):
        hashed_id = self.kwargs.get('hashed_id')
        note = get_object_or_404(Note, hashed_id=hashed_id)
        user_id = self.request.user.id
        
        if user_id == note.user_id:
            return note
        else:
            return redirect('login')
