# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import logging

import httpx

from cbra.core.conf import settings
from webiam.canon import Fingerprint
from webiam.canon import FingerprintReference


class FingerprintResolver:
    """Provides an interface to resolve fingerprints."""
    __module__: str = 'webiam.infra'
    base_url: str
    logger: logging.Logger = logging.getLogger('cbra.endpoint')

    def __init__(self, base_url: str = "https://api.fpjs.io"):
        self.base_url = base_url

    async def resolve(self, ref: FingerprintReference) -> Fingerprint:
        """Retrieve extended details for the given reference to a
        fingerprint.
        """
        headers = {'Auth-API-Key': settings.FINGERPRINTJS_API_TOKEN}
        async with httpx.AsyncClient(base_url=self.base_url, headers=headers) as client:
            response = await client.get( # type: ignore
                url=f'/visitors/{ref.visitor_id}',
                params={'request_id': ref.request_id}
            )
            if response.status_code in (400, 403, 429):
                # 400 is assumed to occur when there is some tampering with the input,
                # 429 is rate limited.
                if response.status_code == 403:
                    self.logger.warning("Received 403 response from FingerprintJS")
                elif response.status_code == 400:
                    self.logger.warning("Received 400 response from FingerprintJS")
                elif response.status_code == 429:
                    self.logger.critical("FingerprintJS is rate-limiting requests.")
            response.raise_for_status()
            data = response.json()
        visits = data.get('visits')
        if not visits:
            raise ValueError('No visits returned from FingerprintJS')
        return Fingerprint.parse_obj({**visits[0], 'visitorId': data['visitorId']})