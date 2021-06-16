from django.urls import path
from api_basic import views

urlpatterns = [
    # path('article/', views.article_list),
    path('article/', views.SnippetList.as_view()),
    path('articleclass/<int:pk>/', views.SnippetDetail.as_view()),

    path('article/<int:pk>/', views.article_detail),
    path('g/article/<int:id>/', views.Genericview.as_view()),
    
] 
