# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import pydantic


class FingerprintUseragent(pydantic.BaseModel):
    name: str | None = pydantic.Field(
        default=None,
        alias='browserName'
    )

    major_version: str | None = pydantic.Field(
        default=None,
        alias='browserMajorVersion'
    )

    version: str | None = pydantic.Field(
        default=None,
        alias='browsbrowserFullVersionerMajorVersion'
    )

    os_name: str | None = pydantic.Field(
        default=None,
        alias='os'
    )

    os_version: str | None = pydantic.Field(
        default=None,
        alias='osVersion'
    )

    device: str | None = pydantic.Field(
        default=None,
        alias='device'
    )

    user_agent: str | None = pydantic.Field(
        default=None,
        alias='userAgent'
    )