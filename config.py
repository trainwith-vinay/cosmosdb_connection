import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://stage-ecp-ecdh-db-sqlapi-cosmos-db.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'QQNy5iretefvxptCwqlDk7lseLWYbiju8QeoT86yF72uAFP41ZmyPiesRgrt28xmRgetPMPjZ0yZA9qsX4puzA=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}