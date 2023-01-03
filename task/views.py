from django.shortcuts import render, get_object_or_404

from .models import Task #üzerinde çalışacağımız tabloyu(modeli import ediyoruz)
from .serializers import TaskSerializers # modele ait serializers'i import ediyoruz.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#concrete yöntemi ile 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#viewSet Yöntemi için import ediyorum.
from rest_framework.viewsets import ModelViewSet

@api_view(['GET','POST'])
def task_list_create(request):
    if request.method== 'GET':
        tasks =Task.objects.filter(is_done=False)
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer =TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'DELETE', 'PUT'])
def tasks_detail(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'GET':
        # todo = Todo.objects.get(id=id)
        serializer = TaskSerializers(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializers(data=request.data, instance=task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response({'message': 'todo deleted succesfully'})
 




##CONCRETE VİEWSI YÖNTEMİ İLE ENDPOİNT 
class Task_List(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    # lookup_field = 'id' # url'ye pk yazarsak buraya lookup_field= id yazarsak eşitlemiş oluruz.


#VİEWSET YÖNTEMİ İLE


class TaskMVS(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers