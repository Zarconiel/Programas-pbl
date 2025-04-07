# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet (como por exemplo códigos gerados por IA). 
# Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.



# Relatório de quantidade de passagens
qttde_passagens_padrao = 0
qttde_passagens_social_ = 0
qttde_passagens_estudante_idoso = 0

recarga_p=0
recarga_e=0
recarga_s=0

passagens_usadas_social = 0
passagens_usadas_estudante = 0
passagens_usadas_padrao = 0
passagens_usadas_padrao=0

#======================INICIO===============================#
# Solicitação do valor da passagem
valor_da_passagem = input("Insira o valor da passagem: ").strip()
while not valor_da_passagem.replace(".", "", 1).isdigit() or float(valor_da_passagem) <= 0:
    print("Entrada inválida! Digite um número maior que zero.")
    valor_da_passagem = input("Insira o valor da passagem: ").strip()
valor_da_passagem = float(valor_da_passagem)

# Menu principal
escolha = ''
while escolha != '0':
    print("\nMENU:")
    print('[1] Recarga de passagens')
    print('[2] Embarque de ônibus')
    print('[3] Compra de passagem')
    print('[4] Relatório')
    print('[0] Sair')

    escolha = input("Digite o número da opção desejada: ").strip()

#======================RECARGA DE PASSAGENS===============================#

    if escolha == '1':
        print("\n=== Recarga de Passagens ===")
        print("Escolha seu tipo de usuário:")
        print("[1] Padrão")
        print("[2] Estudante/Idoso")
        print("[3] Social")

        tipo_de_usuario = input("Escolha seu tipo de usuário (1, 2 ou 3): ").strip()
        while not tipo_de_usuario.isdigit() or int(tipo_de_usuario) < 1 or int(tipo_de_usuario) > 3:
            print("Opção inválida! Tente novamente.")
            tipo_de_usuario = input("Escolha seu tipo de usuário (1, 2 ou 3): ").strip()
            
#================USUARIO/PADRAO==================#
        if tipo_de_usuario == '1':
            categoria = 'Padrão'
            print(f"Tipo de usuário {categoria}, Valor da passagem: R${valor_da_passagem:.2f}")
            qttde_passagens = input("Quantas passagens deseja recarregar?: ").strip()
            while not qttde_passagens.isdigit() or int(qttde_passagens) <= 0:
                print("Opção inválida! Tente novamente.")
                qttde_passagens = input("Quantas passagens deseja recarregar?: ").strip()
            qttde_passagens = int(qttde_passagens)
            qttde_passagens_padrao += qttde_passagens
            recarga_p += qttde_passagens

#================USUARIO/ESTUDANTE==================#
        elif tipo_de_usuario == '2':
            categoria = 'Estudante/Idoso'
            print(f"Tipo de usuário {categoria}, Valor da passagem: R${valor_da_passagem / 2:.2f}")
            qttde_passagens = input("Quantas passagens deseja recarregar?: ").strip()
            while not qttde_passagens.isdigit() or int(qttde_passagens) <= 0:
                print("Opção inválida! Tente novamente.")
                qttde_passagens = input("Quantas passagens deseja recarregar?: ").strip()
            qttde_passagens = int(qttde_passagens)
            qttde_passagens_estudante_idoso += qttde_passagens
            recarga_e += qttde_passagens

#================USUARIO/SOCIAL==================#
        elif tipo_de_usuario == '3':
            categoria = 'Social'
            print(f"Tipo de usuário {categoria}, Valor da passagem: R${valor_da_passagem - (valor_da_passagem * 0.80):.2f}")
            qttde_passagens = input("Quantas passagens deseja recarregar?: ").strip()
            while not qttde_passagens.isdigit() or int(qttde_passagens) <= 0:
                print("Opção inválida! Tente novamente.")
                qttde_passagens = input("Quantas passagens deseja recarregar?: ").strip()
            qttde_passagens = int(qttde_passagens)
            qttde_passagens_social_ += qttde_passagens
            recarga_s += qttde_passagens

        print("\n=== Passagem recarregada com sucesso! ===")


