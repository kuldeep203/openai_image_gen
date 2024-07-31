import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Initialize Django-environ
env = environ.Env()

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))  # Read .env file

# imagegen/tasks.py

from celery import shared_task
import openai

openai.api_key = env('OPENAI_KEY')


@shared_task
def generate_image(prompt):
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)

    return image_url
