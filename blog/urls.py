from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='mainpage'),

    path('news', NewsList.as_view(), name='news'),

    path('blog/', PostList.as_view(), name='post_list'),
    path('blog/category/<int:category_id>/', PostByCategories.as_view(), name='posts_by_categories'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostNew.as_view(), name='post_new'),

    path('about', About.as_view(), name='about'),

    path('search_post/', SearchPost.as_view(), name='search_post'),
    path('search_news/', SearchNews.as_view(), name='search_news'),

    # path('articles/', views.ArticleView.as_view()),
    # path('articles/<int:pk>',views.ArticleUpdateView.as_view())
]
