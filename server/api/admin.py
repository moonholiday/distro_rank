from django.contrib import admin
from .models import LinuxDistribution


class LinuxDistributionAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'overall_rank', 'popularity_score')
    list_filter = ('desktop_environment', 'architectures', 'license')
    search_fields = ('name', 'description')


admin.site.register(LinuxDistribution, LinuxDistributionAdmin)
