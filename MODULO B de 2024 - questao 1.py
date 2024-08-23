#QUESTÃO 1 de 4 - Conteúdo até Aula 03

print('Bem-vindos à loja do Eduardo Winter')   #Colocar nome completo:EXIGÊNCIA DE CÓDIGO 1 de 6

valorDoPedido = float(input('Entre com o valor do pedido:$ '))   #implementar o input do valorDoPedido e da quantidadeParcelas [EXIGÊNCIA DE CÓDIGO 2 de 6]
qtdeParcelas = int(input('Entre com a quantidade de parcelas: '))

if (qtdeParcelas < 4):                      #implementar juros, conforme número de parcelas do enunciado. [EXIGÊNCIA DE CÓDIGO 3 de 6];
    valorDaParcela = valorDoPedido / qtdeParcelas  
    valorTotalParcelado = valorDoPedido     #nao possui juros  devido nº de parcelas  minima
    print(f'Valor da parcela é de: ${valorDaParcela:.2f} e o Valor Total parcelado é de:${valorTotalParcelado} ')

elif (qtdeParcelas >= 4) and (qtdeParcelas < 6):   #parcelas entre 4 e 5 vezes
    valorDaParcela = valorDoPedido * (1 + 0.04) / qtdeParcelas #juros de 4%
    valorTotalParcelado = valorDaParcela * qtdeParcelas
    print(f'Valor da parcela é de: ${valorDaParcela:.2f} e o Valor Total parcelado é de:${valorTotalParcelado} ')

elif (qtdeParcelas >= 6) and (qtdeParcelas < 9):   #parcelas entre 6 e 8 vezes
    valorDaParcela = valorDoPedido * (1 + 0.08) / qtdeParcelas  #juros de 8%
    valorTotalParcelado = valorDaParcela * qtdeParcelas
    print(f'Valor da parcela é de: ${valorDaParcela:.2f} e o Valor Total parcelado é de:${valorTotalParcelado} ')

elif (qtdeParcelas >= 9) and (qtdeParcelas < 13):   #parcelas entre 9 e 12 vezes
    valorDaParcela = valorDoPedido * (1 + 0.16) / qtdeParcelas   #juros de 16%
    valorTotalParcelado = valorDaParcela * qtdeParcelas
    print(f'Valor da parcela é de: ${valorDaParcela:.2f} e o Valor Total parcelado é de:${valorTotalParcelado} ')

else : #parcelas a partir de 13 vezes
    valorDaParcela = valorDoPedido * (1 + 0.32) / qtdeParcelas   #juros de 32%
    valorTotalParcelado = valorDaParcela * qtdeParcelas 
    print(f'Valor da parcela é de: ${valorDaParcela:.2f} e o Valor Total parcelado é de:${valorTotalParcelado} ')


    


    