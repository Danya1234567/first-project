from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from avangers.models import Comments, Applicaion
from avangers.permissions import IsAdminOrAuthor
from avangers.serializer import GetCommentSerializer, UpdateCommentSerializer, DeleteCommentSerializer, \
    GetApplicationSerializer, CreateApplicationSerializer, UpdateApplicationSerializer, GetOneApplicationSerializer, \
    DeleteApplicationSerializer


# Create your views here.


class GetCreateComments(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = GetCommentSerializer


class UpdateComments(generics.UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = UpdateCommentSerializer
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAdminOrAuthor]

    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return Comments.objects.filter(pk=pk)


class DeleteComment(generics.DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = DeleteCommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAuthor]
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):

        serializer = self.get_serializer(data={'id': kwargs.get('pk')}, context={'request': request})
        serializer.is_valid(raise_exception=True)

        return super().delete(request, *args, **kwargs)


class GetApplication(generics.ListCreateAPIView):
    queryset = Applicaion.objects.all()
    serializer_class = GetApplicationSerializer
    permission_classes = [IsAuthenticated]


class CreateApplication(generics.CreateAPIView):
    serializer_class = CreateApplicationSerializer
    permission_classes = [IsAuthenticated]

class UpdateApplication(generics.UpdateAPIView):
    queryset = Applicaion.objects.all()
    serializer_class = UpdateApplicationSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrAuthor]


class GetByApplication(generics.ListAPIView):
    serializer_class = GetOneApplicationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

class DeleteApplication(generics.DestroyAPIView):
    queryset = Applicaion.objects.all()
    permission_classes=[IsAdminOrAuthor]
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        application = self.get_object()
        if application.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)