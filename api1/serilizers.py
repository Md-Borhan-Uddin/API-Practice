
from rest_framework import serializers
from .models import Person, ToDo

class PersonSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    
    def create(self, validat_data):
        return Person.objects.create(**validat_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
    
    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("password to short")
        return value



class ToDoSerilizses(serializers.ModelSerializer):
    
    class Meta:
        model = ToDo
        fields = '__all__'    
    
    def create(self, validate_data):
        return ToDo.objects.create(**validate_data)
    
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.descriptions = validated_data.get("descriptions", instance.descriptions)
        instance.updated = validated_data.get("updated", instance.updated)
        instance.save()
        return instance