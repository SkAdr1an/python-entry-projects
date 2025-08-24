import random
import string

def gerar_senha(tamanho=15):
    """
    Gera uma senha forte com o tamanho especificado.
    
    Parâmetros:
    tamanho (int): O tamanho da senha gerada. O padrão é 15.

    Retorna:
    str: A senha gerada.
    """
    if tamanho < 8:
        raise ValueError("A senha deve ter pelo menos 8 caracteres.")
    
    caracteres_maiusculos = string.ascii_uppercase
    caracteres_minusculos = string.ascii_lowercase
    digitos = string.digits
    caracteres_especiais = string.punctuation

    todos_caracteres = caracteres_maiusculos + caracteres_minusculos + digitos + caracteres_especiais

    senha = [
        random.choice(caracteres_maiusculos),
        random.choice(caracteres_minusculos),
        random.choice(digitos),
        random.choice(caracteres_especiais)
    ]

    senha += random.choices(todos_caracteres, k=tamanho - len(senha))

    random.shuffle(senha)

    return ''.join(senha)

if __name__ == "__main__":
    tamanho_desejado = 16  # Você pode definir o tamanho desejado aqui
    senha_gerada = gerar_senha(tamanho=tamanho_desejado)
    print(f"Senha gerada: {senha_gerada}")
