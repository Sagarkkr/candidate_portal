from django.db.models import Q
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#local imports
from cdt_admin.models import Candidate
from cdt_admin.serializers import CandidateSerializers

class CandidateViewset(viewsets.GenericViewSet,
                       mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin):
    """
        Candidate viewset to handle create,list,retrieve and update requests
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializers
    permission_classes = [IsAuthenticated]

    @action(methods=['GET'],detail=False)
    def get_matching_name(self,request):
        """
            Method to get matching name of candidate
        """
        name_search = request.query_params.get("name").strip().lower().split()
        query = Q()
        for i in name_search:
            query |= Q(name__icontains=i)
        result = Candidate.objects.filter(query).values_list('name',flat=True)
        return Response(result, status=status.HTTP_200_OK)
        