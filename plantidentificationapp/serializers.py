from rest_framework import serializers

# Although we are not using models as we have no database,
# serializers are still useful for data validation and transformation
class SerializerAPI1(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    value = serializers.IntegerField()

class SerializerAPI2(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    value = serializers.IntegerField()
 
