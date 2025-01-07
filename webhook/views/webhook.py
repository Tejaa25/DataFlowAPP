from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webhook.models import Account
import requests


class IncomingDataHandler(APIView):
    """Webhook to send the data to all the account related destinations."""

    def post(self, request):
        """Handle on POST"""

        secret_token = request.headers.get('CL-X-TOKEN')
        if not secret_token:
            return Response({"error": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        account = Account.objects.filter(app_secret_token=secret_token).first()
        if not account:
            return Response({"error": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        if not isinstance(data, dict):
            return Response({"error":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        for destination in account.related_account_destinations.all():
            if destination.http_method == 'GET':
                requests.get(destination.url, headers=destination.headers, params=data)
            elif destination.http_method in ['POST', 'PUT']:
                requests.request(destination.http_method, destination.url, headers=destination.headers, json=data)
        return Response({"message": "Data sent successfully"}, status=status.HTTP_200_OK)
