"""The main settings module used to configure an application
through the ``UNIMATRIX_SETTINGS_MODULE`` environment variable.
"""
from unimatrix.runtime.settings import for_environment


for_environment(__package__, defaults='defaults')