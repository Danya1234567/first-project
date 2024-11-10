
from rest_framework import serializers as s

from users.models import User


class RegisterSerializers(s.ModelSerializer):
    password = s.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'surname','password','avatar','email', 'date_of_birth', 'role']


    def create(self, validated_data):
        avatar = validated_data.get('avatar', 'media/avatar/icon.png')
        role = validated_data.get('role', 'user')
        user = User(
            username=validated_data['username'],
            role=role,
            avatar=avatar,
            surname=validated_data['surname'],
            email=validated_data['email'],
            date_of_birth=validated_data.get('date_of_birth')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class UserSerializer(s.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']



class UserUpdateSerializer(s.ModelSerializer):
    class Meta:
        model = User
        fields = ['surname', 'name', 'avatar', 'email','password', 'date_of_birth', 'role']
        extra_kwargs = {
            'date_of_birth': {'required': False},
            'email': {'required': False},
            'name': {'required': False},
            'surname': {'required': False},
            'password':{'required': False},
            'avatar': {'required': False}
        }

    def update(self, instance: User, validated_data):
        avatar = validated_data.pop('avatar', instance.avatar)
        role = validated_data.pop('role', instance.role)
        surname = validated_data.pop('surname', instance.first_name).capitalize()
        name = validated_data.pop('name', instance.last_name).capitalize()
        email = validated_data.pop('email', instance.email)
        date_of_birth = validated_data.pop('date_of_birth', instance.date_of_birth)
        password = validated_data.pop('password', instance.password)


        instance.email = email
        instance.avatar = avatar
        instance.role = role
        instance.password = password
        instance.date_of_birth = date_of_birth
        instance.first_name = surname
        instance.last_name = name

        return super().update(instance, validated_data)

