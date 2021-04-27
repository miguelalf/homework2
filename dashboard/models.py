from django.db import models

class Person(models.Model) :
    ROLE_LIST = [
        (1, 'Tech Coach'),
        (2, 'Academic Coach'),
        (3, 'Talent Placement Coach'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=30, null=True)
    location = models.CharField(max_length=100, null=True)
    role = models.IntegerField(choices=ROLE_LIST)
    deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, null=True)
