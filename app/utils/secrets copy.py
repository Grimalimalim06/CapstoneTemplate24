import os

def getSecrets():
    secrets = {
        'MONGO_HOST':"mongodb+srv://henry:henry.4jzmxjy.mongodb.net/name?retryWrites=true&w=majority",
        'MONGO_DB_NAME':"name",
        'GOOGLE_CLIENT_ID': "",
        'GOOGLE_CLIENT_SECRET':"",
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration",
        'MY_EMAIL_ADDRESS':""
        }
    return secrets