import jwt
import secret

payload = {
    'user_id':113,
    'nome':'Alberto Silva',
    'admin': True
}
token = jwt.encode(payload, secret, algorithm='HS256')
print(token)

decode_token = jwt.decode(token, secret, algorithms=['HS256'])

try:
    decode_token = jwt.decode(token, secret, algorithms=['HS256'])
except jwt.invalidTokenError:
    print(f'Erro')
