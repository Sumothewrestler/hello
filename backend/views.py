from rest_framework import viewsets
from rest_framework.response import Response
from .models import Thought
from .serializers import ThoughtSerializer

class ThoughtViewSet(viewsets.ModelViewSet):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializer