# Exercício Prático: Academic Analyzer (Linguagem C)

Este exercício foi elaborado para exercitar a lógica de programação, o controle de fluxo e, principalmente, a manipulação de memória através de **ponteiros** e **passagem por referência**.

---

## 📝 Enunciado
Você deve desenvolver um programa em C que processe o desempenho acadêmico de uma turma. O sistema deve receber as notas de vários alunos, calcular a média e definir um status (Aprovado, Recuperação ou Reprovado). A regra de ouro é: o cálculo e a definição do status **não podem** ser feitos na função `main`, mas sim em uma função dedicada que utiliza ponteiros para retornar os resultados.

---

## ⚙️ Requisitos Funcionais

1.  **Entrada de Dados:**
    * O programa deve perguntar quantos alunos serão processados.
    * Para cada aluno, o sistema deve solicitar duas notas ($0.0$ a $10.0$).
2.  **Função de Processamento:**
    * Crie uma função obrigatoriamente com a seguinte assinatura: 
        `void processarDesempenho(float n1, float n2, float *pMedia, char *pStatus);`
3.  **Regra de Negócio:**
    * Média $\ge 7.0$: Status **'A'** (Aprovado).
    * Média entre $5.0$ e $6.9$: Status **'R'** (Recuperação).
    * Média $< 5.0$: Status **'F'** (Reprovado/Falhou).
4.  **Saída de Dados:**
    * O programa deve exibir a média com duas casas decimais e a situação por extenso (ex: "APROVADO") usando a estrutura `switch`.

---

## 🛠️ Requisitos Não Funcionais

* **Ponteiros:** A função `processarDesempenho` não deve usar a palavra-chave `return`. Ela deve alterar as variáveis da `main` diretamente via ponteiros.
* **Validação:** Use um laço `do while` para impedir que o usuário digite notas menores que 0 ou maiores que 10.
* **Organização:** Utilize um laço `for` para iterar sobre a quantidade de alunos.

---

## 📥 Exemplos de Entrada e Saída

**Entrada:**
```text
Quantidade de alunos: 1
Nota 1: 8.0
Nota 2: 7.0
```

**Saída:**
```text
------------------------------
Resultado do Aluno 1:
Média: 7.50
Situação: APROVADO
------------------------------
```