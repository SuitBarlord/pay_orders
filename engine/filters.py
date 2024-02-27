import django_filters
from .models import Reestr_oferts


class ProductFilter(django_filters.FilterSet, django_filters.RangeFilter):
    date_buhgt = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
                attrs={'type': 'date'}))
    # date_buhgt = django_filters.DateFromToRangeFilter()
    # th_month = django_filters.ChoiceFilter()
    # date_buhgt = django_filters.DateTimeFilter(lookup_expr='gte', label='Date')
    class Meta:
        model = Reestr_oferts
        fields = ['exicutor', 'filial']