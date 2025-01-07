from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webhook.config import HttpMethodChoices
from webhook.models import Account
from requests import request
import json


class IncomingDataHandler(APIView):
    """Webhook to send the data to all the account related destinations."""

    @staticmethod
    def make_http_request(
        url: str, method="GET", headers={}, data={}, params={}
    ):
        """
        Function that makes a http request to any given url based on the passed params/data.
        This is defined here just to make things DRY.
        """

        request(
            method=method,
            url=url,
            headers=headers,
            data=json.dumps(data),
            params=params,
        )

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
            if destination.http_method == HttpMethodChoices.GET:
                self.make_http_request(destination.url, headers=destination.headers, params=data)
            elif destination.http_method in [HttpMethodChoices.POST, HttpMethodChoices.PUT]:
                self.make_http_request(destination.url, method=destination.http_method,  headers=destination.headers, data=data)
        return Response({"message": "Data sent successfully"}, status=status.HTTP_200_OK)
