from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Aaicho Paicho Backend API",
      default_version='v1',
      description="A REST API for authentication and managing transactions. Transactions include both income and expense types.",
      contact=openapi.Contact(email="prabinbohara10@gmail.com"),
      
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   
   ...
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('transactions/', include('transactions.urls')),


    ## swagger url patterns:
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
