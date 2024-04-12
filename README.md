# Bootcamp Back-End Python e Django

## Exercício: Erros e Exceções

### Descrição do Problema:
O programa a seguir deve calcular a média dos valores digitados pelo usuário. No entanto, ele não está funcionando corretamente.

### Objetivo:
Corrigir o programa para que ele calcule corretamente a média dos valores inseridos pelo usuário.

### Solução:
O problema ocorre devido a erros de sintaxe e lógica no código Python. Os principais problemas incluem:
- Falta de inicialização das variáveis 'tamanho' e 'soma' na função 'calcular_media'.
- Uso incorreto da função 'enumerate' no loop 'for' na função 'calcular_media'.
- Verificação incorreta para encerrar a entrada de valores no loop 'while' principal.
- Falta de tratamento de erros para garantir que apenas valores numéricos sejam aceitos.

Para corrigir o programa, fizemos as seguintes alterações:
- Inicializamos as variáveis 'tamanho' e 'soma' como zero na função 'calcular_media'.
- Corrigimos o loop 'for' na função 'calcular_media' para iterar corretamente sobre os valores na lista.
- Atualizamos a lógica do loop 'while' principal para encerrar a entrada de valores quando o usuário digita 'ok'.
- Adicionamos um bloco 'try-except' para tratar erros de entrada do usuário e garantir que apenas valores numéricos sejam aceitos.

Agora, o programa deve calcular corretamente a média dos valores inseridos pelo usuário.

### Execução do Programa:
Para executar o programa corrigido, basta seguir as instruções fornecidas no prompt de comando ou na interface do usuário.

