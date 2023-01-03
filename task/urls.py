
#Fonksiyon Yöntemi ile Endpoint 

#from django.urls import path
# from .views import (task_list_create, tasks_detail) #fonksiyon class yöntemi ile

# urlpatterns = [
   
#     path('list', task_list_create), #views de yazdığımız classları çapıracağız.
#     path('detail/<int:id>', tasks_detail),
# ]

#CONCRETE VİEWSI YÖNTEMİ İLE ENDPOİNT

#from django.urls import path
# from .views import (
#     Task_List,
#     TaskDetail,
# )

# urlpatterns = [
 
#     path('list/', Task_List.as_view()),
#     path('detail/<int:pk>', TaskDetail.as_view()),
    
# ]

#VIEWSET Yöntemi ile


from django.urls import path, include
from .views import TaskMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register('taskall', TaskMVS)

urlpatterns = [
  
    path('', include(router.urls))
]