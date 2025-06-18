from rest_framework.routers import DefaultRouter
#local import
from cdt_admin.views import CandidateViewset

cdt_router = DefaultRouter()
cdt_router.register('candidate', CandidateViewset, basename='candidate')

urlpatterns = []
urlpatterns = cdt_router.urls + urlpatterns