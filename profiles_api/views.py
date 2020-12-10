from rest_framework.views import APIView
from rest_framework.response import Response
# to response status .. 200, 400, 500..  
from rest_framework import status
# allows serializer objects model
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]        

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        # self... it comes on django and retrieve the serializer class
        # (...) it's the data from the request and assign the values to the parameter data
        serializer = self.serializer_class(data=request.data)
        # if the input is valid
        if serializer.is_valid():
            # retrieve data name from serializer file
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        # if the input is not valid
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)