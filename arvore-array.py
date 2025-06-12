class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def construir_arvore(array):
    if not array:
        return None

    max_valor = max(array)
    raiz_index = array.index(max_valor)
    raiz = Node(max_valor)

    esquerda = sorted(array[:raiz_index], reverse=True)
    direita = sorted(array[raiz_index + 1:], reverse=True)

    atual = raiz
    for val in esquerda:
        atual.esquerda = Node(val)
        atual = atual.esquerda

    atual = raiz
    for val in direita:
        atual.direita = Node(val)
        atual = atual.direita

    return raiz

def print_arvore(node, prefix="", is_left=True):
    if node is not None:
        print_arvore(node.direita, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.valor))
        print_arvore(node.esquerda, prefix + ("    " if is_left else "│   "), True)

print("Cenário 1:")
arvore1 = construir_arvore([3, 2, 1, 6, 0, 5])
print_arvore(arvore1)

print("\nCenário 2:")
arvore2 = construir_arvore([7, 5, 13, 9, 1, 6, 4])
print_arvore(arvore2)
