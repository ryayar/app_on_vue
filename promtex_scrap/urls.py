"""promtex_scrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# так стало
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('scrap.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Так было
# from django.contrib import admin
# from django.urls import path, re_path, include
# from django.views.generic import TemplateView
# from scrap import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", views.index),
#     path("create/", views.create),
#     path("edit/<int:id>/", views.edit),
#     path("delete/", views.delete),
#     path("dele/<int:id>/", views.dele),
#     path("contact/", TemplateView.as_view(template_name="contact.html")),
#     path("result/", TemplateView.as_view(template_name="results.html")),
#     path("result/<int:id>/", views.edit),
#     path("generate_cp/", views.generate_cp),
# ]


# product_patterns = [
#     path("", views.products),
#     path("new", views.new),
#     path("top", views.top),
# ]
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index),
#     path("products/<int:id>/", include(product_patterns)),
#     path("products/", include(product_patterns)),
#     path("about/", TemplateView.as_view(template_name="about.html")),
#     path("contact/", TemplateView.as_view(template_name="contact.html")),
# ]
