# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['django_scim', 'django_scim.schemas']

package_data = \
{'': ['*'], 'django_scim.schemas': ['core/*', 'extension/*']}

install_requires = \
['django>=3.2', 'scim2-filter-parser>=0.5.0']

setup_kwargs = {
    'name': 'django-scim2',
    'version': '0.19.0',
    'description': 'A partial implementation of the SCIM 2.0 provider specification for use with Django.',
    'long_description': 'django-scim2\n============\n\n|tests| |coverage| |docs|\n\nThis is a provider-side implementation of the SCIM 2.0 [1]_\nspecification for use in Django.\n\nNote that currently the only supported database is Postgres.\n\n\nInstallation\n------------\n\nInstall with pip::\n\n$ pip install django-scim2\n\nThen add the ``django_scim`` app to ``INSTALLED_APPS`` in your Django\'s settings::\n\n    INSTALLED_APPS = (\n        ...\n        \'django_scim\',\n    )\n\nBy default, ``request.user.is_anonymous()`` is checked to determine if the SCIM\nrequest should be allowed or denied.\n\nIf you have specific authentication needs, look into overriding the default "is\nauthenticated predicate" (i.e. see ``GET_IS_AUTHENTICATED_PREDICATE`` for\ndetails) or subclassing the middleware that performs the check\n(``AUTH_CHECK_MIDDLEWARE``).\n\nAdd the necessary url patterns to your root urls.py file. Please note that the\nnamespace is mandatory and must be named `scim`::\n\n    urlpatterns = [\n        ...\n        path(\'scim/v2/\', include(\'django_scim.urls\')),\n    ]\n\nFinally, add settings appropriate for you app to your settings.py file::\n\n    SCIM_SERVICE_PROVIDER = {\n        \'NETLOC\': \'localhost\',\n        \'AUTHENTICATION_SCHEMES\': [\n            {\n                \'type\': \'oauth2\',\n                \'name\': \'OAuth 2\',\n                \'description\': \'Oauth 2 implemented with bearer token\',\n            },\n        ],\n    }\n\nOther SCIM settings can be provided but those listed above are required.\n\nPyPI\n----\n\nhttps://pypi.python.org/pypi/django-scim2\n\nSource\n------\n\nhttps://github.com/15five/django-scim2\n\nDocumentation\n-------------\n\n.. |docs| image:: https://readthedocs.org/projects/django-scim2/badge/\n  :target: https://django-scim2.readthedocs.io/\n  :alt: Documentation Status\n\nhttps://django-scim2.readthedocs.io/\n\nDevelopment\n-----------\n\nThis project uses Poetry to manage dependencies, etc. Thus to install the\nnecessary tools when developing, run:\n\n```\npoetry install\n```\n\nTests\n-----\n\n.. |tests| image:: https://github.com/15five/django-scim2/workflows/CI%2FCD/badge.svg\n    :target: https://github.com/15five/django-scim2/actions\n\nhttps://github.com/15five/django-scim2/actions\n\nTests are typically run locally with `tox` (https://tox.wiki/). Tox will test\nall supported versions of Python and Django.\n\n```\ntox\n```\n\nTo run the test suite with a single version of Python (the version you created\nthe virtualenv with), run:\n\n\n```\npoetry run pytest tests/\n```\n\n\nCoverage\n--------\n\n.. |coverage| image:: https://codecov.io/gh/15five/django-scim2/graph/badge.svg\n    :target: https://codecov.io/gh/15five/django-scim2\n\nhttps://codecov.io/gh/15five/django-scim2/\n\n```\ntox -e coverage\n```\n\nLicense\n-------\n\nThis library is released under the terms of the **MIT license**. Full details in ``LICENSE.txt`` file.\n\n\nExtensibility\n-------------\n\nThis library was forked and developed to be highly extensible. A number of\nadapters can be defined to control what different endpoints do to your resources.\nPlease see the documentation for more details.\n\nPLEASE NOTE: This app does not implement authorization and authentication.\nSuch tasks are left for other apps such as `Django OAuth Toolkit`_ to implement.\n\n.. _`Django OAuth Toolkit`: https://github.com/evonove/django-oauth-toolkit\n\nDevelopment Speed\n-----------------\n\nSince this project is relatively stable, time is only dedicated to it on\nFridays. Thus if you issue a PR, bug, etc, please note that it may take a week\nbefore we get back to you. Thanks you for your patience.\n\nCredits\n-------\n\nThis project was forked from https://bitbucket.org/atlassian/django_scim\n\n\n.. [1] http://www.simplecloud.info/, https://tools.ietf.org/html/rfc7644\n',
    'author': 'Paul Logston',
    'author_email': 'paul@15five.com',
    'maintainer': 'Devs',
    'maintainer_email': 'devs@15five.com',
    'url': 'https://pypi.org/project/django-scim2/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
