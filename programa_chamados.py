import re #PARA A VERIFICAÇÃO DA SENHA 
import time #PARA UMA PEQUENA IMERSÃO NO USO DO CODIGO SEM O FRONT
import random #PARA GERAR UM NUMERO ALEÁTORIO
usuarios = [] #ESSA LISTA ARMAZENA DICIONÁRIOS CONTENDO LOGIN E SENHA
usuariosAdministradores = [] #É UMA CAMADA DE ACESSO, IMPÕE UM REQUISITO PARA ITENS DE USUARIOS[] ENTRAR AQUI
chamados = [] #ARMAZENA DICIONÁRIOS COM DEPARTAMENTO, TITULO E CORPO DO CHAMADO


def validar_senha(senha):
    #VERIFICA SE A SENHA ATENDE AOS REQUISITOS.
    return (re.search(r'.{8,}', senha) and
            re.search(r'[A-Z]', senha) and
            re.search(r'\d', senha) and
            re.search(r'[!@#$%¨&*]', senha))

def cadastrar_senha():
    #SOLICITA E VALIDA A SENHA DO USUÁRIO.
    print("CADASTRE A SUA SENHA COM OS SEGUINTES REQUISITOS:\n"
          "- Pelo menos 8 caracteres\n"
          "- Pelo menos uma letra maiúscula\n"
          "- Pelo menos um número\n"
          "- Pelo menos um dos seguintes caracteres especiais: (!@#$%¨&*)\n")
    
    while True:
        novaSenha = input("Digite sua senha: ")
        if validar_senha(novaSenha):
            print("SENHA CADASTRADA COM SUCESSO.")
            return novaSenha  #RETORNA A SENHA JÁ VERIFICADA PARA SER USADA NA LISTA USUARIOS
        else:
            print("SENHA INVÁLIDA! Tente novamente seguindo os critérios.")

def adicionarUsuario(usuarios):#FUNÇÃO QUE ADICIONA USUARIOS 
    entradaEmail = input("DIGITE O SEU E-MAIL:  ").strip().lower() #VERIFICA SE O EMAIL TEM O SUFIXO QUE O SISTEMA ACEITA
    posicao = entradaEmail.find("@")#PROCURA A PARTE QUE IREI VALIDA
    servidor = entradaEmail[posicao+1:]#SEPARA A PARTE QUE IREI VALIDAR
    if servidor == "gmail.com" or "hotmail.com" or "outlook.com" or "icloud.com": #FAZ A VALIDAÇÃO
        email = entradaEmail# SE PASSAR PELA VALIDAÇÃO A VARIAVEL EMAIL RECEBE O VALOR DE ENTRADA
    else:
        print("FORMATO INVALIDO, TENTE NOVAMENTE.")#INTERAÇÃO COM O USÁRIO, RETORNA AO INICIO DA FUNÇÃO
        return
    
    novaSenha = cadastrar_senha() #CHAMA A FUNÇÃO PARA CRIAÇÃO DA SENHA

    novoUsuario ={
        "login": email, #PREENCHE O DICIONÁRIO DE LOGIN
        "senha": novaSenha #PREENCHE A SENHA
    }
    usuarios.append(novoUsuario)
    time.sleep(1)
    print ("USUÁRIO ADICIONADO COM SUCESSO, ACESSE A OPÇÃO DE ACESSO PARA REALIZAR ALGUMA AÇÃO.") #MOSTRA QUE DEU TUDO CERTO


#FUNÇÕES DE CHAMAR O MENU
def mostrarChamados(chamados): #PRINTA O MENU
    print (chamados)

