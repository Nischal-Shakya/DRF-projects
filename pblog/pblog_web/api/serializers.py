from rest_framework import serializers
from pblog_web.models import Id


class IdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Id
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")


# class IdSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     age = serializers.CharField()
#     lookingForJob = serializers.BooleanField()

#     def create(self, validated_data):
#         return Id.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.age = validated_data.get('age')
#         instance.lookingForJob = validated_data.get('lookingForJob')
#         instance.save()
#         return instance
