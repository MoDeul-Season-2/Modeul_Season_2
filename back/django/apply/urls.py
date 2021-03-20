from django.urls import path
from . import views

app_name = "apply"

urlpatterns = [
    path("", views.AppliesView.as_view()),
    path("<int:id>", views.ApplyView.as_view()),
]