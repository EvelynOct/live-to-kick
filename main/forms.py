from django.forms import ModelForm
from main.models import Product
# Assignmet 6
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "thumbnail", "is_featured"]

    def clean_title(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)