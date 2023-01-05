from rest_framework import serializers
from .models import Paint

class PaintSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Paint
        fields = ('name','img','price','author','description')

    def create(self, validated_data):
        """Crear y devolver un nuevo usuario"""
        cuadro = Paint.objects.create(
            name=validated_data['name'],
            img=validated_data['img'],
            author=validated_data['author'],
            price=validated_data['price'],
            description=validated_data['description'],
            

        )
        return cuadro
    
class PaintLastSerializer(serializers.Serializer):
    cant = serializers.IntegerField()