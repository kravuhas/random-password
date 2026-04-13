# random-password

python3 --version

git clone https://github.com/your-username/password-generator.git

cd password-generator

python3 gerador_senhas.py

=================================
||      Gerador de Senhas      ||
=================================
Número de senhas: 3
Total de dígitos na senha (16 a 35): 20
=================================

Senha 1: k@3Xm!nQ_zA2#wL+8vTp
Senha 2: P9$hRu.mW!2eKj@7Ny+d
Senha 3: 4!Zv#xLq@8TnBp_3mWsJ

password-generator/
├── gerador_senhas.py   # Main script
└── README.md           # This file

def geraSenha(n_senha, t_senha):
    for _ in range(n_senha):
        # 1. Guarantee at least one of each character type
        senha = [random.choice(especiais),
                 random.choice(numeros),
                 random.choice(letras_min),
                 random.choice(letras_mai)]
        # 2. Fill remaining slots from the full pool
        while len(senha) < t_senha:
            senha.append(random.choice(todos))
        # 3. Shuffle to remove predictable positions
        random.shuffle(senha)

        


