# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""Defaults settings for FastAPI projects."""
import os
from typing import Any

from .ioc import DEFAULT_DEPENDENCIES

# Unimatrix-compliant Python packages.
INSTALLED_APPS = []


#: The OpenAPI URL exposed by the application.
OPENAPI_URL = "/openapi.json"

#: The URL at which the API browser is exposed.
DOCS_URL = "/ui"

APP_ISSUER: str = 'https://webiam.id'

BASE_DOMAIN: str = 'webiam.id'

DEPENDENCIES: list[dict[str, Any]] = [*DEFAULT_DEPENDENCIES]

FINGERPRINTJS_API_TOKEN: str = os.environ['FINGERPRINTJS_API_TOKEN']

GOOGLE_SERVICE_PROJECT: str = os.environ['GOOGLE_SERVICE_PROJECT']

OAUTH2_CLIENTS: list[dict[str, Any]] = [
    {
        'name': "google",
        'issuer': 'https://accounts.google.com',
        'allowed_email_domains': ['gmail.com'],
        'scope': {'email', 'profile', 'openid'},
        'credential': {
            'kind': 'ClientSecret',
            'client_id': os.environ['WEBIAM_GOOGLE_CLIENT_ID'],
            'client_secret': os.environ['WEBIAM_GOOGLE_CLIENT_SECRET']
        }
    },
    {
        'name': "microsoft",
        'issuer': 'https://login.microsoftonline.com/consumers/v2.0',
        'allowed_email_domains': ['hotmail.com', 'live.com', 'outlook.com'],
        'scope': {'email', 'profile', 'openid'},
        'credential': {
            'kind': 'ClientSecret',
            'client_id': os.environ['WEBIAM_MICROSOFT_CLIENT_ID'],
            'client_secret': os.environ['WEBIAM_MICROSOFT_CLIENT_SECRET']
        }
    },
    {
        'name': "yahoo",
        'issuer': 'https://api.login.yahoo.com',
        'allowed_email_domains': ['yahoo.com'],
        'scope': {'email', 'profile', 'openid'},
        'credential': {
            'kind': 'ClientSecret',
            'client_id': os.environ['WEBIAM_YAHOO_CLIENT_ID'],
            'client_secret': os.environ['WEBIAM_YAHOO_CLIENT_SECRET']
        }
    },
]

OAUTH2_SIGNING_KEY: str = os.environ['APP_SIGNING_KEY']

OAUTH2_STORAGE: str = 'cbra.ext.google.impl.oauth2.Storage'