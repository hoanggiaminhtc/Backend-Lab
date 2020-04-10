"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from page.views import home_view,page_error
from django.conf.urls import handler404, handler500, url
from django.conf.urls.static import static
from django.conf import settings
from news import views as news_views
from rest_framework import routers
from api.views import NewsListCreateAPIView, NewsDetailUpdateAPIView,CommentDetailUpdateAPIView,CommentListCreateAPIView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.SimpleRouter()
router.register(r'news', NewsListCreateAPIView, basename="News")     # đăng ký API vào router
router.register(r'news', NewsDetailUpdateAPIView, basename="News")
router.register(r'comment', CommentListCreateAPIView, basename="Comment")     
router.register(r'comment', CommentDetailUpdateAPIView, basename="Comment")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',news_views.NewsListView.as_view(), name='home'),
    path('news/', include('news.urls')),
    path('accounts/', include('accounts.urls')),
    url('^api/', include(router.urls))
]
handler404 ='page.views.page_error'
handler500 ='page.views.page_error'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns+= staticfiles_urlpatterns()
