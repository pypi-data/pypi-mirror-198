# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""The Asynchronous Server Gateway Interface (ASGI) module for integration
with external application servers.
"""
import cbra.core as cbra
from cbra.ext.google import Service
from cbra.ext.oauth2 import AuthorizationServer
from cbra.ext.oauth2.types import ResponseType

from . import endpoints



oauth2 = AuthorizationServer(
    response_types=[
        ResponseType.code
    ],
    oidc_onboarding_endpoint=endpoints.OnboardingEndpoint
)
oauth2.handlers.add(endpoints.ConsentEndpoint)
application = cbra.autodiscover(__name__, Service)
application.add(
    oauth2,
    prefix="/oauth/v2"
)