from django.shortcuts import render
from .forms import ApplicationForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            employment_status = form.cleaned_data["employment_status"]
            print(first_name, last_name, email, date, employment_status)
    return render(request, "index.html")
