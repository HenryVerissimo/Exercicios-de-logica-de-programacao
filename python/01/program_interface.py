from utils import clear_terminal

def interface() -> None | dict:

    clear_terminal(2)

    while True:
        print("Simulação de cadastro de usuários\n")

        print("1. Cadastrar usuário")
        print("2. Sair do sistema")
        option = input("Escolha uma opção: ")

        match option:
            case "1":
                while True:
                    name = input("\nDigite o nome: ")

                    if(len(name) >= 3):
                        break

                    print("Erro: O nome deve ter pelo menos 3 caracteres")
                
                while True:
                    try:
                        age = int(input("Digite a idade: "))

                        if ((age >= 18) and (age <= 100)):
                            break

                        print("Erro: Você precisa digitar uma idade entre 18 e 100.\n")

                    except ValueError:
                        print("Erro: A idade precisa ser um válor númerico.\n")
                
                while True:
                    email = input("Digite o email: ")

                    if (email.count("@") == 1):
                        email_split = email.split("@")

                        if (email_split[1].count(".") >= 1):
                            break
                        else:
                            print("Erro: Email inválido! O email deve conter um '.' após o '@'.\n")
                    else:

                        print("Erro: Email inválido! O email deve conter um (e apenas um) '@' em seu corpo.\n")
                
                while True:
                    admin = input("O usuário é admin (S/N)? ")

                    if (admin.upper() in ["S", "N"]):
                        break

                    print("Erro: Opção inválida! Escolha entre S e N.\n")

                return {"name": name, "age": age, "email": email, "admin": admin}
            
            case "2":
                print("\nSaindo do sistema...")
                return None

            case _:
                print("\nErro: Opção inválida! Tente novamente...", end="")
                clear_terminal(sleep_seconds=2)
                continue