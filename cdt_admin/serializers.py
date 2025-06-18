from rest_framework import serializers
from cdt_admin.models import Candidate

class CandidateSerializers(serializers.ModelSerializer):
    """
        Model serializer of candidate model to serialize and validate candidate instances
    """
    class Meta:
        model = Candidate
        fields = '__all__'