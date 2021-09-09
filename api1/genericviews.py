from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

from .models import Person
from .serilizers import PersonSerilizer

class ListPerson(ListModelMixin, GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerilizer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 
    
    
class CreatePerson(CreateModelMixin, GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerilizer
    
    def post(self, request, *args, **kwargs):
        return self.create(request *args, **kwargs) 