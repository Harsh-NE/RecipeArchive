from django import forms
from .models import Dish
class DishForm(forms.ModelForm):
    class Meta:
        model=Dish
        fields=['dish_name','dish_desc','dish_recipe','dish_type','dish_image']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Make all fields optional
            for field in self.fields:
                self.fields[field].required = False
        # In forms.py
        def save(self, commit=True):
            instance = super().save(commit=False)
            
            # For each field in the form
            for field_name in self.fields:
                # Skip fields that were actually submitted
                if field_name in self.changed_data:
                    continue
                    
                # For image field specifically
                if field_name == 'image' and 'image-clear' not in self.data:
                    # Keep original image if not cleared and no new one uploaded
                    if self.instance and self.instance.image:
                        instance.image = self.instance.image
                # For all other fields
                elif hasattr(self.instance, field_name):
                    # Keep original value
                    original_value = getattr(self.instance, field_name)
                    setattr(instance, field_name, original_value)
            
            if commit:
                instance.save()
            
            return instance