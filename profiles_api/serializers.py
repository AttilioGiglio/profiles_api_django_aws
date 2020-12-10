from rest_framework import serializers

# Allows convert data inputs into python objects. They are very similar to django forms, which defines the inputs of data.
class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    