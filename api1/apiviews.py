from rest_framework import response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serilizers import PersonSerilizer, ToDoSerilizses
from .models import Person, ToDo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def home(request, pk=None):
    if request.method == "GET":
        id=pk
        if id is not None:
            person = Person.objects.get(id=id)
            serilize = PersonSerilizer(person)
            return Response(serilize.data)
       
        
                
        person = Person.objects.all()
        serilize = PersonSerilizer(person, many=True)
        return Response(serilize.data) 
    
    if request.method == "POST":
        data = request.data
        serilize = PersonSerilizer(data=data)
        if serilize.is_valid():
            serilize.save()
            res = {"msg":"Data save"}
            return Response(res)
        else:
            return Response(serilize.errors)
    
    
    if request.method == "PUT":
        id = pk
        p = Person.objects.get(id=id)
        serilize = PersonSerilizer(p, data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response({"msg":"Update successfuly"})
        return Response({"msg":"Update Fail"})
    
    if request.method == "PATCH":
        id = pk
        p = Person.objects.get(id=id)
        serilize = PersonSerilizer(p, data=request.data, partial=True)
        if serilize.is_valid():
            serilize.save()
            return Response({"msg":"Update successfuly"})
        return Response({"msg":"Update Fail"})
    
    
    if request.method == "DELETE":
        id = pk
        if id is not None:
            p = Person.objects.get(id=id)
            p.delete()
            return Response({"msg":"Delete successfuly"})
        return Response({"msg":"Delete Fail"})
    

#########################
"""
Class base view
"""
####################

class ToDOView(APIView):
    def get(self,request, **kwargs):
        try:
            pk = kwargs["id"]
        except:
            pk = None
        if pk is not None:
            todo = ToDo.objects.get(id=pk)
            serializer = ToDoSerilizses(todo)
            return Response(serializer.data)
        todo = ToDo.objects.all()
        serializer = ToDoSerilizses(todo, many=True)
        return Response(serializer.data)
    
    def post(self, request, **kwargs):
        data = request.data
        serializer = ToDoSerilizses(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Save Successfuly"})
        return Response(serializer.errors)
        
    def patch(self, request, **kwargs):
        try:
            
            todo = ToDo.objects.get(id=kwargs['id'])
            print("try block")
            data = request.data
            serializer = ToDoSerilizses(todo, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Data Update Successfuly"})
            return Response(serializer.errors)
        except:
            print("except block")
            return Response({"msg":"Some thinks wrong"})
        
    def delete(self, request, **kwargs):
        try:
            id = kwargs['id']
            todo = ToDo.objects.get(id=id)
            todo.delete()
            return Response({"msg":"Delete successfuly"})
        except:
            return Response({"msg":"Item Don't Match"})
        
    

@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def todoView(request, id=None):
    pk = id
    if request.method == "GET":
        if pk is not None:
            todo = ToDo.objects.get(id=pk)
            serializer = ToDoSerilizses(todo)
            return Response(serializer.data)
        todo = ToDo.objects.all()
        serializer = ToDoSerilizses(todo, many=True)
        return Response(serializer.data)
    
    
    if request.method == "POST":
        data = request.data
        serializer = ToDoSerilizses(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Save Successfuly"})
        return Response(serializer.errors)
    
    if request.method == "PATCH":
        todo = ToDo.objects.get(id=pk)
        data = request.data
        serializer = ToDoSerilizses(todo, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Update Successfuly"})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        try:
            id = pk
            todo = ToDo.objects.get(id=id)
            todo.delete()
            return Response({"msg":"Delete successfuly"})
        except:
            return Response({"msg":"Item Don't Match"})
            