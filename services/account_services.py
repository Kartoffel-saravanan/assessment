from rest_framework.views import APIView
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from serializers.account_serializers import RegisterSerializers, DestinationSerializers, UpdateSerializers
from controller.account_controller import AccountController
from database.models import Account, Destination
from rest_framework.exceptions import AuthenticationFailed


class AccountRegister(APIView):

    def post(self, request, format=None, *args, **kwargs):
        serializers = RegisterSerializers(data=request.data)
        destination = DestinationSerializers(data=request.data)
        register = AccountController.account_register(request, serializers, destination)
        if register:
            return register
        else:
            raise Http404


class AccountUpdate(APIView):

    def get_object(self, request):
        bearer = request.headers.get('CL-X-TOKEN')
        try:
            return Account.objects.get(app_secret_token=bearer)
        except ObjectDoesNotExist:
            raise AuthenticationFailed('Un Authenticated!')

    def put(self, request, format=None, *args, **kwargs):
        user = self.get_object(request)
        serializers = UpdateSerializers(user, data=request.data)
        destination = DestinationSerializers(data=request.data)
        update = AccountController.account_update(request, serializers, destination, user)
        if update:
            return update
        else:
            raise Http404


class AccountDelete(APIView):

    def get_object(self, request):
        bearer = request.headers.get('CL-X-TOKEN')
        try:
            return Account.objects.get(app_secret_token=bearer)
        except ObjectDoesNotExist:
            raise AuthenticationFailed('Un Authenticated!')

    def post(self, request, format=None, *args, **kwargs):
        user_account = self.get_object(request)
        delete = AccountController.account_delete(request, user_account)
        if delete:
            return delete
        else:
            raise Http404


class AccountRead(APIView):

    def get_object(self, request):
        bearer = request.headers.get('CL-X-TOKEN')
        try:
            return Account.objects.get(app_secret_token=bearer)
        except ObjectDoesNotExist:
            raise AuthenticationFailed('Un Authenticated!')

    def get(self, request, format=None, *args, **kwargs):
        user_account = self.get_object(request)
        serializers = RegisterSerializers(user_account, data=request.data)
        destination = DestinationSerializers(data=request.data)
        read = AccountController.account_read(request, serializers, destination)
        if read:
            return read
        else:
            raise Http404


class DestinationInformation(APIView):

    def get(self, request, format=None, *args, **kwargs):
        user_account = request.data['account_id']
        account = Destination.objects.filter(account_id=user_account)
        read = AccountController.destination_read_information(request, account)
        if read:
            return read
        else:
            raise Http404
