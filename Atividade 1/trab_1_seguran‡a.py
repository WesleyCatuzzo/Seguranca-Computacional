from Crypto.Cipher import DES

def encrypt(text, key, cipher_type):
    if cipher_type == "DES":
        des_cipher = DES.new(key, DES.MODE_ECB)
        return des_cipher.encrypt(pad_text(text))
    else:
        raise ValueError("Opção inválida")

def pad_text(text):
    padding_size = 8 - len(text) % 8
    padding = chr(padding_size) * padding_size
    return text + padding.encode()

def main():


        key = input("Digite a chave de criptografia: ")
        if len(key) != 8:
            print("A chave deve ter 8 caracteres")
            return
        input_type = input("Digite '1' para inserir o texto ou '2' para ler arquivo: ")
        if input_type == "1":
            text = input("Digite o texto a ser criptografado: ").encode()
        elif input_type == "2":
            file_name = input("Digite o nome do arquivo: ")
            with open(file_name, "rb") as f:
                text = f.read()
                print("Mensagem Lida: ", text)
        else:
            print("Opção inválida!")
            return
        encrypted_text = encrypt(text, key.encode(), "DES")
        print("Texto criptografado: ", encrypted_text.hex())


if __name__ == "__main__":
    main()