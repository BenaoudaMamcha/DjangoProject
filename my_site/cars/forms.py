from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length =100)
    last_name = forms.CharField(label='last Name', max_length =100)
    email = forms.EmailField(label='Email')
     # widgets + attribut
    reviw = forms.CharField(label='please write your review here',widget=forms.Textarea(attrs={'class':'myform'}))
    
   
    
    
    
    