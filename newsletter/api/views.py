from rest_framework import generics
from newsletter.models import Join
from .serializers import Joinserializers

class JoinCreateAPIView(generics.CreateAPIView):
    queryset = Join.objects.all()
    serializer_class = Joinserializers
    permission_classes = []
    authentication_classes = []