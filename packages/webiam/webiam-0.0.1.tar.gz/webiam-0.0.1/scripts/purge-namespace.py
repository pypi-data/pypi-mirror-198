#!/usr/bin/env python3
from google.cloud.datastore import Client


NAMESPACE = 'webiam.unimatrixapis.com'
client = Client(project='unimatrixdev', namespace=NAMESPACE)
query = client.query(kind='__kind__')
query.keys_only()

kinds = [entity.key.id_or_name for entity in query.fetch()]
for kind in kinds:
    query = client.query(kind=kind, namespace=NAMESPACE)
    query.keys_only()
    keys = query.fetch()
    client.delete_multi(keys)
