from rest_framework.serializers import ModelSerializer
from webapp.models import Quotes


class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['id', 'text', 'created_at', 'status',
                  'author_name', 'author_email', 'rating']