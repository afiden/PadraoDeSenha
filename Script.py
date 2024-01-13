import itertools
import string

# Exemplo de Funcionamento
# Vocẽ identificou o seguinte padrão de Senhas
# Exempl1FN4
# Exempl2FN51
# Exempl12FN27
# Exempl96FN41
# A senha é sempre igual, apenas dois espaços mudam
# Você utilizará o script para gerar todas as possíveis combinações para este padrão
# Para utilizar, modifique o base_password

# Base da senha
base_password = "Exempl{}FN{}"

# Possíveis caracteres para a posição X (letras e dígitos)
characters_for_X = string.ascii_letters + string.digits

# Possíveis dígitos para a posição Y (incluindo combinações de dois dígitos)
digits_for_Y = [str(i) for i in range(100)]  # Gera números de 0 a 99

# Gerar combinações
passwords = [base_password.format(x, y) for x, y in itertools.product(characters_for_X, digits_for_Y)]

# Exibir as primeiras 10 combinações para verificação
print(passwords[:10])

# Exibir o total de combinações geradas
print(f"Total de combinações geradas: {len(passwords)}")
