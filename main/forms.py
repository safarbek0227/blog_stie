import email
from django.forms import EmailInput, ModelForm
from .models import Comment
from django.forms.widgets import TextInput, Textarea

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # fields = ["name", "message"]
        fields = "__all__" #Shu modelni hamma maydoni uchun form hosil qilish
        exclude = ["post"]
        widgets = {
            "name":TextInput(attrs={'class':'input', 'placeholder':'ismingiz'}),
            'email':EmailInput(attrs={'class':'input', 'placeholder':'email'}),
            "body":Textarea( attrs={'class':'textarea', 'placeholder':'Your comment...','rows':4, 'cols':50}  )

        }