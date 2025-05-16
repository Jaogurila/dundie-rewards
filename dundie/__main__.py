import sys
import os
#teste inicial para a passagem de argumentos 
def main():
    print("INICIALIZANDO MAIN...")

    if len(sys.argv) < 3:
        print("Uso correto: dundiegur argumento1 argumento2")
        sys.exit(1)

    primeiro_comando = sys.argv[1]
    segundo_comando = sys.argv[2]
    try:
        if primeiro_comando == "load":
            with open(segundo_comando, "a") as arquivo:
                arquivo.write("100 PONTOS\n")
                print("PONTOS ADICIONADOS COM SUCESSO!")
        else: 
            print("NAO FOI POSSIVEL ADICIONAR PONTOS:")
    except Exception as e:
        print(f"ERRO: {e}")









if __name__ == "__main__":
    main()