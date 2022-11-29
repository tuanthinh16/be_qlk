from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Account, Product
from .serializers import AccountSerializer, ProductSerializer, RegisterSerializer, UserSerializer, AccountDTOSerializer
from rest_framework import generics, permissions
from knox.models import AuthToken
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer


@api_view(['GET'])
def getaccount(request):
    account = Account.objects.all()
    serializer = AccountSerializer(account, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getproduct(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addproduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.save())
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def addaccount(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
    return Response({'user': serializer.data, 'token': AuthToken.objects.create(user)[1]})


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        serializers = AccountDTOSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
