import random

print('=================================')
print('||      Gerador de Senhas      ||')
print('=================================')

num_senhas = int(input("Número de senhas: ") or 1)

tamanho_senha = 0
while tamanho_senha < 16 or tamanho_senha > 35:
    tamanho_senha = int(input("Total de dígitos na senha (16 a 35): ") or "16")
    if tamanho_senha < 16 or tamanho_senha > 35:
        print('A senha deve ter entre 16 e 35 dígitos.')

print('=================================\n')

# possíveis caracteres
especiais  = ['.', '+', '-', '@', '#', '*', '!', '?', '~', '$', '_']
numeros    = ['0','1','2','3','4','5','6','7','8','9']
letras_min = list('abcdefghijklmnopqrstuvwxyz')
letras_mai = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def geraSenha(n_senha, t_senha):
    senhas = []
    for _ in range(n_senha):
        senha = []
        # garante pelo menos 1 de cada tipo
        senha.append(random.choice(especiais))
        senha.append(random.choice(numeros))
        senha.append(random.choice(letras_min))
        senha.append(random.choice(letras_mai))
        # preenche o restante com qualquer caractere
        todos = especiais + numeros + letras_min + letras_mai
        while len(senha) < t_senha:
            senha.append(random.choice(todos))
        # embaralha para não ficar em ordem previsível
        random.shuffle(senha)
        senhas.append(''.join(senha))
    return senhas

senhas_geradas = geraSenha(num_senhas, tamanho_senha)

for j, senha in enumerate(senhas_geradas, start=1):
    print(f'Senha {j}: {senha}')

print('\n=================================')