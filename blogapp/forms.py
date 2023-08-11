from django import forms



class ContactForm(forms.Form):
    
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message= forms.CharField(label='メッセージ' , widget=forms.Textarea)
    
    def __init__(self , *args , **kwargs):
        # 親クラスを初期化
        super().__init__(*args ,**kwargs)
        
# classはinputタグを出力するクラスを指定
        self.fields['name'].widget.attrs['placeholder'] = \
            'お名前'
        self.fields['name'].widget.attrs['class'] = \
            'form-control'
        
        self.fields['email'].widget.attrs['placeholder'] = \
            'メール'
        self.fields['email'].widget.attrs['class'] = \
            'form-control'
        
        self.fields['title'].widget.attrs['placeholder'] = \
            'タイトル'
        self.fields['title'].widget.attrs['class'] = \
            'form-control'
        
        self.fields['message'].widget.attrs['placeholder'] = \
            'メッセージ'
        self.fields['message'].widget.attrs['class'] = \
            'form-control'
        
        


            
        
        
        
        
    