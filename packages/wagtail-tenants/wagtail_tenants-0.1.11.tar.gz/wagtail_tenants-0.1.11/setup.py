# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wagtail_tenants',
 'wagtail_tenants.customers',
 'wagtail_tenants.customers.migrations',
 'wagtail_tenants.db',
 'wagtail_tenants.management',
 'wagtail_tenants.management.commands',
 'wagtail_tenants.middleware',
 'wagtail_tenants.migrations',
 'wagtail_tenants.users',
 'wagtail_tenants.users.migrations',
 'wagtail_tenants.users.views']

package_data = \
{'': ['*'],
 'wagtail_tenants': ['templates/wagtail_tenants/admin/*',
                     'templates/wagtailadmin/home/*',
                     'templates/wagtailusers/groups/*',
                     'templates/wagtailusers/groups/includes/*',
                     'templates/wagtailusers/users/*']}

install_requires = \
['django-dbbackup>=3.3.0,<4.0.0', 'django-tenants>=3.3.4,<4.0.0']

setup_kwargs = {
    'name': 'wagtail-tenants',
    'version': '0.1.11',
    'description': 'Adds multitenancy based on django_tenants to wagtail cms',
    'long_description': '# wagtail-tenants\n\n[![Documentation Status](https://readthedocs.org/projects/wagtail-tenants/badge/?version=latest)](https://wagtail-tenants.readthedocs.io/en/latest/?badge=latest)\n[![Testing the wagtail tenants with postgres](https://github.com/borisbrue/wagtail-tenants/actions/workflows/integrationtest.yml/badge.svg)](https://github.com/borisbrue/wagtail-tenants/actions/workflows/integrationtest.yml)\n\nwagtail_tenants is a Django/Wagtail app to provide multitenancy to your wagtail project.\nYou are able to run a main Wagtail Site and from within you are able to host as many Wagtailsites as you want. \ndjango_tenants is used to slice the database layer in a postgres database based on a given schema.\n\nDetailed documentation will be in the "docs" directory. \n\n## Quick start\n\n### Installation\n\n```bash\npip install wagtail-tenants\n```\n\n### Configuration\n\n1. Add "wagtail_tenants" to your INSTALLED_APPS setting like this:\n\n    ```python\n    SHARED_APPS = (\n        \'wagtail_tenants.customers\',\n        \'wagtail_tenants\',\n        \'wagtail.contrib.forms\',\n        ...\n        "wagtail_tenants.users",\n        "wagtail.users",\n        ...\n    )\n\n    TENANT_APPS = (\n        \'wagtail_tenants\',\n        "django.contrib.contenttypes",\n        ...\n        # rest of the wagtail apps\n        ...\n        "wagtail_tenants.users",\n        "wagtail.users",\n        ...\n    )\n\n    INSTALLED_APPS = list(SHARED_APPS) + [\n        app for app in TENANT_APPS if app not in SHARED_APPS\n    ]\n    ```\n\n2. Include the the tenants middleware at the beginning of your middlewares:\n\n    ```python\n    MIDDLEWARE = [\n    "wagtail_tenants.middleware.main.WagtailTenantMainMiddleware",\n    ...\n    ]\n    ```\n\n3. Define the Tenant model Constants (and also set the default auto field if not already done):\n\n    ```python\n    AUTH_USER_MODEL = \'wagtail_tenants.User\' \n    TENANT_MODEL = "customers.Client" \n    TENANT_DOMAIN_MODEL = "customers.Domain"\n    DEFAULT_AUTO_FIELD=\'django.db.models.AutoField\'\n    ```\n\n4. Set the Database backend to the **django_tenants** backend:\n\n    ```python\n    DATABASES = {\n        "default": {\n            "ENGINE": "django_tenants.postgresql_backend",\n            "NAME": "db_name",\n            "USER": "db_user",\n            "PASSWORD": "",\n            "HOST": "127.0.0.1",\n            "PORT": "5432",\n        }\n    }\n    ```\n\n5. Set the Database Router to work with the tenants:\n\n    ```python\n    DATABASE_ROUTERS = ("wagtail_tenants.routers.WagtailTenantSyncRouter",)\n    ```\n\n6. Set the authentication backend to fit to our Tenant model.\n\n    ```python\n    AUTHENTICATION_BACKENDS = [\n        \'wagtail_tenants.backends.TenantBackend\',\n    ]\n    ```\n\n7. Run the migrations with `./manage.py migrate_schemas --shared`\n8. Create a public schema with `./manage.py create_tenant` and use `public` as the schema name and `localhost`\n9. Create a superuser for the public tenant `./manage.py create_tenant_superuser`\n10. Start the Server and have fun\n11. You are able to create tenants within the admin of your public wagtailsite. If you want to log into a tenant you need at least one superuser for the tenant. You can use `./manage.py create_tenant_superuser` for that.\n\n\n### Update 0.1.10\n\nThe new version of wagtail_tenants is now able to archive the follwing features:\n\n#### wagtail 4.2. support\n\nAs the developemt of wagtail still goes on, so we do. Wagtail incuded a reference index for models it was necessary to handle this feature, as we don \'t need this feature on our tenant models.\n\n#### Create tenantaware apps\n\nOnly users of a given tenant are able to interact within the wagtail admin with that kind of app.\nThis works in two ways:\n\n1. Add a tenantaware property to the apps AppConfig class in `yourtenantapp.apps.py` \nin the `admin.py` create a ModelAdmin or ModelAdminGroup for your app and use the `menu_item_name` property to fit to your apps name from your AppConfig. If this fits the app will be hidden for all tenants withou a TenantFeaure of the same name. This feature is good for providing different tiers of your app (eg. free | premium )\n\n2. You can specify the tenant directly within the AppConfig so that only users of the tenant have access to this app. This is necessary if you want to create complete and complex functionality only for one tenant. To archive this you have to add the `WagtailTenantPermissionMiddleware`to your middlewares in your settings like so: \n\n```python\nMIDDLEWARE = [\n    "wagtail_tenants.middleware.main.WagtailTenantMainMiddleware",\n    "wagtail_tenants.middleware.main.WagtailTenantPermissionMiddleware",\n    "..."\n]\n```\n\n#### Exclude permissions from normal users in the group create and group edit view\n\nWe are able to hide apps from the group create and group edit views in the wagtail admin. With this approach it is possible to create a tenant admin group with all permissions and distribute it to a tenant user. The tenant admin is able to create and edit groups, but you can decide which apps should be excluded from the view. By default this should include all customers apps. But feel free to extend the list.\n\n```python\nTENANT_EXCLUDE_MODEL_PERMISSIONS = [\n    "customers.Client",\n    "customers.ClientFeature",\n    "customers.Domain",\n    "customers.ClientBackup",\n]\n```',
    'author': 'Boris Brue',
    'author_email': 'boris@zuckersalzundpfeffer.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://wagtail-tenants.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
