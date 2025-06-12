class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def construir_arvore(array):
    if not array:
        return None

    # Encontrar o maior elemento e seu índice (a raiz)
    max_valor = max(array)
    raiz_index = array.index(max_valor)
    raiz = Node(max_valor)

    # Elementos à esquerda e à direita da raiz
    esquerda = sorted(array[:raiz_index], reverse=True)
    direita = sorted(array[raiz_index + 1:], reverse=True)

    # Construir galhos da esquerda (em cadeia à esquerda)
    atual = raiz
    for val in esquerda:
        atual.esquerda = Node(val)
        atual = atual.esquerda

    # Construir galhos da direita (em cadeia à direita)
    atual = raiz
    for val in direita:
        atual.direita = Node(val)
        atual = atual.direita

    return raiz

# Função para imprimir a árvore em formato visual
def print_arvore(node, prefix="", is_left=True):
    if node is not None:
        print_arvore(node.direita, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.valor))
        print_arvore(node.esquerda, prefix + ("    " if is_left else "│   "), True)

# Testes:
print("Cenário 1:")
arvore1 = construir_arvore([3, 2, 1, 6, 0, 5])
print_arvore(arvore1)

print("\nCenário 2:")
arvore2 = construir_arvore([7, 5, 13, 9, 1, 6, 4])
print_arvore(arvore2)
