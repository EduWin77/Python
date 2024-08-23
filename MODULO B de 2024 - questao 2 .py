#QUESTÃO 2 de 4 - Conteúdo até aula 04

print ('Bem vindos a loja de Marmitas do EDUARDO WINTER')  #impressao do meu nome e do menu do cardápio
print(30 * '>', 'MENU', '<' * 30)
print('Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais')
print('Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais')
print('Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais')


valor_pedido = 0.0  #variavel para pedido especifico
valor_Total = 0.0 #inicia variavel do valor total do pedido, o qual pode inserir varios pedidos
acumulador = 0 #variavel para acumular pedido

while True:
    sabor = input('Entre com sabor desejado (BA/FF):').upper().strip() #entrada para escolher sabor
    if sabor != 'BA' and sabor != 'FF':           #caso a opção seja inválida
        print('Sabor inválido. Tente novamente')
        continue

    tamanho = input('Entre com tamanho desejado (P/M/G): ').upper().strip() #entrada para escolher tamanho da marmita
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':  #caso  tamanho seja inválida
        print('Tamanho inválido. Tente novamente')
        continue


    if sabor == 'BA': #condicionais para escolha do sabor e acumulador do valor do pedido de cada
        if tamanho == 'P':
            acumulador += 16
            print(f"Você pediu um Bife Acebolado no tamanho 'P': R$ {acumulador}") 
        elif tamanho == 'M':
            acumulador += 18
            print(f"Você pediu um Bife Acebolado no tamanho 'M': R$ {acumulador}") 
        elif tamanho == 'G':
            acumulador += 22
            print(f"Você pediu um Bife Acebolado no tamanho 'G': R$ {acumulador}") 
                
      
    elif sabor == 'FF':   #condicionais para escolha do sabor e acumulador do valor do pedido de cada
        if tamanho == 'P':
            acumulador += 15
            print(f"Você pediu um Bife Acebolado no tamanho 'P': R$ {acumulador}")
        elif tamanho == 'M':
            acumulador += 17
            print(f"Você pediu um Bife Acebolado no tamanho 'M': R$ {acumulador}")
        elif tamanho == 'G':
           acumulador += 21
           print(f"Você pediu um Bife Acebolado no tamanho 'G': R$ {acumulador}")
     
    escolha = input('Deseja pedir mais alguma coisa? [S/N]: ').upper().strip() #caso o usuario queira fazer novo pedido ou encerrar, irá imprimir uma mensagem
    if escolha != 'S':
        print(f'O valor total a ser pago:$ {acumulador:.2f}')
        break

