from django.urls import path 
from .views import *

urlpatterns = [
    path("",base,name="base"),

    # Question
    path("Question",QuestionListView.as_view(),name="list_ques"),
    path("detail_ques/<int:pk>",QuestionDetailView.as_view(),name="detail_ques"),
    path("update_ques/<int:pk>",QuestionUpdateView.as_view(),name="update_ques"),
    path("create_ques",QuestionCreateView.as_view(),name="create_ques"),
    path("delete_ques/<int:pk>",QuestionDeleteView.as_view(),name="delete_ques"),
    
    # Answer
    path("Answer",AnswerListView.as_view(),name="list_anwr"),
    path("detail_anwr/<int:pk>",AnswerDetailView.as_view(),name="detail_anwr"),
    path("update_anwr/<int:pk>",AnswerUpdateView.as_view(),name="update_anwr"),
    path("create_anwr",AnswerCreateView.as_view(),name="create_anwr"),
    path("delete_anwr/<int:pk>",AnswerDeleteView.as_view(),name="delete_anwr"),
    
    
    # Subcategory
    path("SubCategory",SubCategoryListView.as_view(),name="list_sub"),
    path("update_sub/<int:pk>",SubCategoryUpdateView.as_view(),name="update_sub"),
    path("detail_sub/<int:pk>",SubCategoryDetailView.as_view(),name="detail_sub"),
    path("create_sub",SubCategoryCreateView.as_view(),name="create_sub"),
    path("delete_sub/<int:pk>",SubCategoryDeleteView.as_view(),name="delete_sub"),
    
    # Category
    path("Category",CategoryListView.as_view(),name="list_c"),
    path("update_c/<int:pk>",CategoryUpdateView.as_view(),name="update_c"),
    path("detail_c/<int:pk>",CategoryDetailView.as_view(),name="detail_c"),
    path("create_c",CategoryCreateView.as_view(),name="create_c"),
    path("delete_c/<int:pk>",CategoryDeleteView.as_view(),name="delete_c"),
    
    # User
    path("User",UserListView.as_view(),name="list_user"),
    path("update_user/<int:pk>",UserUpdateView.as_view(),name="update_user"),
    path("detail_user/<int:pk>",UserDetailView.as_view(),name="detail_user"),
    path("create_user",UserCreateView.as_view(),name="create_user"),
    path("delete_user/<int:pk>",UserDeleteView.as_view(),name="delete_user")
]
