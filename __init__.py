default_app_config = "company.apps.CompanyConfig"

from django.apps import apps as django_apps
from django.utils.module_loading import import_string

from company.apps import CompanyConfig as conf


def get_company_model(address_or_country="Company"):
    return django_apps.get_model(conf.app_label, getattr(conf.Model, address_or_country).lower())


def create_entity(country, input_obj, user=None):
    return import_string(f"company.backends.create.{country}.create")(input_obj, user=user)