#======================VALIDAÇAO DE EMBARQUE===============================#
    elif escolha == '2':
        print("\n=== Validação de Embarque ===")
        print("Escolha seu tipo de usuário:")
        print("[1] Padrão")
        print("[2] Estudante/Idoso")
        print("[3] Social")

        tipo_de_usuario = input("Escolha seu tipo de usuário (1, 2 ou 3): ").strip()
        while not (tipo_de_usuario == '1' or tipo_de_usuario == '2' or tipo_de_usuario == '3'):
            print("Opção inválida! Tente novamente.")
            tipo_de_usuario = input("Escolha seu tipo de usuário (1, 2 ou 3): ").strip()



#======================USUARIO PADRAO===============================#
        if tipo_de_usuario == '1':
            if qttde_passagens_padrao > 0:
                print(f"\n=== Você tem {qttde_passagens_padrao} passagens, pode embarcar! ===")
                
            else:
                print("\n=== Saldo insuficiente para embarcar. Por favor, recarregue sua passagem. ===")


#======================USUARIO ESTUDANTE===============================#
        elif tipo_de_usuario == '2':
            if qttde_passagens_estudante_idoso > 0:
                print(f"\n=== Você tem {qttde_passagens_estudante_idoso} passagens, pode embarcar! ===")
                
            else:
                print("\n=== Saldo insuficiente para embarcar. Por favor, recarregue sua passagem. ===")



#======================USUARIO IDOSO===============================#
        elif tipo_de_usuario == '3':
            if qttde_passagens_social_ > 0:
                print(f"\n=== Você tem {qttde_passagens_social_} passagens, pode embarcar! ===")
                
            else:
                print("\n=== Saldo insuficiente para embarcar. Por favor, recarregue sua passagem. ===")


    #//=================COMPRA DE PASSAGENS=======================//
    elif escolha == '3':
        print("\n=== Compra de passagens ===")
        print("Escolha seu tipo de usuário:")
        print("[1] Padrão")
        print("[2] Estudante/Idoso")
        print("[3] Social")

        tipo_de_usuario = input("Escolha seu tipo de usuário (1, 2 ou 3): ").strip()
        while not (tipo_de_usuario == '1' or tipo_de_usuario == '2' or tipo_de_usuario == '3'):
            print("Opção inválida! Tente novamente.")
            tipo_de_usuario = input("Escolha seu tipo de usuário (1, 2 ou 3): ").strip()



#======================USUARIO PADRAO===============================#
        if tipo_de_usuario == '1':
            categoria = 'Padrão'
            print(f"\n=== Tipo de usuário {categoria}, você tem: {qttde_passagens_padrao} passagens ===")

            passagens_usadas_padrao = input('Quantas passagens deseja usar?: ').strip()
            while not passagens_usadas_padrao.isdigit() or int(passagens_usadas_padrao) < 0:
                print("Resposta inválida! Por favor, insira um número válido.")
                passagens_usadas_padrao = input('Quantas passagens deseja usar?: ').strip()
            passagens_usadas_padrao = int(passagens_usadas_padrao)
            


            if passagens_usadas_padrao > 0 and passagens_usadas_padrao <= qttde_passagens_padrao:
                qttde_passagens_padrao -= passagens_usadas_padrao
                print(f'{passagens_usadas_padrao} passagem(ns) comprada(s) com sucesso!')
            elif passagens_usadas_padrao == 0:
                print('Nenhuma passagem comprada.')
            else:
                print('Número de passagens superior ao saldo disponível. Tente novamente.')



