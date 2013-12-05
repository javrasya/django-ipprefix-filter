import copy
from django.utils.http import urlencode

_s_author__ = 'ahmetdal'

from django import forms
from django.contrib import admin
from django.db import models, connection
from django.forms import TextInput, Select
from django.utils.translation import ugettext as _


class IpMaskForm(forms.Form):
    def __init__(self, model=None, *args, **kwargs):
        self.field_name = kwargs.pop('field_name')

        self.model = model
        super(IpMaskForm, self).__init__(*args, **kwargs)

        self.fields['%s__istartswith' % self.field_name] = forms.CharField(
            label='', widget=TextInput(
                attrs={'class': 'vIpField', 'placeholder': _('Ip')}), localize=True,
            required=False)
        table_name = self.model._meta.db_table

        c = connection.cursor()

        c.execute("""
        select
            DISTINCT(substring(CAST(i.%s as text) from position('/' in CAST(i.%s as text)))) as mask
            from %s i
            order by mask;
        """ % (self.field_name, self.field_name, table_name))
        self.choices = [(c, c) for (c,) in c.fetchall()]
        self.choices.insert(0, ('', _('All')))
        self.fields['%s__iendswith' % self.field_name] = forms.ChoiceField(label='', choices=self.choices, localize=True, required=False,
                                                                           widget=Select(attrs={'class': 'vIpField'}))


    def as_one_div(self):
        return self._html_output(
            normal_row='%(field)s%(help_text)s',
            error_row='%s',
            row_ender='',
            help_text_html=' s',
            errors_on_separate_row=True)


class IpMaskFilter(admin.filters.FieldListFilter):
    template = 'ip_mask_filter/filter.html'


    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg_istartswith = '%s__istartswith' % field_path
        self.lookup_kwarg_iendswith = '%s__iendswith' % field_path
        self.model = model
        super(IpMaskFilter, self).__init__(
            field, request, params, model, model_admin, field_path)
        self.form = self.get_form(request)

    def choices(self, cl):
        return []

    def expected_parameters(self):
        return [self.lookup_kwarg_istartswith, self.lookup_kwarg_iendswith]

    def get_form(self, request):
        return IpMaskForm(model=self.model, data=self.used_parameters, field_name=self.field_path)

    def queryset(self, request, queryset):
        if self.form.is_valid():
            filter_params = dict(filter(lambda x: bool(x[1]),
                                        self.form.cleaned_data.items()))

            return queryset.filter(**filter_params)
        else:
            return queryset


# register the filter
admin.filters.FieldListFilter.register(
    lambda f: isinstance(f, models.CharField), IpMaskFilter)
