from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "brand", "stock"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_brand(self):
        brand = self.cleaned_data.get("brand", "")
        return strip_tags(brand)

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get("thumbnail", "")
        return strip_tags(thumbnail)
