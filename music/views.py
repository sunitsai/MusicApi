from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import *
from rest_framework.response import Response
from . import models
from django.http import Http404
from . import utils


# Create your views here.
class AudioView(APIView):
    def get_serializer(self, request_type, metadata=None, pk=None):
        if self.file_type == "song":
            SerializerClass = SongSerializer
            ModelName = models.Song
        elif self.file_type == "podcast":
            SerializerClass = PodcastSerializer
            ModelName = models.Podcast
        elif self.file_type == "audiobook":
            SerializerClass = AudioBookSerializer
            ModelName = models.AudioBook
        else:
            return utils.Errors({"message" : "audioFileType is not appropriate."})

        if request_type.lower() == "post" and metadata:
            return SerializerClass(data=metadata)
        
        elif request_type.lower() == "get":
            if pk:
                try:
                    obj = ModelName.objects.get(pk=pk)
                    return SerializerClass(obj)
                except ModelName.DoesNotExist:
                    return utils.Errors({"message" : "id is not appropriate."})
            else:
                objects = ModelName.objects.all()
                return SerializerClass(objects, many=True)
        
        elif request_type.lower() == "put":
            try:
                obj = ModelName.objects.get(pk=pk)
                return SerializerClass(obj, data=metadata, partial=True)
            except ModelName.DoesNotExist:
                return utils.Errors({"message" : "id is not appropriate."})

        elif request_type.lower() == "delete":
            try:
                obj = ModelName.objects.get(pk=pk)
                return obj
            except ModelName.DoesNotExist:
                return utils.Errors({"message" : "id is not appropriate."})

        else:
            utils.Errors({"message" : "Request Type is not appropriate"})

    def post(self, request):
        data = request.data
        self.file_type = data.get('audioFileType')
        metadata = data.get('audioFileMetadata')
        if not self.file_type or not metadata:
            return Response({"message" : "audioFileType or audioFileMetaData is not provided"}, status=400)
        
        serializer= self.get_serializer(request_type="post", metadata=metadata)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request, audioFileType, audioFileID=None):
        self.file_type = audioFileType
        serializer = self.get_serializer(request_type="get", pk=audioFileID)
        try:
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
        except:
            return Response(serializer.data)

    def put(self, request, audioFileType, audioFileID):
        self.file_type = audioFileType
        data = request.data
        metadata = data.get('audioFileMetadata')
        if not self.file_type or not metadata:
            return Response({"message" : "audioFileType or audioFileMetaData is not provided"}, status=400)
        
        serializer = self.get_serializer(request_type="put", pk=audioFileID, metadata=metadata)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        serializer.save()
        return Response(serializer.data)


    def delete(self, request, audioFileType, audioFileID):
        self.file_type = audioFileType
        obj = self.get_serializer(request_type="delete", pk=audioFileID)
        try:
            obj.delete()
            return Response(status=204)
        except:
            return Response(obj.errors, status=400)

