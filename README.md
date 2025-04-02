# **Sistema de Pedidos para Copiadora**
---
Atividade prática desenvolvida para a disciplina de **Lógica de Programação e Algoritmos** do Bacharelado em Engenharia de Software.


---
### Objetivos
Implementar um sistema de pedidos para copiadora:
- Calcular valores de serviços de impressão.
- Aplicar descontos progressivos conforme quantidade de páginas.
- Gerenciar serviços adicionais.
- Validar todas as entradas do usuário:

```python
def validar_paginas():
    while True:
        try:
            paginas = int(input('Número de páginas: '))
            if paginas >= 20000:
                print('Não aceitamos pedidos com 20.000+ páginas')
            else:
                return paginas
        except ValueError:
            print('Digite um número válido!')
```

---
### Competências Desenvolvidas
- Estruturas condicionais complexas (`if/elif/else`).
- Validação de entradas.
- Manipulação de estruturas de dados (dicionário).
- Tratamento de erro.
- Formatação de saída:

```python
print(f'Total: R$ {total:.2f} (serviço: {precos.get(servico):.2f} * páginas: {paginas:.0f} + extra: {extra:.2f})')
```

---
### Execução do Programa
![Saída de console esperada](https://github.com/larisanti/py-3/blob/main/output.png)

---
### Como Executar
```bash
python3 copiadora_pedidos.py
```
