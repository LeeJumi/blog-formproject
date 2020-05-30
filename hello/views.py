from django.shortcuts import render, redirect
from .models import Blog #모델의 존재를 알려주는 코드
from django.utils import timezone #장고 안에 있는 타임존을 임포트하라는 뜻
from .forms import BlogPost
# Create your views here.
def home(request):
    blog = Blog.objects.all() #blog라는 변수안에 Blog모델의 objects객체 all()전부를 넣어줘
    return render(request,'home.html',{'blogs':blog})#blog에 담은 것들을 blogs라는 이름으로 home.html에 전해줘


def create(request):
    if request.method == 'POST': #POST로 요청이 들어오면 
        blog = Blog()#Blog 모델의 내용들을 blog라는 변수에 담고
        blog.title = request.POST['title'] #블로그라는 이름에 담긴 내용을 타이틀이란 이름으로 가져옴
        blog.body = request.POST['body'] #블로그라는 이름에 담긴 내용을 바디이란 이름으로 가져옴 (바디라고 모델에 적었으니 통일시켜야함)
        blog.pub_date = timezone.datetime.now()#시간을 가져올 것
        blog.save()#블로그를 저장할 것

        return redirect('/') 
    else:
        return render(request, 'create.html')

def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'new.html',{'forms':form})