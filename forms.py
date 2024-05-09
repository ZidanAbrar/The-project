from django import forms
from movie.models import Review, RATE_CHOICES

class RateForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
	rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

	class Meta:
		model = Review
		fields = ('text', 'rate')

class MovieFilterForm(forms.Form):
    min_rating = forms.FloatField(label='Minimum Rating', required=False, widget=forms.NumberInput(attrs={'min': 1, 'max': 10, 'step': 0.1}))
    max_rating = forms.FloatField(label='Maximum Rating', required=False, widget=forms.NumberInput(attrs={'min': 1, 'max': 10, 'step': 0.1}))