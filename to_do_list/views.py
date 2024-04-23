from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from .models import User,Note



class index(ListView):
    model=Note

# class  create_note(LoginRequiredMixin, CreateView):
#     login_url = '/login/'
#     # redirect to the login page if user is not logged in
#     template_name='notes/create_note.html'
#     success_url="/notes"
#     fields=['title','content']
    
#     def form_valid(self,form):
#         note=form.save(commit=False)
#         note.author=self.request.user
#         note.save()
#         return super().form_valid(form)
        

class ModelDetailView(DetailView):
    model = Note
    

class update_note(UpdateView):
    model=Note
    fields=["title","content"]
    template_name='to_do_list/note_update.html'

    def get_success_url(self):
        obj=self.object
        id=obj.id
        return f"/to-do/notes"
    
class signup(CreateView):
    model=User
    template_name='to_do_list\signup.html'
    fields = ['name','last_name','email','password']
    success_url= 'login'

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()  # Get the user object if it exists
        
        if user and user.password == password:
            # Password matches
            return redirect('/to-do/notes')
        else:
            # Either user doesn't exist or password is incorrect
            return render(request, 'to_do_list/login.html', {'error': "Invalid email or password!"})
    return render(request, 'to_do_list/login.html')
