import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://dev-ecp-ecdh-db-sqlapi-cosmos-db.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'yWvLxGRtV5zxspXPwZk8BvrPbMB08oe2A3Nne3q7PV0dNK3mnsxnIqRSK9UqNpKn47A7dD0t7B2b5Aqa0MeCvQ=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}