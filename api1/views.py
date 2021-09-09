
from .serilizers import PersonSerilizer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Person
from django.shortcuts import render
import io
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

# Create your views here.



########################################
'''
Class Base View
'''
#######################################



@method_decorator(csrf_exempt, name="dispatch")
class Home(View):
    def get(self, request):
        obj = Person.objects.all()
        serilize = PersonSerilizer(obj, many=True)
        print(serilize.data)
        json_data = JSONRenderer().render(serilize.data)
        print(json_data)
        return HttpResponse(json_data)

   
    def post(self, request):
        data = request.body
        stream = io.BytesIO(data)
        native_data = JSONParser().parse(stream)
        person_data = PersonSerilizer(data=native_data)
        if person_data.is_valid():
            person_data.save()
            msg = {'msg':"user create"}
            return JsonResponse(msg, safe=False)
        else:  
            msg = person_data.errors
            return JsonResponse(msg, safe=False)
        
    def put(self, request):
        Inputdata = request.body
        streamdata = io.BytesIO(Inputdata)
        pythonData = JSONParser().parse(streamdata)
        id = pythonData.get("id", None)
        if id is not None:
            info = Person.objects.get(id=id)
            serilizer = PersonSerilizer(info, data=pythonData, partial=True)
            print(serilizer)
            if serilizer.is_valid():
                serilizer.save()
                res = {"msg":"update complite"}
                j = JSONRenderer().render(res)
                return HttpResponse(j)
        else:
            res = {"msg":"User Does nt exits Try Again"}
            j = JSONRenderer().render(res)
            return HttpResponse(j)
        
    def delete(self, request):
        data = request.body
        stream = io.BytesIO(data)
        pydata = JSONParser().parse(stream)
        id = pydata.get("id", None)
        print(id)
        if id is not None:
            obj = Person.objects.get(id=id)
            obj.delete()
            res = {"msg":"Delete successfuly"}
            j = JSONRenderer().render(res)
            return HttpResponse(j)
        else:
            res = {"msg":"User Does not exits Try Again"}
            j = JSONRenderer().render(res)
            return HttpResponse(j)
        
        
 
        


#####################################
'''
Function base view

'''
###############################

# def home(request):
#     obj = Person.objects.all()
#     serilize = PersonSerilizer(obj, many=True)
#     print(serilize.data)
#     json_data = JSONRenderer().render(serilize.data)
#     print(json_data)
#     return HttpResponse(json_data)
    # print(serilize.data)
    # return JsonResponse(serilize.data, safe=False)

# @csrf_exempt
# def registration(request):
#     msg = ""
#     if request.method == "POST":
#         data = request.body
#         stream = io.BytesIO(data)
#         native_data = JSONParser().parse(stream)
#         person_data = PersonSerilizer(data=native_data)
#         if person_data.is_valid():
#             person_data.save()
#             msg = {'msg':"user create"}
#             return JsonResponse(msg, safe=False)
#         else:  
#             msg = person_data.errors
#             return JsonResponse(msg, safe=False)
#     else:
#         msg = {"msg":""}
#         return JsonResponse(msg, safe=False)
# @csrf_exempt 
# def infoupdate(request):
#     if request.method == "PUT":
#         Inputdata = request.body
#         streamdata = io.BytesIO(Inputdata)
#         pythonData = JSONParser().parse(streamdata)
#         id = pythonData.get("id", None)
#         if id is not None:
#             info = Person.objects.get(id=id)
#             serilizer = PersonSerilizer(info, data=pythonData, partial=True)
#             print(serilizer)
#             if serilizer.is_valid():
#                 serilizer.save()
#                 res = {"msg":"update complite"}
#                 j = JSONRenderer().render(res)
#                 return HttpResponse(j)
   
#     res = {"msg":"User Does nt exits Try Again"}
#     j = JSONRenderer().render(res)
#     return HttpResponse(j)  

# @csrf_exempt
# def infodelete(request):
#     if request.method == "DELETE":
#         data = request.body
#         stream = io.BytesIO(data)
#         pydata = JSONParser().parse(stream)
#         id = pydata.get("id", None)
#         print(id)
#         if id is not None:
#             obj = Person.objects.get(id=id)
#             obj.delete()
#             res = {"msg":"Delete successfuly"}
#             j = JSONRenderer().render(res)
#             return HttpResponse(j)
#     res = {"msg":"User Does not exits Try Again"}
#     j = JSONRenderer().render(res)
#     return HttpResponse(j)