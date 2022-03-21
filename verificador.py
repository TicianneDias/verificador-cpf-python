"""Descubra se um cpf computado é válido ou não."""
numeros = []
cpf = input('Digite o cpf: ').replace('.', '').replace('-', '')
if len(cpf) == 11:
    for numero in cpf:
        numeros.append(int(numero))


def multiplica_digitos_parte_um(digitos):
    """Multiplicação dos 9 primeiros valores de 10 a 2 e compara com o décimo
    dígito do CPF."""
    cont = 10
    valor = 0
    for i in range(0, 9):
        mult = numeros[i]*cont
        cont -= 1
        valor += mult
    resto = (valor * 10) % 11
    if resto == 10:
        resto = 0
    if resto == numeros[9]:
        return True
    return False


def multiplica_digitos_parte_dois(digitos):
    """Multiplicação dos 10 primeiros valores de 11 a 2 e compara com o último
    dígito do CPF."""
    cont = 11
    valor = 0
    for i in range(0, 10):
        mult = numeros[i]*cont
        cont -= 1
        valor += mult
    resto2 = (valor * 10) % 11
    if resto2 == 10:
        resto2 = 0
    if resto2 == numeros[10]:
        return True
    return False


def cpf_invalido(digitos):
    """Verifica se todos os dígitos são iguais e retorna CPF inválido"""
    if numeros == numeros[::-1]:
        return False
    return True


(multiplica_digitos_parte_um(numeros))
(multiplica_digitos_parte_dois(numeros))
(cpf_invalido(numeros))
if multiplica_digitos_parte_dois(numeros) and multiplica_digitos_parte_dois(numeros) and cpf_invalido(numeros) is False:
    print('\033[31mCPF Inválido!')
else:
    print('\033[34mCPF Válido!')
