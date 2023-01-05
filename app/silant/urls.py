from django.urls import path

from silant.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
