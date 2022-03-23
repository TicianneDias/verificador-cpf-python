"""Descubra se um cpf computado é válido ou não."""


def multiplica_digitos_parte_um(numeros):
    """Multiplicação dos 9 primeiros valores de 10 a 2 e compara com o décimo dígito do CPF."""
    cont = 10
    valor = 0

    for i in range(0, 9):
        mult = numeros[i] * cont
        cont -= 1
        valor += mult

    resto = (valor * 10) % 11

    if resto == 10:
        return 0 == numeros[9]

    return resto == numeros[9]


def multiplica_digitos_parte_dois(numeros):
    """Multiplicação dos 10 primeiros valores de 11 a 2 e compara com o último dígito do CPF."""
    cont = 11
    valor = 0

    for i in range(0, 10):
        mult = numeros[i] * cont
        cont -= 1
        valor += mult

    resto = (valor * 10) % 11

    if resto == 10:
        return 0 == numeros[10]

    return resto == numeros[10]


def cpf_valido(numeros):
    """Verifica se todos os dígitos são iguais e retorna CPF válido"""
    return numeros != numeros[::-1]


def main():
    numeros = list(
        map(int, list(input('Digite o cpf: ')
                      .replace('.', '')
                      .replace('-', ''))))

    if multiplica_digitos_parte_um(numeros) \
            and multiplica_digitos_parte_dois(numeros) \
            and cpf_valido(numeros):
        print('\033[34mCPF Válido!')
    else:
        print('\033[31mCPF Inválido!')


if __name__ == '__main__':
    main()
