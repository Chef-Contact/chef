import django_filters
from apps.host.models import ChefRegister

class ChefRegisterFilter(django_filters.FilterSet):
    class Meta:
        model = ChefRegister
        fields = {
            'question_1': ['exact'],
            'question_2': ['exact'],
            'question_3': ['exact'],
            'question_4': ['exact'],
            'question_5': ['exact'],
            'question_6': ['exact'],
            'question_7': ['exact'],
            'question_8': ['exact'],
            'question_9': ['exact'],
            'question_10': ['exact']
        }

