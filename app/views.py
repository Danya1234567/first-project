

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from app.models import Technique
from app.serilizer import CreateNewObjectSerializer, TechByIdSerializer,TechniqueDetailSerializer, TechniqueDeleteViewSerializer



class TechinquePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
class TechniqueListView(generics.ListAPIView):
    queryset = Technique.objects.all()
    serializer_class = TechniqueDetailSerializer
    pagination_class = TechinquePagination

class TechByidView(generics.RetrieveAPIView):
    queryset = Technique.objects.all()
    serializer_class = TechByIdSerializer
    lookup_field = 'pk'



class TechniqueCreateView(generics.CreateAPIView):
    queryset = Technique.objects.all()
    serializer_class = CreateNewObjectSerializer


class TechniqueDeleteView(generics.DestroyAPIView):
    queryset = Technique.objects.all()
    serializer_class = TechniqueDeleteViewSerializer
    lookup_field = 'pk'
