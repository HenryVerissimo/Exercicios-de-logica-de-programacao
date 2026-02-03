from program_interface import interface
from process_data import create_user_data

def main() -> None:

    while True:
        data = interface()

        if data is None:
            return
        
        create_user_data(user=data)


if __name__ == "__main__":

    main()