import os

def find_downloads_folder():
    user_home = os.path.expanduser("~")  # Caminho para a pasta do usuário (diretório home)
    downloads_folder = os.path.join(user_home, "Downloads")  # Combinar o caminho com "Downloads"
    
    if os.path.exists(downloads_folder):  # Verificar se a pasta "Downloads" existe
        return downloads_folder
    else:
        print("Pasta Downloads não encontrada.")
        return None

downloads_folder_path = find_downloads_folder()

if downloads_folder_path:
    print(f"Caminho para a pasta Downloads: {downloads_folder_path}")