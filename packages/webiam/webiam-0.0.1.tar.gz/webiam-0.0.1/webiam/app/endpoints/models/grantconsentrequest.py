# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic
from cbra.ext.oauth2.types import GrantedScope

from webiam.canon import FingerprintReference


class GrantConsentRequest(pydantic.BaseModel):
    client_id: str = pydantic.Field(
        default=...,
        title="Client ID",
        description=(
            "Identifies the client to which the consent is given for the "
            "scope or claims."
        )
    )

    scope: list[GrantedScope] = pydantic.Field(
        default=...,
        title="Scope/Claims",
        description="The scope or claims that the Resource Owner consents to."
    )

    fingerprint: FingerprintReference = pydantic.Field(
        default=...,
        title="A fingerprint of the user agent."
    )