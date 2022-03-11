
from django_filters import rest_framework as filters, IsoDateTimeFilter
from .models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TODOFilter(filters.FilterSet):
    date_create = filters.DateFromToRangeFilter()

    class Meta:
        model = ToDo
        fields = ['initial_project', 'date_create']