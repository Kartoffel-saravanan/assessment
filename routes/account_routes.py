from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from services.account_services import AccountRegister, AccountUpdate, AccountDelete, AccountRead, DestinationInformation

urlpatterns = [
    path('register/', AccountRegister.as_view()),
    path('update/', AccountUpdate.as_view()),
    path('delete/', AccountDelete.as_view()),
    path('read/', AccountRead.as_view()),
    path('destination/information/', DestinationInformation.as_view()),
]

url = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
