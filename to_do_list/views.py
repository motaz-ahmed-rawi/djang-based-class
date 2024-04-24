from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import Http404
from .models import User, Note
import uuid
import hashlib
from django.utils import timezone

def user_data(request):
    return request.session.get('user_id')

def generate_random_hashed_id():
    random_uuid = uuid.uuid4()
    hashed_id = hashlib.sha256(str(random_uuid).encode()).hexdigest()
    return hashed_id

class index(ListView):
    model = Note
    template_name = 'to_do_list/note_list.html'

    def get_queryset(self):
        user_id = user_data(self.request)
        if user_id:
            return Note.objects.filter(user=user_id)
        else:
            return redirect('login')

class CreateNewNote(CreateView):
    model = Note
    template_name = 'to_do_list/note_create.html'
    success_url = '/to-do/notes'
    fields = ['title', 'content', 'user']

    def form_valid(self, form):
        form.instance.hashed_id = generate_random_hashed_id()
        return super().form_valid(form)

class update_note(UpdateView):
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

class ModelDeleteView(DeleteView):
    model = Note
    success_url = "/to-do/notes"

    def get_object(self, queryset=None):
        hashed_id = self.kwargs.get('hashed_id')
        return get_object_or_404(Note, hashed_id=hashed_id)

class ModelDetailView(DetailView):
    model = Note
    
    def get_object(self, queryset=None):
        hashed_id = self.kwargs.get('hashed_id')
        note = get_object_or_404(Note, hashed_id=hashed_id)
        user_id_from_session = self.request.session.get('user_id')
        
        if user_id_from_session == note.user_id:
            return note
        else:
            return redirect('login')

class signup(CreateView):
    model = User
    template_name = 'to_do_list/signup.html'
    fields = ['name', 'last_name', 'email', 'password']
    success_url = 'login'

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email, password=password).first()
        
        if user:
            request.session['user_id'] = user.id
            return redirect('/to-do/notes')
        else:
            return render(request, 'to_do_list/login.html', {'error': "Invalid email or password!"})
    return render(request, 'to_do_list/login.html')

def logout(request):
    request.session.clear()
    return redirect('login')
