from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('gallery', views.gallery_display),
    path('services', views.services),
    path('courses', views.courses),
    path('enquireorfeed', views.enquiry_feed),
    path('<int:image_id>', views.galleryDetail,name = 'Details')
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
