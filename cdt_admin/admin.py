from django.contrib import admin
#local imports
from cdt_admin.models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    """
        Admin class to register the candidate model
    """
    list_display = ['name','gender']
