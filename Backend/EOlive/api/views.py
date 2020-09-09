from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from EOlive.models import User, evidencijagospodarstva, berba, podaci_radnje, prihranjivanje, spricanje 
from .serializers import userSerializer, evidencijagospodarstvaSerializer, berbaSerializer, podaci_radnjeSerializer, prihranjivanjeSerializer, spricanjeSerializer



def get_queryset(self):
    user = self.request.User
    return user.accounts.all()


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def userListView(request, format=None):

    if request.method == 'GET':
        user = User.objects.all()
        serializer = userSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def userDetailView(request, pk, format=None):
    try:
        user = User.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = userSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = userSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes((permissions.AllowAny,))
class evidencijagospodarstvaListView(ListAPIView):
    queryset = evidencijagospodarstva.objects.all()
    serializer_class=evidencijagospodarstvaSerializer

@permission_classes((permissions.IsAuthenticated,))
class berbaListView(ListAPIView):
    queryset = berba.objects.all()
    serializer_class=berbaSerializer

@permission_classes((permissions.IsAuthenticated,))
class podaci_radnjeListView(ListAPIView):
    queryset = podaci_radnje.objects.all()
    serializer_class=podaci_radnjeSerializer

@permission_classes((permissions.IsAuthenticated,))
class prihranjivanjeListView(ListAPIView):
    queryset = prihranjivanje.objects.all()
    serializer_class=prihranjivanjeSerializer

@permission_classes((permissions.IsAuthenticated,))
class spricanjeListView(ListAPIView):
    queryset = spricanje.objects.all()
    serializer_class=spricanjeSerializer


@permission_classes((permissions.IsAuthenticated,))
class userDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class=userSerializer

@permission_classes((permissions.AllowAny,))
class evidencijagospodarstvaDetailView(RetrieveAPIView):
    queryset = evidencijagospodarstva.objects.all()
    serializer_class=evidencijagospodarstvaSerializer

@permission_classes((permissions.IsAuthenticated,))
class berbaDetailView(RetrieveAPIView):
    queryset = berba.objects.all()
    serializer_class=berbaSerializer

@permission_classes((permissions.IsAuthenticated,))
class podaci_radnjeDetailView(RetrieveAPIView):
    queryset = podaci_radnje.objects.all()
    serializer_class=podaci_radnjeSerializer

@permission_classes((permissions.IsAuthenticated,))
class prihranjivanjeDetailView(RetrieveAPIView):
    queryset = prihranjivanje.objects.all()
    serializer_class=prihranjivanjeSerializer
    

@permission_classes((permissions.IsAuthenticated,))
class spricanjeDetailView(RetrieveAPIView):
    queryset = spricanje.objects.all()
    serializer_class=spricanjeSerializer

@permission_classes((permissions.IsAuthenticated,))
class evidencijagospodarstvaCreateView(CreateAPIView):
    queryset = evidencijagospodarstva.objects.all()
    serializer_class = evidencijagospodarstvaSerializer
    
@permission_classes((permissions.IsAuthenticated,))
class berbaCreateView(CreateAPIView):
    queryset = berba.objects.all()
    serializer_class=berbaSerializer

@permission_classes((permissions.IsAuthenticated,))
class podaci_radnjeCreateView(CreateAPIView):
    queryset = podaci_radnje.objects.all()
    serializer_class=podaci_radnjeSerializer

@permission_classes((permissions.IsAuthenticated,))
class prihranjivanjeCreateView(CreateAPIView):
    queryset = prihranjivanje.objects.all()
    serializer_class=prihranjivanjeSerializer

@permission_classes((permissions.IsAuthenticated,))
class spricanjeCreateView(CreateAPIView):
    queryset = spricanje.objects.all()
    serializer_class=spricanjeSerializer

@permission_classes((permissions.IsAuthenticated,))
class evidencijagospodarstvaDeleteView(DestroyAPIView):
    queryset = evidencijagospodarstva.objects.all()
    serializer_class=evidencijagospodarstvaSerializer

@permission_classes((permissions.IsAuthenticated,))
class berbaDeleteView(DestroyAPIView):
    queryset = berba.objects.all()
    serializer_class=berbaSerializer
    
@permission_classes((permissions.IsAuthenticated,))
class podaci_radnjeDeleteView(DestroyAPIView):
    queryset = podaci_radnje.objects.all()
    serializer_class=podaci_radnjeSerializer
    
@permission_classes((permissions.IsAuthenticated,))
class prihranjivanjeDeleteView(DestroyAPIView):
    queryset = prihranjivanje.objects.all()
    serializer_class=prihranjivanjeSerializer
    
@permission_classes((permissions.IsAuthenticated,))
class spricanjeDeleteView(DestroyAPIView):
    queryset = spricanje.objects.all()
    serializer_class=spricanjeSerializer
    permission_classes = (permissions.IsAuthenticated, )

@permission_classes((permissions.IsAuthenticated,))
class evidencijagospodarstvaUpdateView(UpdateAPIView):
    queryset = evidencijagospodarstva.objects.all()
    serializer_class=evidencijagospodarstvaSerializer
    
@permission_classes((permissions.IsAuthenticated,))
class berbaUpdateView(UpdateAPIView):
    queryset = berba.objects.all()
    serializer_class=berbaSerializer
    
@permission_classes((permissions.IsAuthenticated,))
class podaci_radnjeUpdateView(UpdateAPIView):
    queryset = podaci_radnje.objects.all()
    serializer_class=podaci_radnjeSerializer

@permission_classes((permissions.IsAuthenticated,))
class prihranjivanjeUpdateView(UpdateAPIView):
    queryset = prihranjivanje.objects.all()
    serializer_class=prihranjivanjeSerializer

@permission_classes((permissions.IsAuthenticated,))
class spricanjeUpdateView(UpdateAPIView):
    queryset = spricanje.objects.all()
    serializer_class=spricanjeSerializer
