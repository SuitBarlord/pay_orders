import django_filters
from .models import Reestr_oferts, Filials, Exicuters
from django import forms


class ProductFilter(django_filters.FilterSet, django_filters.RangeFilter):
    exicutor = django_filters.ModelMultipleChoiceFilter(
        field_name='exicutor',
        queryset=Exicuters.objects.none(),
        widget=forms.CheckboxSelectMultiple
    )
    def __init__(self, *args, **kwargs):
        id = kwargs.pop('id', None)
        super().__init__(*args, **kwargs)
        # Теперь мы можем использовать значение id
        if id is not None:
            self.filters['exicutor'].queryset = Exicuters.objects.filter(filial_id=id)
    date_buhgt = django_filters.DateFromToRangeFilter(label='Диапозон дат передачи в бухгалтерию', widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    date_orders = django_filters.DateFromToRangeFilter(label='Диапозон дат договора', widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    # date_buhgt = django_filters.DateFromToRangeFilter()
    # th_month = django_filters.ChoiceFilter()
    # date_buhgt = django_filters.DateTimeFilter(lookup_expr='gte', label='Date')
    class Meta:
        model = Reestr_oferts
        fields = ['exicutor']