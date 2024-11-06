import os
from colorama import Fore, init

init(autoreset=True)

##Sistema de Cadastro
Cadastro = []

##Função para salvar cadastro
def salvar_cadastro(login, senha):
    with open('user_logins.txt', 'a') as arquivo:
        arquivo.write(f"{login}:{senha}\n")

##Função para ler os cadastros
def load_cadastros():
    try:
        with open('user_logins.txt', 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip().split(":", 1)
                if len(linha) == 2:
                    login, senha = linha
                    Cadastro.append({"login": login.strip(), "senha": senha.strip()})
    except FileNotFoundError:
        pass


load_cadastros()

log_sucess = False

while not log_sucess:
    print(" ")
    print(f"{Fore.YELLOW}╔══════════════════════════════════╗")
    print(f"{Fore.YELLOW}║      Sistema de Cadastro         ║")
    print(f"{Fore.YELLOW}║   1. Realizar Cadastro           ║")
    print(f"{Fore.YELLOW}║   2. Efetuar Login               ║")
    print(f"{Fore.YELLOW}║   3. Sair                        ║")
    print(f"{Fore.YELLOW}╚══════════════════════════════════╝")

    escolha = input(f"{Fore.CYAN}Escolha uma opção: ")

    ##Realizar Cadastro
    if escolha == '1':
        while True:
            login = input(f"{Fore.CYAN}Digite o login: ")
            senha = input(f"{Fore.CYAN}Digite a senha: ")
            if not login or not senha:
                print(f"{Fore.RED}Login e senha não podem estar vazios!")
                continue
            
            if len(senha) < 8:
                print(f"{Fore.RED}A senha deve ter pelo menos 8 caracteres!")
                continue
            
            salvar_cadastro(login, senha)
            Cadastro.append({"login": login, "senha": senha})
            print(f"{Fore.GREEN}Cadastro realizado com sucesso!")
            break

    ##Fazer Login
    elif escolha == '2':
        while True:
            login = input(f"{Fore.CYAN}Digite seu login: ")
            senha = input(f"{Fore.CYAN}Digite sua senha: ")

            if not login or not senha:
                print(f"{Fore.RED}Login e senha não podem estar vazios! Tente novamente.")
                continue 

            if len(senha) < 8:
                print(f"{Fore.RED}A senha deve ter pelo menos 8 caracteres!")
                continue

            for usuario in Cadastro:
                if usuario["login"] == login and usuario["senha"] == senha:
                    print(f"{Fore.GREEN}Login realizado com sucesso!")
                    log_sucess = True
                    break
            else:
                print(f"{Fore.RED}Login ou senha incorretos!")
            break

    ##Sair do sistema
    elif escolha == '3':
        print(f"{Fore.YELLOW}Saindo...")
        break

    ##Opção inválida
    else:
        print(f"{Fore.RED}Opção inválida! Tente novamente.")    