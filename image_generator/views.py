# imagegen/views.py

from django.shortcuts import render
from .forms import ImageForm
from .tasks import generate_image
from .models import Image
from celery.result import AsyncResult
# from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


def image_generator_view(request):
    # authentication_classes = [BasicAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            task = generate_image.delay(prompt)
            Image.objects.create(prompt=prompt, task_id=task.id)
    else:
        form = ImageForm()

    # Check task status and get URL if completed
    images = Image.objects.all()
    for img in images:
        result = AsyncResult(img.task_id)
        if result.ready():
            img.image_url = result.result
            img.save()

    return render(request, 'image_generator.html', {'form': form, 'images': images})
