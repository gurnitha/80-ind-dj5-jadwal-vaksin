# apps/user/forms.py

# django modules
from django.contrib.auth.forms import (
    UserCreationForm,
)
from django.contrib.auth import get_user_model

User = get_user_model()


# Form: Sign up form
class SignupForm(UserCreationForm):
    """
    Form to create a new user
    """

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "gender",
            "photo",
            "identity_document_type",
            "identity_document_number",
        ]