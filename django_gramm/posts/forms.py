from cloudinary.forms import CloudinaryFileField
from django import forms

from . import models


class CreatePost(forms.ModelForm):
    images = CloudinaryFileField()

    class Meta:
        model = models.Post
        fields = ["title", "images", "tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["images"].options = {
            "tags": "new_image",
            "format": "png",
            "crop": "pad",
            "width": 600,
            "height": 400,
            "quality": "auto",
        }
