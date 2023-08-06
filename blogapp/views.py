from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from . models import BlogPost

class IndexView(ListView):
    template_name="index.html"
    
    # object_listキーの別名を保存
    context_object_name = "orderby_records"
    # クエリを決定
    queryset = BlogPost.objects.order_by('-posted_at')
    paginate_by = 4
    

# 詳細ページ表示用のビュー
class BlogDetail(DetailView):
    template_name="post.html"
    model= BlogPost