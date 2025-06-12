CREATE TABLE Colaboradores (
    Id_Colaborador INT PRIMARY KEY,
    Nome_Colaborador VARCHAR(50),
    Salario_Colaborador DECIMAL(10, 2), -- Ajustado para salários com valores quebrados
    Id_Departamento INT
);

INSERT INTO Colaboradores (Id_Colaborador, Nome_Colaborador, Salario_Colaborador, Id_Departamento) VALUES
(1, 'João Silva', 70000.50, 1),
(2, 'Helena Costa', 80000.75, 2),
(3, 'Samuel Mendes', 60000.00, 2),
(4, 'Márcia Lima', 90000.25, 1),
(5, 'Carlos Rocha', 75500.80, 1),
(6, 'Ana Pereira', 82100.90, 2),
(7, 'Felipe Souza', 68000.10, 3), -- Novo departamento
(8, 'Beatriz Alves', 95000.00, 1),
(9, 'Gustavo Martins', 72300.40, 3), -- Novo departamento
(10, 'Julia Fernandes', 88900.60, 2);


CREATE TABLE Departamentos (
    Id_Departamento INT PRIMARY KEY,
    Nome_Departamento VARCHAR(50)
);

INSERT INTO Departamentos (Id_Departamento, Nome_Departamento) VALUES
(1, 'TI'),
(2, 'Vendas'),
(3, 'Marketing'); -- Novo departamento


WITH Salarios_Com_Classificacao AS (
    SELECT
        c.Id_Colaborador,
        c.Nome_Colaborador,
        c.Salario_Colaborador,
        c.Id_Departamento,
        d.Nome_Departamento,
        RANK() OVER (PARTITION BY c.Id_Departamento ORDER BY c.Salario_Colaborador DESC) AS Posicao_Salario
    FROM
        Colaboradores AS c
    INNER JOIN
        Departamentos AS d ON c.Id_Departamento = d.Id_Departamento
)
SELECT
    Nome_Departamento AS Departamento,
    Nome_Colaborador AS Pessoa,
    Salario_Colaborador AS Salario
FROM
    Salarios_Com_Classificacao
WHERE
    Posicao_Salario = 1;
