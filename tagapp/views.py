from rest_framework import serializers
from tagapp.forms import SnippetForm
from rest_framework.serializers import Serializer
from tagapp.models import TagModel, TagUser
from tagapp.serializers import TagDetailSerializer, TagSerializer, TagUserCreateSerializer, TagUserDetailSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action

class TagView(viewsets.ModelViewSet):
    queryset = TagUser.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = TagUserCreateSerializer

    def get_serializer_class(self):
        if self.action=='list':
           return TagUserDetailSerializer
        return super().get_serializer_class()
    
    @action(detail=True, methods=['GET'],)
    def tag(self,request,pk=None):
        tagmodels = TagModel.objects.all()
        if pk:
            tagmodel = TagModel.objects.filter(id=pk).first()
            serializer = TagDetailSerializer(tagmodel)
        else:
            serializer = TagSerializer(tagmodels,many = True)
        return Response(serializer.data,status=200)

@login_required(login_url='admin/login')
def home(request):
    form=SnippetForm()
    context={"form":form,"tags":TagUser.objects.filter(auth_user=request.user)} 
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            instance = form.instance
            user = request.user
            taguser = TagUser.objects.filter(auth_user=user,title=instance)
            if not taguser:
                taguser = TagUser.objects.create(auth_user=user,title=instance)
            context={"form":form,"tags":TagUser.objects.filter(auth_user=request.user)}
    return render(request,"index.html",context=context)