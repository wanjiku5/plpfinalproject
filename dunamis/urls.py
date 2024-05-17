



from django.urls import path
from .views import home, AboutView, jobs

urlpatterns = [
    path('', home, name='home'),
    path('about', AboutView, name='about'),
    path('jobs', jobs, name='jobs'),

]