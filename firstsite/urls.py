from django.contrib import admin
from django.urls import path
import hello.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello.views.home, name='home'),
    path('newblog/',hello.views.blogpost, name="newblog"),
    path('create/',hello.views.create, name='create'),
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





