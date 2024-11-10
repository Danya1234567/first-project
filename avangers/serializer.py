from rest_framework.response import Response

from app.models import Technique
from rest_framework import serializers as s

from avangers.models import Comments, Applicaion
from avangers.permissions import IsAdminOrAuthor


class GetCommentSerializer(s.ModelSerializer):
    class Meta:
        model=Comments
        fields='__all__'

        def get_queryset(self,pk):
            comment= Comments.objects.filter(id=pk)
            return comment

        def create(self, validated_data):
            comment = Comments.objects.create(**validated_data)
            return comment

class UpdateCommentSerializer(s.ModelSerializer):
    class Meta:
        model=Comments
        exclude=['user','technique']
        extra_kwargs={
            'title':{'required':False},
            'description':{'required':False},
            'created_at':{'required':False}
        }

        def update(self,instance:Comments, validated_data):

            title= validated_data.pop('title', instance.title)
            description=validated_data.pop('description',instance.description)
            created_at=validated_data.pop('created_at',instance.created_at)

            instance.title = title
            instance.description=description
            instance.created_at=created_at

            instance.save()

            return instance


class DeleteCommentSerializer(s.ModelSerializer):
    class Meta:
        model=Comments
        permission_classes=[IsAdminOrAuthor]
        fields=['id']

        def validate(self, data):
            request = self.context.get('request')
            user = request.user

            comment = Comments.objects.filter(id=data['id']).first()
            if not comment:
                raise s.ValidationError("Комментарий не существует.")
            if comment.user != user:
                raise s.ValidationError("У вас нет прав удалять комментарий.")

            return data


class GetApplicationSerializer(s.ModelSerializer):
    class Meta:
        model=Applicaion
        fields='__all__'

        def get_queryset(self,pk):
            technique= Technique.objects.filter(id=pk)
            return technique


class CreateApplicationSerializer(s.ModelSerializer):
    class Meta:
        model=Technique
        fields='__all__'

        def create(self, validated_data):
            technique = Technique.objects.create(**validated_data)
            return technique

class UpdateApplicationSerializer(s.ModelSerializer):
    class Meta:
        model=Applicaion
        exclude=['user']
        extra_kwargs={
            'title':{'required':False},
            'description':{'required':False},
            'created_at':{'required':False},
            'status':{'required':False},
            'date_of_beging':{'required':False},
            'date_of_end':{'required':False}
        }
        def update(self,instance:Applicaion, validated_data):
            title= validated_data.pop('title', instance.title)
            description=validated_data.pop('description',instance.description)
            created_at=validated_data.pop('created_at',instance.created_at)
            status=validated_data.pop('status',instance.status)
            date_of_beging=validated_data.pop('date_of_beging',instance.date_of_beging)
            date_of_end=validated_data.pop('date_of_end',instance.date_of_end)

            instance.title = title
            instance.description=description
            instance.created_at=created_at
            instance.status=status
            instance.date_of_beging=date_of_beging
            instance.date_of_end=date_of_end

            instance.save()

            return instance


class GetOneApplicationSerializer(s.ModelSerializer):
    class Meta:
        model=Applicaion
        fields='__all__'

        def get_queryset(self,pk):
            technique= Technique.objects.filter(id=pk)
            return technique


class DeleteApplicationSerializer(s.ModelSerializer):
    class Meta:
        model=Applicaion
        permission_classes = [IsAdminOrAuthor]
        fields=['pk']

    def validate(self, data):
        request = self.context.get('request')
        user = request.user

        comment = Comments.objects.filter(id=data['id']).first()
        if not comment:
            raise s.ValidationError("Комментарий не существует.")
        if comment.user != user:
            raise s.ValidationError("У вас нет прав удалять комментарий.")

        return data