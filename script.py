from settings import *

def openFile(user_input):
    list = glob.glob(directories[int(user_input)], recursive=True)
    try:
        # files = [ file for file in list if file.endswith( ('.mkv', '.mp4', '.wmv', '.mov', '.avi', '.mpg', '.mpeg', '.webm', '.flv', '.m4v') ) ]
        files = [ file for file in list if not file.endswith( ('.jpg', '.png', '.jpeg', '.zip', '.rar') ) ]
        file = files[random.randint(0, len(files) - 1)]
        print("Iniciando sessão de: " + file)
        os.startfile(file)
    except:
        print("Não foi possível abrir nenhum arquivo. O diretório pode não conter arquivos válidos")
        random_directory()

def select_directory():
    # try:
        print(f"Olá, selecione uma opção de diretório:\n(0) {directories[0]}\n(1) {directories[1]}\n(2) {directories[2]}\n:\n\n")
        openFile(input())
    # except:
    #     # print("Erro ao selecionar opção. Verifique se todos os repositórios foram adicionados")

def random_directory():
    openFile(random.randint(0, len(directories) - 1))

def switch():
    print("Olá, qual método de seleção você deseja utilizar:\n(1) Seleção de diretório específico\n(2) Seleção aleatória:\n(3) Repetição aleatória:\n(4) Repetição de diretório:\n")
    user_input = input()
    if user_input == "1":
        select_directory()
    elif user_input == "2":
        random_directory()
    elif user_input == "3":
        print("Quantos:\n")
        windows = int(input())
        number = 0
        for number in range(windows):
            random_directory()
    elif user_input == "4":
        
        # print("Quantos:\n")
        print(f"Olá, selecione quantos e uma opção de diretório:\n(0) {directories[0]}\n(1) {directories[1]}\n(2) {directories[2]}\n:\n\n")
        windows = int(input())
        number = 0
        directory = input()
        for number in range(windows):
            openFile(directory)

    elif user_input == "0":
        return 0
    else: 
        print("Seleção inválida")
        switch()

if __name__ == "__main__":
    directories = [
        DIRECTORY_A,
        DIRECTORY_B,
        DIRECTORY_C
    ]

    switch()