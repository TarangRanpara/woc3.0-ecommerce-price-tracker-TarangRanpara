from django.urls import path
from .views import main_page_view

urlpatterns = [

    # this is single most view that handles GET and POST requests
    path('', main_page_view)
]