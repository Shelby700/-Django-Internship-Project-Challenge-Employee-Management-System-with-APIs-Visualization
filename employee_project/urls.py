from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny

# Import views from each app
from employees.views import EmployeeViewSet, chart_view
from departments.views import DepartmentViewSet
from attendance.views import AttendanceViewSet
from performance.views import PerformanceViewSet

# DRF Router setup
router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management System API",
        default_version='v1',
        description="API documentation for Employee Management System",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/', include(router.urls)),

    # Swagger Docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Charts Template View
    path('charts/', chart_view, name='charts'),
]
