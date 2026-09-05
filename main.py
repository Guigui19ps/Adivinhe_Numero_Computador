def jogar():

    num_min = 1
    num_max = 100
    chute = (num_min + num_max) // 2
    tentativas = 0

    while True:

        tentativas += 1

        mostrar_chute(chute)

        resposta_chute = pegar_resposta(chute)

        if resposta_chute == "maior":
            num_min = chute + 1
            chute = (num_min + num_max) // 2

        elif resposta_chute == "menor":
            num_max = chute - 1
            chute = (num_min + num_max) // 2

        elif resposta_chute == "igual":
            print(f"Seu número é {chute}")
            print(f"Eu acertei seu número em {tentativas} tentativas")
            break


def pegar_resposta(chute):

    resposta_chute = input(f"seu número é maior, menor ou igual a {chute}? ").lower()

    while resposta_chute not in ["maior", "menor", "igual"]:
        print("Resposta inválida, digite maior, menor ou igual")
        resposta_chute = input(
            f"Seu número é maior, menor ou igual a {chute}? "
        ).lower()

    return resposta_chute


def iniciar_jogo():
    input(f"Pense em um número de 1 a 100; Assim que pensar dê enter no teclado ")


def mostrar_chute(chute):
    print(f"Meu chute é {chute}")


print(
    f"\nOlá, Bem-vindo ao jogo Adivinhe o número, onde eu tentarei adivinhar o número que voce está pensando e depois mostrarei em quantas tentativas eu adivinhei seu número\n"
)

resposta = input(
    "Vamos começar? (Digite sim para começar ou não para encerrar) ").lower()

if resposta == "sim":
    iniciar_jogo()
    jogar()

elif resposta == "não":
    print(f"Tudo bem, até a proxima")