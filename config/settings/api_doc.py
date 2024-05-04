from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="fake JIRA API",
        default_version="v1",
        description="faking jira response",
        contact=openapi.Contact(email="erfan.ehsany@outlook.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
