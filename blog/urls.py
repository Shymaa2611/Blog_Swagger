from django.urls import path

from . import views

urlpatterns = [
   path('blog/', views.postView.as_view()),
   path('blog/<int:pk>/', views.postView_pk.as_view()),
]
