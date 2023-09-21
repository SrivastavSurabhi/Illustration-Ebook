"""
URL configuration for ebookcreatorai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('old_theme', views.home, name="home"),
    path('', views.story_preview, name="story_preview"),
    path('show_customized_story/', views.show_customized_story, name="show_customized_story"),
    # path('show_customized_story', views.show_customized_story, name="show_customized_story"),
    # path('show_customized_story/<response_type>', views.show_customized_story, name="show_customized_story"),
    # path('convert_to_mp3/', views.convert_to_mp3, name="convert_to_mp3"),
    path('openai_api/<str:prompt>', views.openai_api, name="openaiapi"),
    path('generate_story', views.generate_story_webhook, name="generate_story"),
    path('create_story/<str:unique_id>', views.generate_story, name="create_story"),
    path('create_poem/<str:unique_id>', views.poem_generation, name="create_poem"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)