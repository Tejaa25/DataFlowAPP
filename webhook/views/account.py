from rest_framework.viewsets import ModelViewSet
from webhook.models import Account
from webhook.serializers import AccountSerializer

# class AccountView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             account = get_object_or_404(Account, pk=pk)
#             serializer = AccountSerializer(account)
#         else:
#             accounts = Account.objects.all()
#             serializer = AccountSerializer(accounts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = AccountSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def put(self, request, pk):
#         account = get_object_or_404(Account, pk=pk)
#         serializer = AccountSerializer(account, data=request.data, partial=False)  # Full update
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request, pk):
#         account = get_object_or_404(Account, pk=pk)
#         account.delete()
#         return Response({"message": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class AccountCUDModelApiViewSet(ModelViewSet):
    """Api viewset for Account model"""

    serializer_class = AccountSerializer
    queryset = Account.objects.all()