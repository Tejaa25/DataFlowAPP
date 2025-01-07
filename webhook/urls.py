from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import IncomingDataHandler, AccountCUDModelApiViewSet, DestinationModelApiViewSet

API_URL_PREFIX = "api/v1/"

router = SimpleRouter()

router.register(f"{API_URL_PREFIX}accounts", AccountCUDModelApiViewSet),
router.register(f"{API_URL_PREFIX}destinations", DestinationModelApiViewSet),

urlpatterns = [
    path(f'{API_URL_PREFIX}server/incoming_data/', IncomingDataHandler.as_view()),
] + router.urls
