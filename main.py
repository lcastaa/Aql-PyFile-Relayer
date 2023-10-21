# main.py
import Receiver
import Relayer
from utils import Printer


def main():
    Printer.print_header('       * Aql PyFile Relayer *')
    options = ['Relayer Mode', 'Receiver Mode', 'Exit']
    Printer.print_menu(options)
    user_choice = Printer.prompt_for_int('Your Mode Selection: ')
    if user_choice == 1:
        destination_ip = Printer.prompt_for_input("Enter HOST IP of RECEIVER: ")
        start_relayer("http://" + destination_ip + ":5001/receive")
    if user_choice == 2:
        start_receiver()
    elif user_choice == 3:
        exit(233)


def start_relayer(destination_ip):
    Relayer.destination_ip = destination_ip
    Relayer.app.run(host='0.0.0.0', port=5000)


def start_receiver():
    Receiver.app.run(host='0.0.0.0', port=5001)


if __name__ == '__main__':
    main()
