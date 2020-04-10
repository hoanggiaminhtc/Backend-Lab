from django.urls import path
from .views import (
    NewsDetailView,
    NewsListView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView,
    # my_fbv
)
#from news.views import post

app_name = 'news'
urlpatterns = [
    path('', NewsListView.as_view(), name="news_list"),
    # path('', my_fbv, name='courses-list'),
    path('create/', NewsCreateView.as_view(), name="news_create"),
    path('<int:id>/', NewsDetailView.as_view(), name="news_detail"),
    path('<int:id>/update/', NewsUpdateView.as_view(), name="news_update"),
    path('<int:id>/delete/', NewsDeleteView.as_view(), name="news_delete"),
    #path('<int:id>/',NewsCommentView.as_view, name='news_comment')
    
]