from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Account, Product, RequestForm
from .serializers import AccountSerializer, ProductSerializer, RegisterSerializer, UserSerializer, AccountDTOSerializer, RequestFormSerializer
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


@api_view(['GET'])
def getRequestForm(request):
    res = RequestForm.objects.all()
    serializer = RequestFormSerializer(res, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.save())
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def edit_product(request, id):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = Product.objects.get(id=id)
        product = serializer.data
        product.save()
    return Response(serializer.data)


@api_view(['POST'])
def delete_product(request, id):
    product = Product.objects.get(id=id)
    if product:
        product.delete()
    return Response({'data': "Xoa thanh cong", 'product': product})


@api_view(['POST'])
def add_account(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
    return Response({'user': serializer.data, 'token': AuthToken.objects.create(user)[1]})


@api_view(['POST'])
def update_account(request, id):
    serializer = AccountSerializer(data=request.data)
    faccount = Account.objects.get(id=id)
    faccount = serializer.data
    if serializer.is_valid():
        faccount.save()
    return Response(serializer.data)


@api_view(['POST'])
def delete_account(request, id):
    account = Account.objects.get(id=id)
    if account:
        account.delete()
    return Response({'data': "Xoa thanh cong", 'account': account})


@api_view(['POST'])
def addrequest(request):  # gửi yêu cầu
    serializer = RequestFormSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.save())
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def change_state(request, id):  # set lại trạng thái duyệt hay chưa
    req = RequestForm.objects.get(id=id)
    req.status == False if req.status == True else req.status == False
    req.save()
    return Response("Thanh cong")


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
