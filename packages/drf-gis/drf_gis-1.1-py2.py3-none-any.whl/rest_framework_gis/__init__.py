VERSION = (1, 0, 0, 'final')
__version__ = VERSION  # alias


def get_version():
    version = f'{VERSION[0]}.{VERSION[1]}'
    if VERSION[2]:
        version = f'{version}.{VERSION[2]}'
    if VERSION[3:] == ('alpha', 0):
        version = f'{version} pre-alpha'
    elif VERSION[3] != 'final':
        version = f'{version} {VERSION[3]}'
    return version


try:
    import django

    if django.VERSION < (3, 2):
        default_app_config = 'rest_framework_gis.apps.AppConfig'
except ImportError:
    pass
