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

from django.apps import apps
from django.contrib import admin
from django.forms.widgets import MediaDefiningClass


def get_admin_models():
    """Get all the ModelAdmin in every loaded application"""
    admin_models = {}
    for application in apps.app_configs.keys():
        application_module = apps.app_configs[application]
        application_module.import_models()
        for module_name in dir(application_module.models_module):
            obj = getattr(application_module.models_module, module_name)
            if (issubclass(obj.__class__, MediaDefiningClass) and
                    issubclass(obj, admin.options.BaseModelAdmin) and
                    # Avoid to list the BaseModelAdmin class
                    obj.__class__ is not admin.options.BaseModelAdmin):
                admin_models[obj.__name__] = obj
    return admin_models