#======================USUARIO ESTUDANTE===============================#
        elif tipo_de_usuario == '2':
            categoria = 'Estudante/Idoso'
            print(f"\n=== Tipo de usuário {categoria}, você tem: {qttde_passagens_estudante_idoso} passagens ===")

            passagens_usadas_estudante = input('Quantas passagens deseja usar?: ').strip()
            while not passagens_usadas_estudante.isdigit() or int(passagens_usadas_estudante) < 0:
                print("Resposta inválida! Por favor, insira um número válido.")
                passagens_usadas_estudante = input('Quantas passagens deseja usar?: ').strip()

            passagens_usadas_estudante = int(passagens_usadas_estudante)

            if passagens_usadas_estudante > 0 and passagens_usadas_estudante <= qttde_passagens_estudante_idoso:
                
                print(f'{passagens_usadas_estudante} passagem(ns) comprada(s) com sucesso!')
            elif passagens_usadas_estudante == 0:
                print('Nenhuma passagem comprada.')
            else:
                print('Número de passagens superior ao saldo disponível. Tente novamente.')



#======================USUARIO SOCIAL===============================#
        elif tipo_de_usuario == '3':
            categoria = 'Social'
            print(f"\n=== Tipo de usuário {categoria}, você tem: {qttde_passagens_social_} passagens ===")

            passagens_usadas_social = input('Quantas passagens deseja usar?: ').strip()
            while not passagens_usadas_social.isdigit() or int(passagens_usadas_social) < 0:
                print("Resposta inválida! Por favor, insira um número válido.")
                passagens_usadas_social = input('Quantas passagens deseja usar?: ').strip()

            passagens_usadas_social = int(passagens_usadas_social)

            if passagens_usadas_social > 0 and passagens_usadas_social <= qttde_passagens_social_:
                
                print(f'{passagens_usadas_social} passagem(ns) comprada(s) com sucesso!')
            elif passagens_usadas_social == 0:
                print('Nenhuma passagem comprada.')
            else:
                print('Número de passagens superior ao saldo disponível. Tente novamente.')


#//=================RELATORIO=======================//
    elif escolha == "4":
        recarga_total= recarga_p + recarga_s + recarga_e
        print("\n=== Relatório ===")
        print("\n===recarga de usuarios===")
        print(f"Quantidade de recarga usauario/Social: {recarga_p}")
        print(f"Quantidade de recarga usauario/Etudante e idoso: {recarga_e}")
        print(f"Quantidade de recarga usauario/padrao: {recarga_s}")
        print(f"Total de recargas de passagens de todos os usuarios: {recarga_total}")
        
        print('-------------  --------------------------')
        compra_total = (passagens_usadas_estudante + passagens_usadas_padrao + passagens_usadas_social)
        print(f"Quantidade de passagens compradas usauario/padrao: {passagens_usadas_padrao}")
        print(f"Quantidade de passagens compradas usauario/Etudante e idoso: {passagens_usadas_estudante}")
        print(f"Quantidade de passagens compradas usauario/Social: {passagens_usadas_social}")
        print(f"Quantidade de passagens compradas total: {compra_total}")
        
        #--------------- -------------------------
        gasto_p= recarga_p * valor_da_passagem
        gasto_e=recarga_e * (valor_da_passagem/2)
        gasto_s= recarga_s* (valor_da_passagem - (valor_da_passagem*0.80))
        total_gasto= (gasto_s + gasto_e + gasto_p)
        print('-------------  --------------------------')
        print(f"valor total gasto com passagens usauario/padrao: R${(gasto_p):.2f}")
        print(f"valor total gasto com passagens usauario/Etudante e idoso: R${gasto_e}")
        print(f"valor total gasto com passagens usauario/Social: R${gasto_s}")
        print(f"valor total gasto com passagens: R${total_gasto}")
        #--------------- -------------------------
        recarga_t= (qttde_passagens_padrao + qttde_passagens_estudante_idoso + qttde_passagens_social_)
        print('-------------  --------------------------')
        print(f"Saldo restante de passagens usuario/padrao: {qttde_passagens_padrao}")
        print(f"Saldo restante de passagens usuario/Etudante e idoso: {qttde_passagens_estudante_idoso}")
        print(f"Saldo restante de passagens usuario/Social: {qttde_passagens_social_}")
        print(f"Total de Saldo restante de passagens  de todos os usuarios: {recarga_t}")

#//=================FFECHAR CODIGO=======================//
    elif escolha == "0":
        print("\nSaindo... Até logo!")
    else:
        print("Opção inválida! Tente novamente.")

