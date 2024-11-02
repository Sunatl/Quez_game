from django.db import models


class User(models.Model):
    fulname = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField( max_length=50)
    username = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to="static/images",null=True,blank=True)
    def __str__(self):
        return self.username
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title


class Question(models.Model):
    title  = models.CharField(max_length=50, unique=True)
    description =  models.TextField()
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images",null=True,blank=True)
    resume = models.FileField(upload_to='static/images',null=True,blank=True)
    created_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
       
    def __str__(self):
        return  self.title
    
    
class Answer(models.Model):
    title  = models.CharField(max_length=50)
    description =  models.TextField()
    ques_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images",null=True,blank=True)
    resume = models.FileField(upload_to='static/images',null=True,blank=True)
    created_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
       
    def __str__(self):
        return  self.title