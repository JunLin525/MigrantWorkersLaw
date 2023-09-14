from django.db import models
from datetime import date
# Create your models here.
class NewPolicy(models.Model):
    MinisterOfLabor = "MOL"
    ImmigrationBureau= "IMB"
    DepartmentOfHealth="DOH"
    MinisterOfForeignerAffairs="MFA"
    DepartmentOfAgriculture="DOA"
    Government_Bureau=[
        (MinisterOfLabor, "MinisterOfLabor"),
        (ImmigrationBureau, "ImmigrationBureau"),
        (DepartmentOfHealth, "DepartmentOfHealth"),
        (MinisterOfForeignerAffairs,"MinisterOfForeignerAffairs"),
        (DepartmentOfAgriculture,"DepartmentOfAgriculture"),
    ]
    Title = models.CharField(max_length=150)
    IssueBureau = models.CharField(max_length=3, choices=Government_Bureau, default=MinisterOfLabor,)
    IssueDate= models.DateField(default=date.today)
    Text = models.TextField()
    image = models.FileField(upload_to="NewPolicy/")