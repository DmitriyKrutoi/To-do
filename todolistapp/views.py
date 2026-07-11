from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Task, Note, Category
from .forms import TaskForm, NoteForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.functions import Lower


class MyTasksView(LoginRequiredMixin, ListView):
    template_name = "todolistapp/my_tasks.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all().order_by('due_time').filter(user=self.request.user)


class AddTaskView(CreateView):
    template_name = "todolistapp/add_task.html"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('main:my_tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddNoteView(CreateView):
    template_name = "todolistapp/add_note.html"
    form_class = NoteForm
    model = Note
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class AddCategoryView(LoginRequiredMixin, CreateView):
    template_name = "todolistapp/add_category.html"
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('main:add_task')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MyNotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "todolistapp/my_notes.html"
    context_object_name = "notes"
    paginate_by = 3 

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created_at')


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'todolistapp/note.html'
    context_object_name = 'note'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Note, slug=slug, user=self.request.user)


class NoteSearchView(ListView):
    template_name = 'todolistapp/note_search.html'
    model = Note
    context_object_name = 'notes'
    paginate_by = 4

    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.user)
        q = self.request.GET.get('q', '').strip()
        if q:
            queryset = queryset.annotate(
                lower_name=Lower('name'), lower_info=Lower('info')
            ).filter(
                Q(lower_name__contains=q.lower()) | Q(lower_info__contains=q.lower())
            )
        return queryset.order_by('-created_at')
    

class UpdateNoteView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'todolistapp/edit_note.html'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    

    def get_success_url(self):
        return reverse_lazy('main:note', kwargs={'slug': self.object.slug})
    

    def form_valid(self, form):
        return super().form_valid(form)
    

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('main:my_tasks')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('main:my_notes')
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


def main_page(request):
    return render(request, "todolistapp/main.html")


@login_required
def delete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()

    return redirect("main:my_tasks")    


@login_required
def complete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        if task.is_completed:
            task.is_completed = False
        else:
            task.is_completed = True
        task.save()
    return redirect('main:my_tasks')


@login_required
def complete_all_reward(request):
    if request.method == 'POST':
        tasks = Task.objects.filter(user=request.user)
        if all(task.is_completed for task in tasks):
            Task.objects.filter(user=request.user).update(is_completed=False)
            request.user.profile.streak += 1
            request.user.profile.save()
            print(request.user.profile.streak)
        else:
            messages.error(request, "У вас еще не выполнены все задачи")

    return redirect("main:gift")


@login_required
def gift(request):
    return render(request, "todolistapp/gift.html")


@login_required
def tg_redirect(request):
    return render(request, "todolistapp/telegram_redirect.html")


