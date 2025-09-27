respostas = {
    "1": "A filial com maior volume total de vendas foi o **Supermercado Central**.",
    "2": "O produto mais vendido no geral foi o **Ovos**.",
    "3": """Top 5 mais vendidos:
1. Ovos
2. Arroz
3. Refrigerante
4. Sabão em Pó
5. Frango

Bottom 5 menos vendidos:
1. Shampoo
2. Café
3. Sabonete
4. Queijo
5. Manteiga""",
    "4": "Produto que se destaca apenas em uma filial: **Sabonete no Supermercado Popular**.",
    "5": "O mês com maior volume de vendas foi o **Mês 8 (Agosto)**.",
    "6": "Entre os produtos básicos, o maior crescimento foi do **Arroz**.",
    "7": "A filial com maior variação de vendas foi o **Supermercado Central**.",
    "8": "Filiais abaixo da média de vendas totais: **Supermercado Manaus, Supermercado Ponto Certo, Supermercado Nova Era, Supermercado Vitória**.",
    "9": "Produtos com crescimento em Novembro → Dezembro: **Cerveja, Suco, Carne Bovina, Ovos, Queijo**."
}

def chatbot():
    print(" Chatbot Supermercado pronto! Pergunte usando o número da questão (1 a 9). Digite 'sair' para encerrar.\n")
    while True:
        pergunta = input("Sua pergunta: ").strip().lower()
        
        if pergunta in ["sair", "exit", "quit"]:
            print("Até mais! ")
            break
        
        
        if pergunta.isdigit() and pergunta in respostas:
            print(respostas[pergunta])
        
        
        else:
            for num in respostas:
                if num in pergunta:
                    print(respostas[num])
                    break
            else:
                print("Desculpe, não entendi. Pergunte de 1 a 9.")
                


chatbot()