##
#     Project: Django Admin Settings
# Description: A Django application to configure some Django Admin settings
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2023 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

from django.contrib import admin


class AdminTextInputFilter(admin.SimpleListFilter):
    template = 'django_admin_settings/text_input_filter/form.html'
    parameter_name = None
    lookup_condition = None
    lookup_condition_advanced = None

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ('', ''),

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

    def queryset(self, request, queryset):
        if self.value() is not None:
            # Apply filter condition
            if self.lookup_condition_advanced:
                # Use advanced lookup condition
                condition = self.lookup_condition_advanced
            elif self.lookup_condition:
                # Use parameter name with lookup condition only
                condition = f'{self.parameter_name}__{self.lookup_condition}'
            else:
                # Use parameter name only
                condition = self.parameter_name
            return queryset.filter(**{condition: self.value()})
