def processar_texto(text):

    ativo = True 
    soma_total = 0

    sequencia_atual = ""

    for elemento in text:
        if elemento.isalpha():
            if sequencia_atual.isdigit():
                soma_total += int(sequencia_atual) 
                sequencia_atual = ""

            sequencia_atual += elemento

            if sequencia_atual.lower() == "on":
                ativo = True 
            elif sequencia_atual.lower() == "off":
                ativo = False 
        elif elemento.isdigit():
            if sequencia_atual.isalpha():
                sequencia_atual = ""
            if ativo:
                sequencia_atual += elemento
        elif elemento == "=":
            if sequencia_atual.isdigit():
                soma_total += int(sequencia_atual) 
                sequencia_atual = ""
            elif sequencia_atual.isalpha():
                sequencia_atual = ""
            print(soma_total)  
        else:
            if sequencia_atual.isdigit():
                soma_total += int(sequencia_atual) 
            sequencia_atual = ""  

texto = input("Qual é o texto que pretendes testar?")
#texto_exemplo = "123; abc456On78Off90On12=abc=34Off56=On1="
processar_texto(texto)