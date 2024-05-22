from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


app_name = 'Book'

#Books pattern
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Bookpage, name="Bookpage"),
    path('Book/', views.Addbookpage, name="Addbookpage"),
    path('Booklist/', views.Booklistpage, name="Booklistpage"),
    path('deletebook/<int:id>/', views.Deletebook, name="deletebook"),
    path('bookdetail/<int:id>/', views.Bookdetail, name="bookdetail"),
    path('editbookpage/<int:id>/', views.Editbookpage, name="editbookpage"),
    path('editbook/<int:id>/', views.Editbook, name="editbook"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
