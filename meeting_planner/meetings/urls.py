from django.urls import path
from .views import details, room_list, new

urlpatterns = [
    path ('<int:id>', details, name="details"),
    path ('rooms', room_list, name='rooms'),
    path ('new', new, name='new')
]