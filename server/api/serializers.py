from rest_framework import serializers
from .models import LinuxDistribution


class LinuxDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinuxDistribution
        fields = ('id', 'name', 'description', 'logo', 'release_date', 'version', 'website', 'documentation', 'popularity_score', 'overall_rank', 'performance', 'community_support',
                  'package_manager', 'desktop_environment', 'architectures', 'license', 'pros_and_cons', 'security_features', 'installation_method', 'package_repositories')

