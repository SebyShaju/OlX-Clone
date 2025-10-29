from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage,name='home'),
    path('addcategoroy',addcategory,name='addcategory'),
    path('categories',categories_page,name='categories'),
    path('managecategory',manage_category,name='managecategory'),
    path('editcategory/<categoryname>',editcategory,name='edit_category'),
    path('deletecategory/<categoryname>',deletecategory,name='delete_category'),

    
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)