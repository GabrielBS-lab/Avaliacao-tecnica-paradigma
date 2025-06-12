using System;
using System.Collections.Generic;
using System.Linq;

class Node
{
    public int Valor { get; set; }
    public Node Esquerda { get; set; }
    public Node Direita { get; set; }

    public Node(int valor)
    {
        Valor = valor;
    }
}

class ArvoreBinaria
{
    public static Node ConstruirArvore(int[] array)
    {
        if (array == null || array.Length == 0)
            return null;

        int maxValor = array.Max();
        int raizIndex = Array.IndexOf(array, maxValor);
        var raiz = new Node(maxValor);

        var esquerda = array.Take(raizIndex).OrderByDescending(x => x).ToList();
        var direita = array.Skip(raizIndex + 1).OrderByDescending(x => x).ToList();

        var atual = raiz;
        foreach (var val in esquerda)
        {
            atual.Esquerda = new Node(val);
            atual = atual.Esquerda;
        }

        atual = raiz;
        foreach (var val in direita)
        {
            atual.Direita = new Node(val);
            atual = atual.Direita;
        }

        return raiz;
    }

    public static void ImprimirArvore(Node node, string prefix = "", bool isLeft = true)
    {
        if (node == null) return;

        if (node.Direita != null)
            ImprimirArvore(node.Direita, prefix + (isLeft ? "│   " : "    "), false);

        Console.WriteLine(prefix + (isLeft ? "└── " : "┌── ") + node.Valor);

        if (node.Esquerda != null)
            ImprimirArvore(node.Esquerda, prefix + (isLeft ? "    " : "│   "), true);
    }

    static void Main()
    {
        Console.WriteLine("Cenário 1:");
        var arvore1 = ConstruirArvore(new int[] { 3, 2, 1, 6, 0, 5 });
        ImprimirArvore(arvore1);

        Console.WriteLine("\nCenário 2:");
        var arvore2 = ConstruirArvore(new int[] { 7, 5, 13, 9, 1, 6, 4 });
        ImprimirArvore(arvore2);
    }
}
