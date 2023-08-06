# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from cbra.types import NotFound
from cbra.types import SessionRequestPrincipal
from cbra.ext.oauth2 import AuthorizationServerEndpoint

from .models import GrantConsentRequest


class ConsentEndpoint(AuthorizationServerEndpoint):
    __module__: str = 'webiam.app.endpoints'
    name: str = 'oauth2.consent'
    principal: SessionRequestPrincipal # type: ignore
    path: str = '/consent'
    require_authentication: bool = True
    summary: str = 'Consent Endpoint'

    async def post(self, dto: GrantConsentRequest) -> None:
        owner = await self.get_owner(dto.client_id)
        if owner is None:
            raise NotFound
        owner.consents.update([x.name for x in dto.scope])
        await self.persist(owner)