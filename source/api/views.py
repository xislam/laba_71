from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import QuoteSerializer
from webapp.models import Quotes, QUOTE_APPROVED


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class QuoteViewSet(ModelViewSet):
    queryset = Quotes.objects.none()
    serializer_class = QuoteSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Quotes.objects.all()
        return Quotes.objects.filter(status=QUOTE_APPROVED)

    # доступ к изменению и удалению цитат
    # только для вошедших пользователей
    # ...
    # название точки входа для проверки
    # доступно в: self.action

    @action(methods=['post'], detail=True)
    def rate_up(self, request, pk=None):
        quote = self.get_object()
        quote.rating += 1
        quote.save()
        return Response({'id': quote.pk, 'rating': quote.rating})

    # def rate_down
    # ...


# здесь может понадобится точка входа для выдачи кодов и названий статусов,
# чтобы передавать их на клиент с сервера, а не копировать в код клиента.
# (по заданию не обязательно, но желательно).
