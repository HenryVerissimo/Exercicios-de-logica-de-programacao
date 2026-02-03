from typing import Dict, List

DATA_SET: List[dict]  = []

def create_user_data(user: Dict[str, str | int]) -> None:
    try:
        if ((type(user["name"]) is not str) or (len(user["name"]) < 3)):
            print("Erro: o nome do usuário é inválido!")

        elif ((type(user["age"]) is not int) or (user["age"] < 18) or (user["age"] > 100)):
            print("Erro: a idade do usuário é inválida!")
        
        elif ((type(user["email"]) is not str) or (user["email"].count("@") != 1) or (user["email"].split("@")[1].count(".") < 1)):
            print("Erro: o email do usuário é inválido!")

        elif ((type(user["admin"]) is not str) or (user["admin"].upper() not in ["S", "N"])):
            print("Erro: não foi possível identificar se o usuário é admin!")

        else:
            DATA_SET.append(user)

            if (user["admin"].upper() == "S"):
                print(f"\nCadastro realizado com sucesso! bem vinda, administrador(a) {user["name"]}.")
            
            else:
                print("\nCadastro realizado com seucesso!")

            return

    except Exception:
        print("Erro: existem dados inválidos no registro!\n")

    print("Dados não salvos!\n")