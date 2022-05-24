from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('books/', views.BookView),
    path('journals/', views.JournalView)
]