import getpass
import hashlib

def ler_arquivo_texto(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        print(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    return conteudo

def hash_senha(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()


def main():
    
    caminho_arquivo = r"./password.txt"

    senha = hash_senha(ler_arquivo_texto(caminho_arquivo))    

    senha_tentativa = getpass.getpass("Digite senha: ")

    if hash_senha(senha_tentativa) == senha:
        print("\nSenha correta!")
        
    else:
        print("\nSenha incorreta!")

if __name__ == "__main__":
    main()
