from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from . models import BlogPost

from django.core.paginator import Paginator

def index_view(request):
    # レコードの取得
    records = BlogPost.objects.order_by("-posted_at")
    # ページ1個で4レコード
    paginator = Paginator(records , 4)
    page_number = request.GET.get('page' , 1)
    
    pages = paginator.page(page_number)
    
    return render(request , 'index.html' , {'orderby_records':pages})

# 詳細ページ表示用のビュー
class BlogDetail(DetailView):
    template_name="post.html"
    model= BlogPost