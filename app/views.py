from app.models import Imagekit
from django.shortcuts import render
from django.contrib import messages
from app.helpers import ImagekitClient

# Create your views here.


def index(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        imagekit = ImagekitClient(file)
        result = imagekit.upload_media
        print(result)
        Imagekit.objects.create(
            file_url=result["url"],
        )
        messages.success(request, "Email sent successfully")
    media_files = Imagekit.objects.all()
    return render(request, "index.html", {"media_files": media_files})
