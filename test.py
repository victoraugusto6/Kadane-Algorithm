from main import somador


def test():
    lista_1 = [-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]
    assert somador(lista_1, len(lista_1)) == 13

    lista_2 = [6, -4, -2, 1, -3, 5, -1, 2, 1, 1, -5, 4]
    assert somador(lista_2, len(lista_2)) == 8

    lista_3 = [-2, -3, 4, -1, -2, 5, -3]
    assert somador(lista_3, len(lista_3)) == 6
