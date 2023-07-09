from django.urls import path,include
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.allpost,name="allpost"),
    path('<int:blog_id>/',views.detail,name = 'detail')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
