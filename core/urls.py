from django.contrib import admin
from django.urls import path, include, re_path
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += re_path('edjango.views.static',(r'^media/(?P<path>.*)','serve',{'document_root':settings.MEDIA_ROOT}), )
