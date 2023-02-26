"""This file contains routes for SelectionView"""
from rest_framework import routers
from selections.views import SelectionView
# -------------------------------------------------------------------------

router = routers.SimpleRouter()
router.register('', SelectionView)

urlpatterns = router.urls
