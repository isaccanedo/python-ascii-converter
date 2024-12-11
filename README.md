# 🛠 Localizador de Valores ASCII

Este é um programa simples em Python que permite aos usuários encontrar os valores ASCII de caracteres ou strings que eles inserem. O programa é interativo e executa em um loop, permitindo que os usuários insiram dados continuamente sem reiniciar o script.

## Funcionalidades

- Aceita entrada dinâmica do usuário.
- Processa tanto caracteres únicos quanto strings completas.
- Exibe os valores ASCII de cada caractere na entrada.
- Permite que o usuário saia do programa a qualquer momento digitando `exit` ou `quit`.

## Uso

### Pré-requisitos

Certifique-se de ter o Python instalado no seu sistema. Este programa é compatível com Python 3.x.

### Executando o Programa

1. Clone o repositório ou baixe o script.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório que contém o script.
4. Execute o programa usando o comando:

   ```bash
   python python_ascii_converter.py
   ```

### Como Usar

1. Insira qualquer caractere ou string para ver seus valores ASCII.
2. O programa exibirá o valor ASCII de cada caractere na sua entrada.
3. Para sair do programa, digite `exit` ou `quit` e pressione Enter.

### Exemplo

#### Entrada:

```
Enter your input: Hello
```

#### Saída:

```
ASCII values:
Character: 'H' -> ASCII Value: 72
Character: 'e' -> ASCII Value: 101
Character: 'l' -> ASCII Value: 108
Character: 'l' -> ASCII Value: 108
Character: 'o' -> ASCII Value: 111
```

#### Saindo:

```
Enter your input: exit
Exiting the program. Goodbye!
```

## Código

O código completo do programa:

```python
# Programa para encontrar os valores ASCII de caracteres dados

def find_ascii_values():
    print("Insira caracteres ou strings para encontrar seus valores ASCII.")
    print("Digite 'exit' ou 'quit' para sair do programa.")

    while True:
        user_input = input("\nDigite sua entrada: ")

        if user_input.lower() in ('exit', 'quit'):
            print("Saindo do programa. Até logo!")
            break

        if not user_input:
            print("Você não digitou nada. Por favor, tente novamente!")
            continue

        print("\nValores ASCII:")
        for char in user_input:
            print(f"Caractere: '{char}' -> Valor ASCII: {ord(char)}")

if __name__ == "__main__":
    find_ascii_values()
```
