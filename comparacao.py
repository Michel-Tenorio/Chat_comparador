def comparar_opcoes(op1, op2):
  
    print("\n Comparando opções ")
    print(f"Opção 1: {op1['nome']} - Custo: {op1['custo']}, Nota de benefício: {op1['beneficio']}")
    if op1['desc']:
        print(f"Descrição: {op1['desc']}")
    print(f"Opção 2: {op2['nome']} - Custo: {op2['custo']}, Nota de benefício: {op2['beneficio']}")
    if op2['desc']:
        print(f"Descrição: {op2['desc']}\n")


    ratio1 = op1['beneficio'] / op1['custo']
    ratio2 = op2['beneficio'] / op2['custo']

    if ratio1 > ratio2:
        melhor = op1
        justificativa = f"{op1['nome']} tem melhor custo-benefício (benefício/custo = {ratio1:.2f})"
    elif ratio2 > ratio1:
        melhor = op2
        justificativa = f"{op2['nome']} tem melhor custo-benefício (benefício/custo = {ratio2:.2f})"
    else:
        melhor = None
        justificativa = "Ambas as opções têm custo-benefício equivalente."

    return melhor, justificativa


def chatbot():
    print(" Bem-vindo ao Chat Comparador Avançado \n")

  
    nome1 = input("Digite o nome da primeira opção: ")
    custo1 = float(input(f"Custo de {nome1}: "))
    beneficio1 = float(input(f"Nota de benefício de {nome1} (ex: 1 a 10): "))
    desc1 = input(f"Descrição de {nome1} (opcional): ")

   
    nome2 = input("\nDigite o nome da segunda opção: ")
    custo2 = float(input(f"Custo de {nome2}: "))
    beneficio2 = float(input(f"Nota de benefício de {nome2} (ex: 1 a 10): "))
    desc2 = input(f"Descrição de {nome2} (opcional): ")


    op1 = {'nome': nome1, 'custo': custo1, 'beneficio': beneficio1, 'desc': desc1}
    op2 = {'nome': nome2, 'custo': custo2, 'beneficio': beneficio2, 'desc': desc2}


    melhor, justificativa = comparar_opcoes(op1, op2)

    print("\n Resultado ")
    if melhor:
        print(f"A melhor opção é: {melhor['nome']}")
    print("Justificativa:", justificativa)


if __name__ == "__main__":
    chatbot()
