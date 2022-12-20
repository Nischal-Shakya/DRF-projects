from pblog_web.models import Id
from pblog_web.api.serializers import IdSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def id_list(request):

    if request.method == 'GET':
        identities = Id.objects.all()
        serializer = IdSerializer(identities, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = IdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def id_details(request, pk):

    if request.method == 'GET':
        try:
            identity = Id.objects.get(pk=pk)
        except Id.DoesNotExist:
            return Response({"Error": "Id not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = IdSerializer(identity)
        return Response(serializer.data)

    if request.method == 'PUT':
        identity = Id.objects.get(pk=pk)
        serializer = IdSerializer(identity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        identity = Id.objects.get(pk=pk)
        identity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
