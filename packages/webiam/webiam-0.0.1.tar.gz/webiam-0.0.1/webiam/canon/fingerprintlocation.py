# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic

from .fingerprintlocationcity import FingerprintLocationCity
from .fingerprintlocationcontinent import FingerprintLocationContinent
from .fingerprintlocationcountry import FingerprintLocationCountry


class FingerprintLocation(pydantic.BaseModel):
    accuracy: int | None = pydantic.Field(
        default=None,
        alias='accuracyRadius'
    )

    latitude: float | None = pydantic.Field(
        default=None,
    )

    longitude: float | None = pydantic.Field(
        default=None,
    )

    postal_code: str | None = pydantic.Field(
        default=None,
        alias='postalCode'
    )

    timezone: str | None = pydantic.Field(
        default=None,
    )

    city: FingerprintLocationCity | None = pydantic.Field(
        default=None,
    )

    country: FingerprintLocationCountry | None = pydantic.Field(
        default=None,
    )

    continent: FingerprintLocationContinent | None = pydantic.Field(
        default=None,
    )