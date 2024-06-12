from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator

class SchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        if 'definitions' in schema:
            del schema.definitions
        return schema

schema_view = get_schema_view(
    openapi.Info(
        title="Python Challenge - API Playground",
        default_version='beta',
        description="API documentation for the challenge project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
    generator_class=SchemaGenerator
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('auth/', include('user.urls', namespace='user')),
    path('transaction/', include('transaction.urls', namespace='transaction')),
    path('hello-world/', include('hello_world.urls', namespace='hello_world'))
]
