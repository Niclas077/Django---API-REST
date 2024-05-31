#utils
from typing import Any
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http.response import HttpResponse as HttpResponse, JsonResponse
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import VehiculoSerializers

#TEMPLATES
def index(request):
    return render(request, 'index.html')



def formularioP(request):
     return render(request, 'form.html')
 
def putview(request):
    return render(request, 'putview.html')

def dlview(request):
    return render(request,'delete.html')

"""
PETICIONES HTTP
esta vista se encarga de generar la solicitud post para crear el recurso vehiculo
"""
#GET
def gettemplate(request):
    vehiculos = Vehiculos.objects.order_by('id')
    return render(request, 'getview.html',{'Vehiculos': vehiculos})
#PUT
class vehiculo_update(View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('vehiculoid')
        if not id:
         return HttpResponse('ID is required', status=400) 
        
        
        print(f"Actualizando vehiculo con ID:{id} ")
        vehiculo = get_object_or_404(Vehiculos, id=id)
        
        data = {
            'marca':request.POST.get('marca'),
            'anyo': request.POST.get('anyo'),
            'color': request.POST.get('color')
        }
        
        serializer = VehiculoSerializers(vehiculo, data=data)
        if(serializer.is_valid()):
            serializer.save()
            return redirect('/index')
        else:
            return redirect('/putview')
        

#POST
@api_view(['POST'])
def addVh(request):
    if request.method == 'POST':
        serializer = VehiculoSerializers(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            print(Response(serializer.data,status=status.HTTP_201_CREATED))
            return redirect('/index')
        else:
            print(Response(serializer.data,status=status.HTTP_400_BAD_REQUEST))
            return redirect('/formulario')   
            

#DELETE
@api_view(['POST'])
def delete_vehiculos(request):
    if request.method=='POST':
        id = request.POST.get('id')
        try:
            vehic = Vehiculos.objects.get(id=id)
            vehic.delete()
            print(f"vehiculo con id:{id} eliminado")
            return redirect('/index')
        except Vehiculos.DoesNotExist:
            print("El vehiculo no existe")
            return redirect('/dlview')
    else:
        return JsonResponse({'error': "Invalid Method Request"}, status=400)
            

class DataViews(View):    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id=0):
        if id > 0:
            vehiculos=list(Vehiculos.objects.filter(id=id).values())
            if len(vehiculos) > 0:
                vehiculof = vehiculos[0]
                data={'messagge':"Success", 'vehiculos':vehiculof}
            else:
                 data={'messagge':"Vehiculo no encontrado"}
            return JsonResponse(data)
        else:  
            vehiculos = list(Vehiculos.objects.order_by('id').values()) #Es necesario serializar los datos de esta forma para que python lo pueda convertir a JSON
            if len(vehiculos) > 0 :
                data = {
                    'message':"Success", 
                    'vehiculos': vehiculos
                }
            else:
                data = {
                    'message':"Vehiculos no encontrados", 
                }
            return JsonResponse(data)
        
    def post(self,request):
         jd= json.loads(request.body) #convierte el formato del body en un JSON para poder crear el recurso en la base de datos
         Vehiculos.objects.create(marca=jd['marca'],anyo=jd['anyo'],color=jd['color'])
         data = {'message':"Success"}
         return JsonResponse(data)
     
    def put(self,request,id):
        jd=json.loads(request.body)
        vehiculos=list(Vehiculos.objects.filter(id=id).values())
        if len(vehiculos) > 0:
            vh = Vehiculos.objects.get(id=id)
            vh.marca = jd['marca']
            vh.anyo = jd['anyo']
            vh.color = jd['color']
            vh.save()
            data = {'messagge':"Success"}
        else:
            data={'messagge':"Vehiculo no encontrado"}
        return JsonResponse(data)
        
    def delete(self,request,id):
        vehiculos = list(Vehiculos.objects.filter(id=id).values()) # valida que exista
        if len(vehiculos) > 0 :
            vh = Vehiculos.objects.get(id=id) #Trae el recurso
            vh.delete()
            data={
                'messagge': "El vehiculo ha sido eliminado de la base de datos con exito"
            }
        else:
            data={'messagge': 'Vehiculo no encontrado'}
        return JsonResponse(data)
    
    
# Rest Framework

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculos.objects.all()
    serializer_class = VehiculoSerializers
    

    