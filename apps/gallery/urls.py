from django.urls import path
from apps.gallery.views import (
    index, image, search,
    new_image, edit_image, delete_image
)


urlpatterns = [
    path('', index, name='index'),
    path('image/<int:photo_id>', image, name="image"),
    path('search', search, name='search'),
    path('new_image', new_image, name='new_image'),
    path('edit_image/<int:photo_id>', edit_image, name='edit_image'),
    path('delete_image/<int:photo_id>', delete_image, name='delete_image')
]