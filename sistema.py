import re
import json
import os

ARQUIVOS_DADOS = "usuarios.json"
usuarios = []

def carregar_dados():
    global usuarios
    if os.path.exists(ARQUIVOS_DADOS):
        try:
            with open(ARQUIVOS_DADOS, "r", encoding= "utf-8") as f:
                usuarios = json.load(f)
        except:
            usuarios = []
    else: 
        usuarios = []

def salvar_dados():
    try:
        with open (ARQUIVOS_DADOS, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii= False)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def menu():
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Editar usuário")  # <-- Nova opção!
    print("5 - Remover usuário")
    print("6 - Sair")

def editar_usuario(): 
    if not usuarios:
        print("\n Ainda não tem nada há ser editado.")
        return
    
    while True:
        email_busca = input("\Digite o email do usuário que deseja editar ou 'sair: ").strip().lower()
        if email_busca == 'sair':
            return
        
        usuario_encontrado = None
        for u in usuarios:
            if u['email'] == email_busca:
                usuario_encontrado = u
                break

        if usuario_encontrado:
            break
        else:
            print("\nUsuário não encontrado! Tente novamente ou digite 'sair'.")

    print(f"Edição de: {usuario_encontrado['nome']} ")

    while True:
            novo_nome = input(f"Digite o novo nome [{usuario_encontrado['nome']}]: ").strip()
            if not novo_nome:
                break
            if re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]{2,}$', novo_nome):
                usuario_encontrado['nome'] = novo_nome
                break
            print("Nome inválido!")

    while True: 
            nova_idade_str = input(f"Digite a nova idade [{usuario_encontrado['idade']}]: ").strip()
            if not nova_idade_str:
                break
            try:
                nova_idade = int (nova_idade_str)
                if 0 <= nova_idade <= 120:
                    usuario_encontrado['idade'] = nova_idade
                    break
                print("Idade entre 0 e 120.")
            except ValueError:
                print("Digite um número.")

    while True:
            novo_email = input(f"Novo email [{usuario_encontrado['email']}]: ").strip().lower()
            if not novo_email:
                break
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', novo_email):
                ja_existe = any (u['email'] == novo_email for u in usuarios if u != usuario_encontrado)
                if ja_existe:
                    print("Email já cadastrado em outra conta!")
                else:
                    usuario_encontrado['email'] = novo_email
                    break
            else: 
                print("Email inválido!")

    salvar_dados()
    print("\n Dados atualizados!")
            
    

        
def cadastrar_usuario():
    print("\n------ Novo cadastro ------")
    while True:
        nome = input("\nDigite o nome do usuário: ").strip()
        if re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]{2,}$', nome):
            break
        print("Nome inválido! Use pelo menos duas letras.")

    while True:
        try: 
            idade = int(input("\nDigite a idade: "))
            if 0 <= idade <= 120:
                break
            else: 
                print("Erro: A idade deve ser entre 0 e 120")
                
        except ValueError: 
            print("Erro: a idade tem que ser um número inteiro.")
            
         
         
    while True: 
        email = input("\nDigite seu email: ").strip().lower()
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            print("Formato do email inválido!")
            continue
        if any (u['email'] == email for u in usuarios): 
            print("Este email já está cadastrado!")
            continue
        break

    novo_usuario = {"nome": nome, "email": email, "idade": idade}
    usuarios.append(novo_usuario)
    salvar_dados() #Salva o usuario cadastrado no arquivo .json criado
    print("Usuário cadastrado com sucesso!")



def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    print("\n--- Lista de Usuários ---")
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. Nome: {u['nome']} | Email: {u['email']} | Idade: {u['idade']}")


def buscar_usuarios():
    termo = input("\nDigite o nome ou email para buscar: ").lower()
    encontrados = [u for u in usuarios if termo in u['nome'].lower() or termo in u['email'].lower()]
    
    if encontrados:
        print(f"\n {len(encontrados)} usuário(s) encontrado(s):")
        for u in encontrados:
            print(f"-> Nome: {u['nome']} | Email: {u['email']}")
    else:
        print("Nenhum usuário corresponde à busca.")


def remover_usuarios():
    if not usuarios:
        print("Não há usuários cadastrados para remover.")
        return
    
    while True:

        email_remover = input("\nDigite o EMAIL exato do usuário que deseja remover (ou sair): ").strip().lower()
        if email_remover == "sair":
            break

        usuario_encontrado = None
        for u in usuarios:
            if u["email"] == email_remover: 
                usuario_encontrado = u
                break
    
        if usuario_encontrado: 
            usuarios.remove(usuario_encontrado)
            salvar_dados()
            print(f"Usuário {email_remover} removido com sucesso!")
            opcao = input("\nDeseja remover outro? (s/n): ").lower()
            if opcao != "s":
                break
        else:
            print("Email não encontrado no sistema tente novamente.")
    


def main(): 
        carregar_dados()
        while True: 
            menu()
            op = input("\nDigite a opção desejada: ")
            if op == "1": cadastrar_usuario()
            elif op == "2": listar_usuarios()
            elif op == "3": buscar_usuarios()
            elif op == "4": editar_usuario() 
            elif op == "5": remover_usuarios()
            elif op == "6": break
            else: print("Opção inválida!")
                        
if __name__ == "__main__":
    main()