def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9