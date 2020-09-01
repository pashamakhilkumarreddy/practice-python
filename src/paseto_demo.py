import json
import secrets
import uuid
import paseto
import pysodium

key = secrets.token_bytes(32)

ttl = 60 * 5

data = {
  'id': str(uuid.uuid1()),
  'name': 'John Doe',
  'type': 'super-admin',
}

token = paseto.create(key = key, purpose='local', claims = data, footer = {
  'check': True
}, exp_seconds=ttl)


print(f'''
      Token Data 
      {json.dumps(data, indent = 4)}
      PASETO 
      {token.decode("utf-8")}
''')

parsed_token = paseto.parse(key = key, purpose='local', token = token)

print(f'''
      Parsed Token data
      {json.dumps(parsed_token['message'], indent=2)}
      
      Token Footer
      
      {json.dumps(parsed_token['footer'], indent=2)}
      ''')

pk, sk = pysodium.crypto_sign_keypair()

token = paseto.create(key = sk, purpose = 'public', claims=data, 
                      footer = { 'check': True }, exp_seconds=ttl)

print(f'''
      Token Data
      
      {json.dumps(data, indent = 2)}
      
      PASETO
      
      {token.decode('utf-8')}
      ''')

parsed = paseto.parse(key = pk, purpose='public', token = token)

parsed_token = json.dumps(parsed['message'], indent = 2)

print(f'''
      Parsed Token Data
           
      {parsed_token}
      
      Token FOOTER
      
      {json.dumps(parsed['footer'], indent = 2)}
      ''')