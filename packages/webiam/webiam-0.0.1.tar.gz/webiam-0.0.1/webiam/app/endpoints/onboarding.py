# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import fastapi

from cbra.ext import oauth2
from cbra.types import Forbidden
from cbra.types import ServiceNotAvailable

from webiam.infra import FingerprintResolver
from webiam.canon import FingerprintReference
from webiam.canon import Fingerprint
from .models import BeginOnboardRequest


class OnboardingEndpoint(oauth2.OnboardingEndpoint):
    __module__: str = 'webiam.app.endpoints'
    resolver: FingerprintResolver = FingerprintResolver()

    async def post( # type: ignore
        self,
        dto: BeginOnboardRequest,
        client_id: str = fastapi.Path(
            default=...,
            title="Client ID",
            description=(
                "Specifies the OIDC client application used to "
                "authenticate with the downstream authorization "
                "server."
            )
        )
    ) -> oauth2.models.BeginOnboardResponse:
        response = await super().post(dto, client_id)
        try:
            fp = await self.resolver.resolve(dto.fingerprint)
        except Exception:
            raise ServiceNotAvailable
        self.validate_fingerprint(dto.fingerprint, fp)
        self.session.set('icg', fp.incognito)
        self.session.set('uai', fp.visitor_id)
        return response
    
    def validate_fingerprint(
        self,
        ref: FingerprintReference,
        fingerprint: Fingerprint
    ) -> None:
        if fingerprint.visitor_id != ref.visitor_id:
            self.logger.critical("Fingerprint mismatch.")
            raise Forbidden