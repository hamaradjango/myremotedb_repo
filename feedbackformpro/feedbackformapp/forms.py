from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    location = forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Location'
            }
        )
    )
    feedback = forms.CharField(help_text="Thanks For Your Valuable Feedback",
        label='Enter Your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )