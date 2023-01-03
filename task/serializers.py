from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.ModelSerializer):
    
    #oluşturacağımız derializers hangi model ile çalışacaksa belirtiyoruz.
    class Meta:
        model= Task

        fields = (
            'id',
            'todo',
            'description',
            'priority',
            'is_done',
            'created_date',
        )
