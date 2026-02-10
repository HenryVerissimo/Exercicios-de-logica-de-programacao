# Exercício de Lógica: O Analista de Temperaturas

## 📌 Tema
**Estruturas de Dados Lineares (Vetores/Arrays)**

---

## 📝 Enunciado
Uma estação meteorológica precisa de um pequeno sistema para monitorar as temperaturas registradas durante uma semana (7 dias). O objetivo é desenvolver um programa em C que armazene essas temperaturas, calcule a média semanal e identifique o desempenho térmico do período.



---

## ⚙️ Requisitos

### Requisitos Funcionais (RF)
- **RF1:** O programa deve solicitar ao usuário a temperatura (valor real) de cada um dos 7 dias da semana.
- **RF2:** O sistema deve calcular a média aritmética simples de todas as temperaturas informadas.
- **RF3:** O programa deve identificar e contar quantos dias registraram temperaturas estritamente maiores que a média calculada.
- **RF4:** O sistema deve exibir o valor da média e a quantidade de dias acima dela.

### Requisitos Não Funcionais (RNF)
- **RNF1:** O código deve ser desenvolvido na linguagem **C**.
- **RNF2:** É obrigatório o uso de um **vetor (array)** de tamanho 7 para armazenar os dados.
- **RNF3:** Devem ser utilizadas estruturas de repetição (`for` ou `while`) para otimizar a leitura e o processamento dos dados.
- **RNF4:** A saída da média deve ser formatada com duas casas decimais.

---

## 📥 Exemplo de Execução

**Entrada:**
```text
Digite a temperatura do dia 1: 25.0
Digite a temperatura do dia 2: 30.5
...
Digite a temperatura do dia 7: 24.0
```

**Saída:**
```text
Média semanal: 24.57°C
Dias acima da média: 3
```
