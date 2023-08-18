
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
   
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
   
]
# Media setting #s
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


