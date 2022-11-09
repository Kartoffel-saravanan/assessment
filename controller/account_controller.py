from rest_framework.response import Response
from rest_framework import status
from utils.token_generate import token_generator
from database.models import Destination
from serializers.account_serializers import DestinationSerializers


class AccountController:

    def account_register(self, serializers, destination):
        serializers = serializers
        if serializers.is_valid(raise_exception=True):
            serializers.validated_data['app_secret_token'] = token_generator()
            if destination.is_valid(raise_exception=True):
                destination.validated_data['urls'] = 'http://127.0.0.1:8000/api/account/register/'
                destination.validated_data['http_methods'] = 'POST'
                destination.validated_data['account_id'] = serializers.validated_data['account_id']
                destination.validated_data['headers'] = {'ACC_ID': serializers.validated_data['account_id'],
                                                         'APP_SECRET': serializers.validated_data['app_secret_token'],
                                                         'ACTION': 'user.create', 'Content-Type': 'application/json',
                                                         'Accept': '*'}
                destination.save()
                serializers.save()
            response = Response(status=status.HTTP_200_OK)
            response.data = {'Message': 'Successfully register!', 'Satus': 200,
                             'token': serializers.data['app_secret_token']}
            return response
        else:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.data = {'Message': 'Invalid Data!', 'Status': 400}
            return response

    def account_update(self, serializers, destination, user):
        serializers = serializers
        if serializers.is_valid(raise_exception=True):
            account_id = serializers.validated_data.get('account_id')
            if account_id is not None:
                Destination.objects.filter(account_id=user.account_id).update(account_id=account_id)
            serializers.save()
            if destination.is_valid(raise_exception=True):
                destination.validated_data['urls'] = 'http://127.0.0.1:8000/api/account/update/'
                destination.validated_data['http_methods'] = 'PUT'
                destination.validated_data['account_id'] = user.account_id
                destination.validated_data['headers'] = {'ACC_ID': user.account_id,
                                                         'APP_SECRET': user.app_secret_token,
                                                         'ACTION': 'user.update', 'Content-Type': 'application/json',
                                                         'Accept': '*'}
                destination.save()
            response = Response(status=status.HTTP_200_OK)
            response.data = {'Message': 'Update Successfully!', 'Satus': 200}
            return response
        else:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.data = {'Message': 'Invalid Data!', 'Status': 400}
            return response

    def account_delete(self, user_account):
        if user_account:
            user_account.delete()
            Destination.objects.filter(account_id=user_account.account_id).delete()
            response = Response(status=status.HTTP_200_OK)
            response.data = {'Message': 'Delete successfully', 'Status': 200}
            return response
        else:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.data = {'Message': 'Invalid Data!', 'Status': 400}
            return response

    def account_read(self, serializers, destination):
        if serializers.is_valid(raise_exception=True):
            account_id = serializers.data['account_id']
            app_token = serializers.data['app_secret_token']
            if destination.is_valid(raise_exception=True):
                destination.validated_data['urls'] = 'http://127.0.0.1:8000/api/account/read/'
                destination.validated_data['http_methods'] = 'GET'
                destination.validated_data['account_id'] = account_id
                destination.validated_data['headers'] = {'ACC_ID': account_id,
                                                         'APP_SECRET': app_token,
                                                         'ACTION': 'user.get', 'Content-Type': 'application/json',
                                                         'Accept': '*'}
                destination.save()
            response = Response(status=status.HTTP_200_OK)
            response.data = {'Message': 'Success', 'Status': 200, 'data': serializers.data}
            return response
        else:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.data = {'Message': 'Invalid Data!', 'Status': 400}
            return response

    def destination_read_information(self, account):
        if account:
            serializers = DestinationSerializers(account, many=True)
            response = Response(status=status.HTTP_200_OK)
            response.data = {'Message': 'Success', 'Status': 200, 'data': serializers.data}
            return response
        else:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.data = {'Message': 'Invalid Data!', 'Status': 400}
            return response
