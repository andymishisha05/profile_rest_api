from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.core import serializers as ser
from rest_framework import status, viewsets
from rest_framework import filters
from django.core.paginator import Paginator
from django.http import JsonResponse

from profile_api import serializers, models,permissions




class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields = ('name','email')



class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES





class UserProfileAPIView(APIView):

    serializer_class = serializers.UserProfileSerializer

    def get(self, request, format=None):
        
        queryset = models.UserProfile.objects.all()
        serializer = serializers.UserProfileSerializer(queryset,many=True)

        return Response({"list":serializer.data})
       

    def post(self,request):
        serializer = serializers.UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your logic',
        'Is mapped manually to URLs',
    ]

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        return Response({'message': 'Hello!', 'an_apiview': self.an_apiview})

    def get(self, request, pk=None):

        return Response({'message': 'Hello!'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            self.an_apiview.append("new Item")
            return Response({'message': message, 'an_apiview': self.an_apiview})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'list': a_viewset})

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'hello ' + name
            return Response({'message', message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({"message", "get"})

    def update(self, request, pk=None):
        return Response({"message", "put"})

    def partial_update(self, request, pk=None):
        return Response({'message', 'update'})

    def destroy(self, request, pk=None):
        return Response({'message', 'Delete'})


def index(request):
    queryset = models.UserProfile.objects.all()
    serializer = serializers.UserProfileSerializer(queryset,many=True)

    return JsonResponse({"array_to_js":serializer.data}, safe=False)

