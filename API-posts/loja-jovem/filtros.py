def filtrar_por_preco(sapatos, preco_max):
    lista_filtrada_por_preco_max = []
    for sapato in sapatos:
        if sapato['preco'] <= preco_max:
            lista_filtrada_por_preco_max.append(sapato)

def filtrar_por_tamanho(sapatos, tamanho):
    lista_filtrada_por_tamanho = []
    for sapato in sapatos:
        if sapato['tamanho'].lower() == tamanho.lower():
            lista_filtrada_por_tamanho.append(sapato)


def filtrar_por_marca(sapatos, marca):
    lista_filtrada_por_marca = []
    for sapato in sapatos:
        if sapato['marca'].lower() == marca.lower():
            lista_filtrada_por_marca.append(sapato)

    return lista_filtrada_por_marca

def filtrar_por_cor(sapatos, cor):
    lista_filtrada_por_cor = []
    for sapato in sapatos:
        if sapato['cor'].lower() == cor.lower():
            lista_filtrada_por_cor.append(sapato)

        return lista_filtrada_por_cor