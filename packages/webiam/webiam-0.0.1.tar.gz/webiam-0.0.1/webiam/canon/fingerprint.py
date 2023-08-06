# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Literal

import pydantic

from .fingerprintconfidence import FingerprintConfidence
from .fingerprintlocation import FingerprintLocation
from .fingerprintuseragent import FingerprintUseragent


class Fingerprint(pydantic.BaseModel):
    """Represents a reference to a device fingerprint created with
    FingerprintJS.
    """
    kind: Literal['browser'] = 'browser'

    request_id: str = pydantic.Field(
        default=...,
        alias='requestId'
    )

    incognito: bool = pydantic.Field(
        default=False,
    )

    ip: str = pydantic.Field(
        default=...,
    )

    location: FingerprintLocation | None = pydantic.Field(
        default=None,
        alias='ipLocation'
    )

    ua: FingerprintUseragent | None = pydantic.Field(
        default=None,
        alias='browserDetails'
    )

    confidence: FingerprintConfidence = pydantic.Field(
        default=...,
    )

    url: str = pydantic.Field(
        default=...,
    )

    timestamp: int = pydantic.Field(
        default=...,
    )

    found: bool = pydantic.Field(
        default=...,
        alias='visitorFound'
    )

    visitor_id: str = pydantic.Field(
        default=...,
        alias='visitorId'
    )