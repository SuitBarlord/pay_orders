import django_filters
from .models import Reestr_oferts


class ProductFilter(django_filters.FilterSet):
    date_buhgt = django_filters.DateFromToRangeFilter()
    class Meta:
        model = Reestr_oferts
        fields = ['exicutor', 'filial', 'date_buhgt']