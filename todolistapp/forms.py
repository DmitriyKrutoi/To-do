from django import forms
from .models import Task, Note, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'info', 'due_time', 'image']

    
    name = forms.CharField(
        label = 'Название задачи',
        widget = forms.TextInput(attrs={
            'class': 'task-name',
            'placeholder': 'Название задачи'
        })
    )

    info = forms.CharField(
        label = 'Информация о задаче', 
        required = False,
        widget=forms.Textarea(attrs={
            'class': 'task-info',
            'placeholder': 'Информация о задаче (необязательно)'
        })
    )

    due_time = forms.TimeField(
        label = 'Время выполнения',
        required=False,
        widget = forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control'
        })
    )

    image = forms.ImageField(
        label = "Картинка к задаче",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'task-image',
            'accept': 'image/*'
        })
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),  # пока пустой, заполним во View
        required=False,
        label='Категория',
        widget=forms.Select(attrs={
            'class': 'task-category'
        }),
        empty_label="Без категории"  # текст для пустого значения
    )


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'info', 'image']


    name = forms.CharField(
        widget = forms.TextInput(attrs={
            'class': 'note-name',
            'placeholder': 'Название заметки'
        })
    )

    info = forms.CharField( 
        widget=forms.Textarea(attrs={
            'class': 'note-info',
        })
    )

    image = forms.ImageField(
        label = "Картинка к заметке",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'note-image',
            'accept': 'image/*'
        })
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    name = forms.CharField(
        label="Название категории",
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Работа, Учеба, Тренировки...',
                'class': 'category-name'
            }
        )
    )