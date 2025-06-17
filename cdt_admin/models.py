from django.db import models

class BaseModel(models.Model):
    """
        Data model to save common data used in models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    """Data created date and time."""

    modified_at = models.DateTimeField(auto_now=True)
    """Data update date and time."""

    class Meta:
        abstract = True

class CandidateGenderChoices(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHERS = "OTHERS"

class Candidate(BaseModel):
    """
        Candidate model to store details of a candidate
    """
    name = models.CharField(max_length=250)
    """Name of the candidate"""

    age = models.PositiveIntegerField()
    """Age of the candidate"""

    gender = models.CharField(max_length=50, choices=CandidateGenderChoices.choices)
    """Gender of the candidate"""

    email = models.EmailField(unique=True,blank=True,null=True)
    """Email of the candidate"""

    phone_number = models.CharField(max_length=15,unique=True)
    """Phone number of the candidate"""

    def __str__(self):
        return self.name
