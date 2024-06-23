import netifaces
from termcolor import colored


def get_ipv4_list():
    list_of_interfaces = netifaces.interfaces()  # zwraca listę nazw interfejsów

    list_of_ipv4 = []  # finalna lista adresów

    # pętla przeszukująca interfacy
    for interface_name in list_of_interfaces:
        interface_info = netifaces.ifaddresses(interface_name)  # zapisuje info o pojedyńczym interfejsie
        for number in interface_info:  # pętla pokazuje wartości w poszczególnych indexach
            if 'addr' in interface_info[number][0].keys():

                # sprawdzanie poprawności adresu
                if len(interface_info[number][0]['addr']) <= 15 and ':' not in interface_info[number][0]['addr']:
                    list_of_ipv4.append(interface_info[number][0]['addr'])
            else:
                print('addr not exist')
    return list_of_ipv4


print(colored("Final ipv4 array:", color="green", force_color=True))
print(get_ipv4_list())
