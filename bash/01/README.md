# Exercício de Lógica: Organizador de Workspace Inteligente (Bash)

Este é um desafio prático de automação em Shell Script para treinar lógica de programação, manipulação de arquivos e variáveis de ambiente.

---

## 📝 Enunciado
Você percebeu que sua pasta de trabalho (`workspace`) está desorganizada, repleta de arquivos de log e temporários. Sua missão é criar um script chamado `organizador.sh` que automatize a limpeza dessa pasta, movendo arquivos específicos para um diretório de backup e renomeando-os com um carimbo de data para evitar que arquivos antigos sejam sobrescritos.

## ✅ Requisitos Funcionais

1.  **Verificação de Diretório:** O script deve verificar se existe uma pasta chamada `backup`. Caso não exista, ele deve criá-la automaticamente.
2.  **Filtragem de Arquivos:** O script deve processar apenas arquivos com as extensões `.log` e `.tmp`.
3.  **Renomeação Dinâmica:** Ao mover cada arquivo para a pasta `backup`, o script deve inserir a data atual no nome do arquivo (antes da extensão).
    * *Exemplo:* `servidor.log` → `servidor_2026-02-01.log`.
4.  **Feedback Visual:** O script deve imprimir no terminal cada ação realizada (ex: "Movendo arquivo X para Y").
5.  **Contador Final:** Ao concluir a execução, o script deve exibir o total de arquivos que foram movidos.

## ⚙️ Requisitos Não Funcionais

* **Variáveis:** Utilize variáveis para definir os caminhos de origem e destino.
* **Tratamento de Erros:** O script deve lidar graciosamente com situações onde não existam arquivos `.log` ou `.tmp` na pasta, exibindo uma mensagem informativa em vez de erros de sistema.
* **Boas Práticas:** O código deve conter comentários explicativos em cada bloco lógico relevante.

## 📥 Exemplo de Entrada e Saída

**Arquivos na pasta atual:**
- `app.py`
- `debug.log`
- `temp_data.tmp`
- `notas.txt`

**Execução:**
```bash
bash organizador.sh
```

**Saída esperada no terminal:**

```bash
[INFO] Criando diretório de backup...
[OK] Movendo debug.log -> backup/debug_2026-02-01.log
[OK] Movendo temp_data.tmp -> backup/temp_data_2026-02-01.tmp
--------------------------------------
Limpeza concluída! 2 arquivos movidos para o backup.
```
