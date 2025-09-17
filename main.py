import pandas as pd
from datetime import datetime as dt
from tabulate import tabulate as tb


#df = pd.read_csv("produtos.csv")
#df.columns = ["Id", "Produto", "Estoque", "Preço"]
#print(df)

LISTA_PRODUTOS = ["mock", "mock2", "mock3", "mock4"]
PRODUTOS_SELECIONADOS=[]


def menu():
    print("=== CAIXA ABERTO ===\n")
    lista_cliente = []
    indice_cliente = 0
    while(True):
        indice_cliente+=1
        lista_cliente.append(f"Cliente {indice_cliente}")
        print(lista_cliente[indice_cliente-1]) #Cliente 1
        print("-> Iniciar atendimento")
        menu_produtos()


def menu_produtos():
    #print() MOSTRAR UMA TABELA COM ID/NOME/PREÇO
    id = int(input("Digite o código produto escolhido: "))
    verifica_id(id)
    qtd = int(input("Digite a quantidade desejada: "))
    verifica_quantidade(qtd)

    PRODUTOS_SELECIONADOS.append([id, qtd])
    
    #Separar em outra função
    opcao = int(input("Finalizar atendimento?\n[1].SIM ||  [2]. NÃO\n"))
    if opcao == 1:
        finalizar_atendimento(1, PRODUTOS_SELECIONADOS)
    elif opcao == 2:
        return
    else:
        print("Comando inválido. Tente novamente.\n\n")



def finalizar_atendimento(id_cliente, lista):
    print(f"Cliente {id_cliente}")
    print(f"Data: {dt.now()}")
    print(tb(lista, headers=["Item","Produto", "Quant.", "Preço", "Total"]))
    print(f"Itens: {len(lista)}")
    #print(f"Total: {}") #Pegar o total de cada linha e somar

    ultimo_cliente = int(input("Este foi o último cliente?\n[1].SIM || [2]. NÃO\n"))
    if ultimo_cliente == 1:
        print("Deseja fechar o caixa?")

    

def fechar_caixa():
    table = [["a", 2, 111], ["b", 3, 222]]
    print("Fechamento do caixa")
    print(f"Data: {dt.now()}")
    print(tb(headers=["Cliente", "Total"]))

def confirmar_ultimo_cliente(escolha):
    if escolha == 1:
        opcao = int(input("Deseja fechar o caixa?\n[1].SIM ||  [2]. NÃO\n"))
        confirmacao_fechar_caixa(opcao)
    else:
        return

def confirmacao_fechar_caixa(escolha):
    if escolha == 1:
        fechar_caixa()
    else:
        return

def verifica_id(id):
    if id < 1 or id > len(LISTA_PRODUTOS):
        print("Erro: produto não cadastrado")
        return
    
def verifica_quantidade(qtd):
    if qtd < 1:
        print("Erro: quantidade deve ser maior que zero")
        return

menu()


#while(True):
#        lista_cliente.append(f"Cliente {indice_cliente + 1}")
#        print(lista_cliente[indice_cliente]) #Cliente 1
#        print("-> Iniciar atendimento")
#        opcao_iniciar = int(input("[1]. SIM  |  [2]. NÃO\n"))
#        if opcao_iniciar == 1:
#            menu_produtos()
#        elif opcao_iniciar == 2:
#            opcao = int(input("Finalizar atendimento?\n[1].SIM ||  [2]. NÃO\n"))
#            if opcao == 1:
#                finalizar_atendimento(PRODUTOS_SELECIONADOS)
#            
#        else:
#            print("Comando inválido. Tente novamente.\n\n")