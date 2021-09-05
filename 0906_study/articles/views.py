from .models import Article
from django.shortcuts import render
# Create your views here.

# 작성한 모든 게시글을 출력
def index(request):
    # 1. 모든 게시글 조회
    articles = Article.objects.all() # 쿼리셋 리턴한다.
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)



def new(request):
    return render(request, 'articles/new.html')


def create(request):
    return render(request, 'articles/create.html')
    # new로부터 title과 content를 받아서 저장

    # 1.
    # 2. 
    # 3.  


def detail(request, pk):
    pass


def delete(request, pk):
    pass


def edit(request, pk):
    pass


def update(request, pk):
    pass
