#QUESTÃO 3 de 4 - Conteúdo até aula 05

print('LOJA DO EDUARDO WINTER')

def escolha_modelo(): ##função para escolha de modelo de camiseta
    print('Escolha  o modelo desejado')
    print('MCS - Manga Curta Simples ')
    print('MLS - Camiseta Manga Longa Simples  ')
    print('MCE - Camiseta Manga Curta Com Estampa ')
    print('MLE - Camiseta Manga Longa Com Estampa ')

    while True: ##entrada do modelo desejado
        modelo = input ('Entre com o modelo desejado:  ') .upper().strip()       
        if modelo != 'MCS' and modelo != 'MLS' and modelo != 'MCE' and modelo != 'MLE': #mensagem de erro em  entrada que não seja valida
             print('Escolha inválida, favor tente novamente')
             continue
        else:  # seleciona modelo desejado e retorna com valor
            if modelo == "MCS":
                return 1.80
            elif modelo == 'MLS':
                return 2.10
            elif modelo == 'MCE':
                return 2.90
            else:    #para modelo MLE 
                return 3.20

def num_camiseta():   #função para definir o desconto, conforme numero de camisetas
    desconto = 0.0
    qtd_camisetas = 0
    
    while True:
        try:
            qtd_camisetas = int(input("Entre com o numero de camisetas: "))
            if qtd_camisetas > 20000:
                print('Não é aceito pedidos nessa quantidade de camisetas') #mensagem de erro devido a quantidade extrapolar o limite 
                continue
       
            if  20 <= qtd_camisetas < 200:  #desconto de 5% para este intervalo de  nº camisetas
                desconto = 0.05
                
            
            elif 200 <= qtd_camisetas < 2000: #desconto de 7% para este intervalo de  nº camisetas
                desconto = 0.07
                
            
            elif 2000 <= qtd_camisetas < 20000: #desconto de 12% para este intervalo de  nº camisetas
                desconto = 0.12
                
            else:   #para pedidos < 20, não há desconto
                desconto = 0

            break
        
        except ValueError:
            print ('Valor não numerico, tente novamente')
    
    return qtd_camisetas * (1 - desconto)   #retornando desconto

def frete(): #função para escolher o tipo de frete para ser escolhido no menu
    print(' ESCOLHA TIPO DE FRETE:')
    print('1 - Frete por transportadora - R$ 100.00 ')
    print('2 - Frete por SEDEX - R$ 200.00 ')
    print('0 - Retirar pedido na fábrica - R$ 0.00')

    while True:
       try:
        adicional_frete = int(input('Escolha o tipo de frete (1/2/0): ')) # entrada do tipo de frete a ser escolhido
            
        if adicional_frete != 1 and adicional_frete != 2 and adicional_frete != 0: # em caso de entrada inválida
            print(adicional_frete)  
            continue

        if adicional_frete == 1: #escolha da opção de frete com retorno do valor do mesmomle
            
           return 100.00
        elif adicional_frete == 2:
            return 200.00
        else:
            return 0.00
        
       except ValueError:
           print('Opção inválida. Favor, tente novamente')
           continue

#chamando funções e atribuindo  variáveis
modelo = escolha_modelo()
qtd_camisetas = num_camiseta()
adicional_frete = frete()

#Saída do total a pagar
print (f'Total a pagar: R$ {((modelo * qtd_camisetas) + adicional_frete):.2f}')

