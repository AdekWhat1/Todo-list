from django import forms
from django.utils import timezone
from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                }
            ),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")

        if deadline:
            if deadline < timezone.now():
                raise forms.ValidationError("Deadline must be in the future")

        return deadline