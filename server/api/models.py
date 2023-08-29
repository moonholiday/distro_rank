from django.db import models

# Create your models here.


class LinuxDistribution(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    release_date = models.DateField()
    version = models.CharField(max_length=20)
    website = models.URLField()
    documentation = models.URLField()
    popularity_score = models.DecimalField(max_digits=5, decimal_places=2)
    overall_rank = models.PositiveIntegerField()
    performance = models.TextField()
    community_support = models.TextField()
    package_manager = models.CharField(max_length=50)
    desktop_environment = models.CharField(max_length=50)
    architectures = models.CharField(max_length=200)
    license = models.CharField(max_length=50)
    pros_and_cons = models.TextField()
    security_features = models.TextField()
    installation_method = models.TextField()
    package_repositories = models.TextField()

    def __str__(self):
        return self.name
