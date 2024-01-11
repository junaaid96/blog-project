from django import forms
from .models import Author

# here forms.ModelForm is a class that will convert our model into a form. We can also use forms.Form to create a form from scratch. AuthorForm is the name of our form.


class AuthorForm(forms.ModelForm):
    # we use Meta class to specify the model we are using and the fields we want to include in our form
    class Meta:
        model = Author
        fields = '__all__'
