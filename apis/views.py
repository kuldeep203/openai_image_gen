from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from image_generator.models import Image
from .serializers import ImageSerializer
from image_generator.tasks import generate_image
from celery.result import AsyncResult
# from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


class ImageGenerationView(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        prompt = request.data.get('prompt')
        # seed = request.data.get('seed', None)
        if not prompt:
            return Response({'error': 'Prompt is required.'}, status=status.HTTP_400_BAD_REQUEST)

        task = generate_image.delay(prompt)
        image = Image.objects.create(prompt=prompt, task_id=task.id)
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
