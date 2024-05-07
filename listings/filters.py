import django_filters
from listings import models

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = models.Listings
        fields = ['condition', 'city', 'state']