def novoChamado (chamados): #CAPTA A ENTRADA DOS USUÁRIOS E GERA O ID DELE PELO METODO DO RANDOM
    print ("SUPORTE, TI, GESTÃO DE PESSOAS, GENÉRICO.")
    titulo = input ("DOS INTENS LISTADOS ACIMA, QUAL MAIS SE ENCAIXA AO SEU PROBLEMA? \n")
    assunto = input ("DESCREVA EM POUCAS PALAVRAS QUAL SERIA O POSSIVEL PROBLEMA.")
    corpo = input ("DIGITE DETALHADAMENTE QUAL SERIA O SEU PROBLEMA: ")
    id = random.randint(1000,9999)

    novoChamado = { #ADICIONA OS DADOS DE ENTRADA NUM NOVO DICIONÁRIO
        "ID": id,
        "DEPARTAMENTO": titulo,
        "TITULO": assunto,
        "MENSAGEM/INTERAÇÃO": corpo
    }
    chamados.append(novoChamado) #ADICIONA O DICIONÁRIO RECEM CRIADO NA LISTA CHAMADOS

def tornarAdministrativo(login, usuariosAdministradores): #ATENDE REQUISITOS BASICOS PARA O USUÁRIO SE TORNAR UM USUÁRIO MASTER
    print ("DIGITE A SEGUIR A SENHA MASTER PARA TORNAR SEU USUÁRIO UM USUÁRIO ADMINISTRADOR. \n")
    time.sleep(1)
    key = "ciberbatutinha"
    keyUsuario = input ("DIGITE A SENHA: ")
    if keyUsuario == key:
        loginMaster = { #IMPORTANTE, MUDAR ISSO, CRIAR UMA NOVA LISTA E TIRAR O USUÁRIO MASTER DA LISTA DE USUÁRIO COMUM.
            "EMAIL_MASTER": login 
        }
        usuariosAdministradores.append(loginMaster)
        print ("PARABÉNS AGORA VOCÊ É UM USUÁRIO ADMINISTRADOR. ")
        print ("VOLTANDO PARA O MENU PRINCIPAL. ")
        time.sleep(2)
        menuPrincipal()

def finalizarChamado(chamados): #O FINALIZAR CHAMADO REMOVE O CHAMADO, MAS FUTURAMENTE IREI MOVER ELE PARA UMA NOVA LISTA OU ITEM.
    print (chamados)
    fimChamado = int (input ("DIGITE SOMENTE, E EM NUMEROS O ID DO CHAMADO QUE DESEJA FINALIZAR."))
    for chamado in chamados:
        if fimChamado == chamado["ID"]:
            chamados.remove(chamado)
            print (f"O CHAMADO DE ID: {fimChamado} FOI FINALIZADO COM SUCESSO!")
        else:
            print ("CHAMADO NÃO ENCONTRADO. ")


def menuUsuario(login, usuariosAdministradores): #ESSE É O MENU DO USUÁRIO, CHAMA ALGUMAS FUNÇÕES
    while True: #MANTEM O USUÁRIO EM LOOP ATÉ OCORRER UMA CONDIÇÃO
        print("""
        1 - Mostrar chamados
        2 - Abrir novo chamado
        3 - Tornar-se administrativo
        4 - Voltar para o menu principal
        """)
        opcao = input ("DIGITE A OPÇÃO DESEJADA: ")
        if opcao == "1":
            mostrarChamados(chamados)
        elif opcao == "2":
            novoChamado (chamados)
        elif opcao == "3":
            tornarAdministrativo(login, usuariosAdministradores)
        elif opcao == "4":
            break
        else:
            print("OPÇÃO INVALIDA, TENTE NOVAMENTE !")

