# Variáveis globais
servico = ''
paginas = 0
extra = 0
total = 0.00

# Dicionário de preços dos serviços por página
precos = {
    'DIG': 1.10,
    'ICO': 1.0,
    'IPB': 0.40,
    'FOT': 0.20
}

# Função escolha_servico
def escolha_servico():
  global servico
  while True:
    print('Escolha o serviço desejado:')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')
    servico = input('>> ').upper()
    if servico in precos: # Verificar de acordo com dicionário de serviços
      return servico
    else: # Se digitar uma opção diferente das do dicionário
      print('Escolha inválida, entre com o tipo do serviço novamente.')

# Função num_pagina
def num_pagina():
  global paginas
  while True:
    try:
      paginas = int(input('Entre com o número de páginas: '))
      # Se digitar valor acima de 20000
      if paginas >= 20000:
          print('Não aceitamos tantas páginas de uma vez.')
          print('Por favor, entre com o número de páginas novamente.')
      else:
          # Verificar condições e aplicar desconto
          if paginas >= 2000:
              paginas = paginas * 0.75 # Desconto de 25%
          elif paginas >= 200:
              paginas = paginas * 0.80 # Desconto de 20%
          elif paginas >= 20:
              paginas = paginas * 0.85 # Desconto de 15%
          else:
              paginas = paginas # SEM desconto
          return paginas
    # Se digitar valor não numérico
    except ValueError:
        print('Não aceitamos tantas páginas de uma vez.')
        print('Por favor, entre com o número de páginas novamente.')

# Função servico_extra
def servico_extra():
  global extra
  while True:
      print('Deseja adicionar algum serviço?')
      print('1 - Encadernação Simples - R$ 15.00')
      print('2 - Encadernação Capa Dura - R$ 40.00')
      print('0 - Não desejo mais nada')
      try:
          opcao = int(input('>> '))
          if opcao == 1:
              extra = 15.00
              return extra
          elif opcao == 2:
              extra = 40.00
              return extra
          elif opcao == 0:
              extra = 0.00
              return extra
          else:
              print('Opção inválida, entre com a opção novamente.')
      except ValueError:
          print('Opção inválida, entre com a opção novamente.')


# Programa principal
print('Bem-vindo à Copiadora da Larissa de Santi')
servico = escolha_servico() # Retorna o tipo de serviço
paginas = num_pagina() # Retorna a quantidade de páginas
extra = servico_extra() # Retorna condições para desconto
total = precos[servico] * paginas + extra # Calcula o total (fora de função)
print(f'Total: R$ {total:.2f} (serviço: {precos.get(servico):.2f} * páginas: {paginas:.0f} + extra: {extra:.2f})')
