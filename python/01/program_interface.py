from utils import clear_terminal

def interface() -> None | dict:

    clear_terminal()

    while True:
        print("Simulação de cadastro de usuários\n")

        print("1. Cadastrar usuário")
        print("2. Sair do sistema")
        option = input("Escolha uma opção: ")

        match option:
            case "1":
                name = input("\nDigite o nome: ")
                
                while True:
                    try:
                        age = int(input("Digite a idade: "))

                        if ((age >= 0) and (age <= 100)):
                            break

                        print("Erro! Você precisa digitar uma idade entre 0 e 100.")

                    except ValueError:
                        print("Erro! Você precisa digitar uma idade válida.")
                
                while True:
                    email = input("Digite o email: ")

                    if (email.count("@") == 1):
                        email_split = email.split("@")

                        if (email_split[1].count(".") >= 1):
                            break
                        else:
                            print("Email inválido! O email deve conter um '.' após o '@'.")
                    else:

                        print("Email inválido! O email deve conter um (e apenas um) '@' em seu corpo.")
                
                while True:
                    admin = input("O usuário é admin (S/N)? ")

                    if (admin.upper() in ["S", "N"]):
                        break

                    print("Opção inválida! Escolha entre S e N.")

                return {"name": name, "age": age, "email": email, "admin": admin}
            
            case "2":
                print("\nSaindo do sistema...")
                return None

            case _:
                print("\nOpção inválida! Tente novamente...", end="")
                clear_terminal(sleep_seconds=2)
                continue