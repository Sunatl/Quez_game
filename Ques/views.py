
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from .models import *
from django.http import HttpResponse
from django.template import loader




def base(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())


class QuestionListView(ListView):
    model = Question
    template_name = 'list_ques.html'
    
class QuestionDetailView(DetailView):
    model = Question
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["answer"] = Answer.objects.filter(ques_id = self.kwargs['pk'])
        return context
    
    template_name = 'detail_ques.html'
    
class QuestionCreateView(CreateView):
    model = Question
    template_name = 'create_ques.html'
    fields = ['title','description', 'user','category','image','resume']
    success_url = reverse_lazy('list_ques') 
    
    
class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'update_ques.html'
    fields = ['title','description', 'user','category','image','resume']
    success_url = reverse_lazy('list_ques') 
    
    
class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'delete_ques.html'
    success_url = reverse_lazy('list_ques') 
    
    
    
    
    
    
    
# Answer 1111111111111111111111111111111111111111111111111111111111111111111111111111
class AnswerListView(ListView):
    model = Answer
    template_name = 'list_anwr.html'
    
class AnswerDetailView(DetailView):
    model = Answer
    template_name = 'detail_anwr.html'
    
class AnswerCreateView(CreateView):
    model = Answer
    template_name = 'create_anwr.html'
    fields = ['title','description', 'user','ques_id','image','resume']
    success_url = reverse_lazy('list_anwr') 
    
    
class AnswerUpdateView(UpdateView):
    model = Answer
    template_name = 'update_anwr.html'
    fields = ['title','description', 'user','ques_id','image','resume']
    success_url = reverse_lazy('list_anwr') 
    
    
class AnswerDeleteView(DeleteView):
    model = Answer
    template_name = 'delete_anwr.html'
    success_url = reverse_lazy('list_anwr') 
    
    
# Subcategory `111111111111111111111`

class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'list_sub.html'
    
class SubCategoryDetailView(DetailView):
    model = SubCategory
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["ques"] = Question.objects.filter(category = self.kwargs['pk'])
        return context
    template_name = 'detail_sub.html'
    
class SubCategoryCreateView(CreateView):
    model = SubCategory
    template_name = 'create_sub.html'
    fields = ['category','title']
    success_url = reverse_lazy('list_sub') 
    
    
class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    template_name = 'update_sub.html'
    fields = ['category','title']
    success_url = reverse_lazy('list_sub') 
    
    
class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = 'delete_c.html'
    success_url = reverse_lazy('list_sub') 
    
    
# Category
class CategoryListView(ListView):
    model = Category
    template_name = 'list_c.html'
    
class CategoryDetailView(DetailView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["sabcategory"] = SubCategory.objects.filter(category = self.kwargs['pk'])
        return context
    template_name = 'detail_c.html'
    
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'create_c.html'
    fields = ['name']
    success_url = reverse_lazy('list_c') 
    
    
class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'update_c.html'
    fields = ['name']
    success_url = reverse_lazy('list_c') 
    
    
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'delete_c.html'
    success_url = reverse_lazy('list_c') 
    
    
# username

class UserListView(ListView):
    model = User
    template_name = 'list_user.html'
    context_object_name = "object_list"
    
class UserDetailView(DetailView):
    model = User
    template_name = 'detail_user.html'
    
class UserCreateView(CreateView):
    model = User
    template_name = 'create_user.html'
    fields = ['fulname','age', 'phone','username','image']
    success_url = reverse_lazy('list_user') 
    
    
class UserUpdateView(UpdateView):
    model = User
    template_name = 'update_user.html'
    fields = ['fulname','age', 'phone','username','image']
    success_url = reverse_lazy('list_user') 
    
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('list_user') 