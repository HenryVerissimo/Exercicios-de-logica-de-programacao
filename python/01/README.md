# Exercício de Lógica: Validador de Fluxo de Cadastro (Backend Python)

Este exercício simula uma camada de validação de dados, fundamental para proteger a integridade de bancos de dados em aplicações backend.

---

## 📝 Enunciado
Você deve desenvolver uma função que receba dados de um novo usuário (Nome, Idade, Email e se é Administrador). O objetivo é garantir que esses dados sigam as regras de negócio da empresa antes de permitir o "salvamento" no sistema. O programa deve retornar uma mensagem de sucesso ou o erro específico encontrado.

---

## ⚙️ Requisitos

### Funcionais
- **Validação de Nome:** Não pode estar vazio e deve conter no mínimo 3 caracteres.
- **Validação de Idade:** Deve ser um número inteiro positivo entre 18 e 100 anos.
- **Validação de Email:** Deve conter obrigatoriamente um `@` e pelo menos um ponto `.` após o arroba.
- **Verificação de Perfil:** Se o usuário for administrador (`admin=True`), a mensagem de sucesso deve ser personalizada.

### Não Funcionais
- **Estruturas Condicionais:** Utilizar `if`, `elif` e `else` para as validações.
- **Tratamento de Erros:** Utilizar blocos `try/except` para lidar com entradas de idade que não sejam números.
- **Modularização:** O código deve ser organizado dentro de uma função principal de validação.

---

## 📥 Exemplos de Entrada e Saída

| Entrada (Nome, Idade, Email, Admin) | Saída Esperada |
| :--- | :--- |
| `"Jo"`, `25`, `"jo@dev.com"`, `False` | `Erro: O nome deve ter pelo menos 3 caracteres.` |
| `"Carlos"`, `17`, `"carlos@email.com"`, `False` | `Erro: O usuário deve ser maior de idade.` |
| `"Ana"`, `30`, `"ana@email.com"`, `True` | `Cadastro realizado com sucesso! Bem-vinda, administradora Ana.` |
| `"Luiz"`, `"vinte"`, `"luiz@web.com"`, `False` | `Erro: A idade deve ser um valor numérico.` |

---

## 🚀 Desafio Extra (Opcional)
Tente armazenar os usuários validados em uma **lista** (simulando um banco de dados temporário) e permita que o programa valide múltiplos usuários em um loop até que o desenvolvedor digite "sair".