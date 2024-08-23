#QUESTÃO 4 de 4 - Conteúdo até aula 06

print('Bem vindos a empresa do Eduardo Winter')

lista_funcionarios = []  #lista vazia para pôr cadastro funcionarios
id_global = 3662963 #variavel para acumular os id´s a partir deste numero, conforme exigencia

def cadastrar_funcionario(id):  #função cadastrar funcionarios
    global id_global  #chama id global
    print("id do Funcionário:", id)
    nome = input('Entre com nome do funcionario: ')
    setor = input('Entre com o setor do funcionario: ')

    while True:
        try:
            salario = float(input ('Entre com o salario do funcionario: '))
            break
        except ValueError:
            print('Valor inválido para salário, tente novamente.')

    funcionario = {'id':id,'nome': nome, 'setor':setor, 'salario':salario}  #atribuição de valores
    lista_funcionarios.append(funcionario.copy())   #para adicionara lista de funcionarios e copiar 'dicionario funcionario'
    id_global += 1  #contador do id global para que a cada novo cadastro, adicione o id a partir do 'nº id global' do inicio

def consultar_funcionarios(): #função de consulta dos funcionarios e menu de opção
   while True:
       print(10 * '>', 'ESCOLHA OPÇÃO DESEJADA', '<' * 10)
       print ('1. Consultar Todos') 
       print ('2. Consultar por Id') 
       print ('3. Consultar por Setor') 
       print ('4. Retornar ao menu') 
       opcao = input("Escolha uma opção do menu: ")
        
       if opcao == '1':       #opção de consulta todos
            for funcionario in lista_funcionarios:
                print(f"ID: {funcionario['id']}\n"
                      f"Nome: {funcionario['nome']}\n"
                      f"Setor: {funcionario['setor']}\n"
                      f"Salario: {funcionario['salario']}"
                      ) 
                 
                
       elif opcao == '2': #consulta por ID
            id_consulta = int(input('ID do funcionario: ')) 
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                   print(f"ID: {funcionario['id']}\n"
                      f"Nome: {funcionario['nome']}\n"
                      f"Setor: {funcionario['setor']}\n"
                      f"Salario: {funcionario['salario']}"
                      ) 
                   break
            else:
                print('ID INVÁLIDO')   
                
            
       elif opcao == '3': #consulta por setor
            setor_consulta = input('Setor do funcionario: ')
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == setor_consulta:
                    print(f"ID: {funcionario['id']}\n"
                      f"Nome: {funcionario['nome']}\n"
                      f"Setor: {funcionario['setor']}\n"
                      f"Salario: {funcionario['salario']}"
                      ) 

       elif opcao == '4': #para retornar ao MENU de opções
          return 
       else: #caso usuario digite opção inválida
          print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
          continue 
             
def remover_funcionario():     #função de remoção do cadastro do funcionario 
    while True:
        id_funcionario_remover = int(input('Digite o ID do funcionario a ser removido ou digite 0 (zero) para retornar ao menu principal: '))

        if id_funcionario_remover == 0: #se a entrada for 0, retorna ao menu principal
            return

        for funcionario in lista_funcionarios: #consulta o ID do funcionario e remove ele
            if funcionario['id'] == id_funcionario_remover:
                lista_funcionarios.remove(funcionario)
                print(f'Funcionario de ID {id_funcionario_remover} removido. ')
                break
        else: #mensagem de erro de ID inválido
            print('ID INVÁLIDO. TENTE NOVAMENTE')
            return
            
#menu principal
while True:
    print('QUAL OPÇÃO DESEJA')
    print('1. Cadastrar Funcionário')
    print('2. Consultar Funcionário')
    print('3. Remover Funcionário')
    print('4. Encerrar Programa')

    escolha_menu_principal = input("Escolha uma opção: ")

    if escolha_menu_principal == '1': #para cadastrar
        print('')
        cadastrar_funcionario(id_global + 1)

    elif escolha_menu_principal == '2': #para consulta
        print('')
        consultar_funcionarios()
    elif escolha_menu_principal == '3':  #para remover
        print('')
        remover_funcionario()
        
    elif escolha_menu_principal == '4': #para encerrar o programa - encerra o loops e printa mensagem
        print('')
        break

    else: #para opção invalida na entrada do menu
        print('Opção inválida')
        
