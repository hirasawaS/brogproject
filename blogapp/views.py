from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView ,DetailView ,FormView
from . models import BlogPost
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

def index_view(request):
    # レコードの取得
    records = BlogPost.objects.order_by("-posted_at")
    # ページ1個で4レコード
    paginator = Paginator(records , 4)
    page_number = request.GET.get('page' , 1)
    
    pages = paginator.page(page_number)
    
    return render(request , 'index.html' , {'orderby_records':pages})

# # classビューの場合は違う
# class IndexView(ListView):
#     template_name="index.html"
#     context_object_name="orderby_records"
#     queryset = BlogPost.objects.order_by('-posted_at') 
#     paginate_by= 4   

# 詳細ページ表示用のビュー
class BlogDetail(DetailView):
    template_name="post.html"
    model= BlogPost
    
class ScienceView(ListView):
    model= BlogPost
    template_name="science_list.html"
    queryset = BlogPost.objects.filter(category="science").order_by("-posted_at")
    paginate_by=2
    
    context_object_name="science_records"
    
class MusicView(ListView):
    model= BlogPost
    template_name="music_list.html"
    queryset = BlogPost.objects.filter(category="music").order_by("-posted_at")
    paginate_by=2
    context_object_name="music_records"
class DailylifeView(ListView):
    model= BlogPost
    template_name="dailylife_list.html"
    queryset = BlogPost.objects.filter(category="dailylife").order_by("-posted_at")
    paginate_by=2
    context_object_name="dailylife_records"
    
class ContactView(FormView):
    # テンプレート指定
    template_name="contact.html"
    # formを持ってくる
    form_class= ContactForm
    # 成功時のURL
    success_url = reverse_lazy('blogapp:contact')

# フォームのバリデーションを通過したデータがPOSTされたときに呼ばれる
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        
        # メールのタイトルの書式設定
        subject ='お問い合わせ:{}'.format(title)
        
        message = \
            "送信者:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:{3}" \
                .format(name,email,title,message)
        
        # 送信者と受信者
        form_email = 'admin@example.com'
        to_list = ["admin@example.com"]
        # メッセージを設定
        message = EmailMessage(subject=subject , body=message , from_email=form_email , to=to_list)
        # メッセージが送られる
        message.send()
        
        messages.success(
            self.request , 'お問い合わせ完了しました'
        )
        return super().form_invalid(form)