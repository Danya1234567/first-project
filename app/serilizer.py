from rest_framework.response import Response

from app.models import Technique
from rest_framework import serializers as s, status


class CreateNewObjectSerializer(s.ModelSerializer):
    class Meta:
        model = Technique
        fields = '__all__'

        def create(self, validated_data):
            current_user = self.context['request'].user
            if not current_user.is_authenticated or current_user.role != 'arendator':
                return s.ValidationError('You are not authorized to create a new object')
            return Technique.objects.create(**validated_data)

        def update(self, instance, validated_data):
            current_user = self.context['request'].user
            if not current_user.is_authenticated or current_user.role != 'arendator':
                return s.ValidationError('You are not authorized to update this object')
            return super().update(instance, validated_data)



class TechniqueDetailSerializer(s.ModelSerializer):
    class Meta:
        model = Technique
        fields = '__all__'



class TechByIdSerializer(s.ModelSerializer):
    class Meta:
        model = Technique
        fields = '__all__'

        def get_queryset(self,pk):
            return Technique.objects.filter(id=pk)


class TechniqueDeleteViewSerializer(s.ModelSerializer):
    class Meta:
        model = Technique
        fields = '__all__'

        def delete(self, request, **kwargs):
            title = request.query_params.get('title')
            technique_id = kwargs.get('pk')
            if title:
                technique = Technique.objects.get(title=title)
                technique.delete()
                return Response({"message": 'Техника удалена!'}, status=status.HTTP_204_NO_CONTENT)

            if technique_id:
                technique = Technique.objects.get(id=technique_id)
                technique.delete()
                return Response({"message": 'Техника удалена!'}, status=status.HTTP_204_NO_CONTENT)

            elif Technique.DoesNotExist:
                return Response({'error': 'Техника не найдена!'}, status=status.HTTP_404_NOT_FOUND)

            return Response({'error': 'Наименование или id техники не указано!'}, status=status.HTTP_400_BAD_REQUEST)

        def create(self, validated_data):
            current_user = self.context['request'].user
            if not current_user.is_authenticated or current_user.role != 'arendator':
                return s.ValidationError('You are not authorized to delete a new object')
            return Technique.objects.create(**validated_data)

        def update(self, instance, validated_data):
            current_user = self.context['request'].user
            if not current_user.is_authenticated or current_user.role != 'arendator':
                return s.ValidationError('You are not authorized to delete this object')
            return super().update(instance, validated_data)