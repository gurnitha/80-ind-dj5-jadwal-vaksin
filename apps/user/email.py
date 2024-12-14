# apps/user/email.py

# django modules
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model

User = get_user_model()

# my modules
from user.utils import EmailVerificationTokenGenerator


def send_email_verification(request, id):
    """
    Sends email to the user regarding email verification
    """
    user = User.objects.get(pk=id)
    current_site = get_current_site(request)
    subject = "Request for Email Verification | Vaccine Scheduling App Account"
    message = render_to_string(
        "user/email-verify.html",
        {
            "full_name": user.get_full_name(),
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.id)),
            "token": EmailVerificationTokenGenerator.make_token(user),
        },
    )
    to_email = user.email
    email = EmailMessage(subject, message, to=[to_email])
    return email.send()