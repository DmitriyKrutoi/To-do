from django.contrib import admin
from django.urls import path, include
from todolistapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    # URL-ы, связанные с задачами
    path('my_tasks/', views.MyTasksView.as_view(), name="my_tasks"),
    path('add_task/', views.AddTaskView.as_view(), name="add_task"),
    path('gift/', views.gift, name="gift"),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete_task/<int:pk>', views.DeleteTaskView.as_view(), name='delete_task'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('complete_all_reward/', views.complete_all_reward, name='complete_all_reward'),  

    # URL-ы, связанные с заметками
    path('add_note/', views.AddNoteView.as_view(), name='add_note'),
    path('my_notes/', views.MyNotesView.as_view() , name="my_notes"),
    path('note/<slug:slug>', views.NoteDetailView.as_view(), name='note'),
    path('edit_note/<slug:slug>', views.UpdateNoteView.as_view(), name='edit_note'),
    path('delete_note/<int:pk>', views.DeleteNoteView.as_view(), name="delete_note"),
    path('note_search/', views.NoteSearchView.as_view(), name='note_search'),
    # Другие
    path('tg_redirect/', views.tg_redirect, name='tg_redirect'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)