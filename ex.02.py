nome = str(input('Nome: ')).upper()
senha = str(input('Senha: ')).upper()
while nome == senha:
    print('A senha não pode ser igual ao nome. Senha inválida!')
    senha = str(input('Digite novamente a senha: ')).upper()

print('Login: %s'%(nome))
print('Senha: %s '%(senha))