"""This unit contains urls for LocationViewSet CBV"""
from rest_framework import routers
from locations.views import LocationViewSet
# ------------------------------------------------------------------------

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = router.urls