def menuUsuarioMaster(): #ESSE É O MENU DO USUÁRIO MASTER, TEM ALGUMAS FUNÇÕES A MAIS
    while True: #MANTEM O USUÁRIO EM LOOP ATÉ OCORRER UMA CONDIÇÃO
        print("""
        BEM VINDO AO MENU DO USUÁRIO MASTER.
        DIGITE 1. PARA ACESSAR OS CHAMADOS. 
        DIGITE 2. PARA ABRIR UM NOVO CHAMADO. 
        DIGITE 3. PARA FINALIZAR CHAMADOS APÓS RESOLVIDOS. 
        DIGITE 4. PARA RETORNAR AO MENU PRINCIPAL.
        """)

        opcao = input("DIGITE A OPÇÃO DESEJADA: ")

        if opcao == "1":
            mostrarChamados(chamados)
        elif opcao == "2":
            novoChamado(chamados)
        elif opcao == "3":
            finalizarChamado(chamados)
        elif opcao == "4":
            print("Retornando ao menu principal...")
            break  # Sai do loop para retornar ao menu principal
        else:
            print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")

def verificarUsuario(usuarios): #VERIFICA SE O USUÁRIO EXISTE E QUAL TIPO DELE, PRINTA INFORMANDO SE É UM USUÁRIO COMUM OU MASTER
    if not usuarios:
        print("AINDA NÃO HÁ RESGISTROS POR AQUI") #RETORNA ESSA MENSAGEM SE A LISTA DE USUÁRIO ESTARÁ VAZIA
        time.sleep(2)
    else:
        print ("DIGITE AS SUAS CREDENCIAS ABAIXO PARA ACESSAR O SISTEMA.\n") #SE NÃO ESTIVER VAZIA RETORNA UMA ESTRUTURA DE REPETIÇÃO QUE VERIFICA QUAL TIPO DE USUÁRIO O CLIENTE É
        time.sleep(1)
        login = input ("DIGITE O SEU E-MAIL: ") #ENTRADA DE DADOS
        senha = input ("DIGITE A SUA SENHA: ")   #ENTRADA DE DADOS
        for user in usuarios: #PERCORRE AS DUAS LISTAS E VERIFICA QUAL TIPO O USUARIO É, DEPENDENDO DO TIPO CHAMA UM MENU DIFERENTE
            if user["login"] == login and user["senha"] == senha:
                print ("VOCÊ É UM USUÁRIO.") 
                time.sleep(2)
                menuUsuario()
                return
        for admin in usuariosAdministradores:
            if admin["EMAIL_MASTER"] == login:
                print ("VOCÊ É ADMINISTRADOR. ")
                time.sleep(2)
                menuUsuarioMaster()
                return
            
        print ("USUÁRIO NÃO ENCONTRADO. ")



def menuPrincipal():
    while True:
    #CRIA UM LOOP ATÉ QUE A CONDIÇÃO SE SATISFAÇA
        print ()
        print ("====================================")
        print ("                MENU                ")
        print ("====================================")
        print ()
        time.sleep(1)
        print ("DIGITE 1. PARA ACESSAR O SEU USUÁRIO.\n")
        print ("DIGITE 2. PARA CRIAR UM NOVO USUÁRIO.\n")
        print ("DIGITE 3. PARA SAIR.")

        opcao = input ("DIGITE A OPÇÃO QUE DESEJA ACESSAR.\n")

        if opcao == "1":
            verificarUsuario(usuarios)#ESSA FUNÇÃO CARREGA QUASE TODA A LOGICA DO PROGRAMA 
        elif opcao == "2":
            adicionarUsuario(usuarios)
        elif opcao == "3":
            break
        else:
            print("O NÚMERO QUE ESCOLHEU NÃO CORRESPONDE A NENHUMA OPÇÃO, POR FAVOR, TENTE NOVAMENTE.")
    #CASO O USUARIO JÁ TENHA LOGIN E SENA ATIVO, ELE CONSEGUE ACESSAR A ABA DE CHAMADOS NELA CONTEM: MEUS CHAMADOS, NOVO CHAMADO, CHAMADOS FINALIZADOS.
    #CASO O USUARIO FAÇA O LOGIN AGORA, MANDAR UMA MENSAGEM MOSTRANDO QUE DEU TUDO CERTO E RETORNANDO PARA O MENU.

menuPrincipal()
