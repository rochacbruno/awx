# This file exists for backwards compatibility only
# the current way of running AWX is to point settings to
# awx/settings/__init__.py as the entry point for the settings
# that is done by exporting: export DJANGO_SETTINGS_MODULE=awx.settings
from ansible_base.lib.dynamic_config import export
from . import DYNACONF  # noqa

export(DYNACONF)
