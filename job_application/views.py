from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        # Validate the form
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            employment_status = form.cleaned_data["employment_status"]

            # Save the form data to the database
            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date, employment_status=employment_status)
            
            # Message to inform the user that the application was submitted successfully
            messages.success(request, "Your application has been submitted successfully!")

            # Send an email to the user
            message_body = f"Hi {first_name},\n\nThank you for applying for the job. We will get back to you soon.\n\nBest regards,\nThe Team"
            email_message = EmailMessage("Job Application Confirmation", message_body, to=[email])
            email_message.send()

    return render(request, "index.html")

