from django.apps import AppConfig
from .create_model import create_model_emo

class WordConfig(AppConfig):
    name = 'word'
    model = create_model_emo()
