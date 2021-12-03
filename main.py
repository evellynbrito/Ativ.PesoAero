
print('olá')
print('se a aeronave estiver com mais de 250 horas de voo, selecione a opção abaixo')
print('digite 1 para opção recachutagem.')
print('digite 2 para opção reciclagem.')
print('digite 3 para sair.')

opcao = int(input('digite sua escolha:'))

if opcao == 1:
    print('recauchutagem')
elif opcao == 2:
    print('reciclagem')
elif opcao == 3:
    print('saindo...')
    exit()
else:
    print('opção invalida')
