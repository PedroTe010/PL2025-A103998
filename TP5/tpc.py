import json
import datetime

def carregar_stock(filename="stock.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 

def guardar_stock(stock, filename="stock.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(stock, file, indent=4, ensure_ascii=False)

def listar_produtos(stock):
    print("maq:\n")
    print("cod | nome | quantidade | preço")
    print("---------------------------------")
    for item in stock:
        print(f"{item['cod']} {item['nome']} {item['quant']} {item['preco']:.2f}")

def processar_moedas(entrada):
    valores = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}
    saldo = 0
    for moeda in entrada.split(","):
        moeda = moeda.strip()
        if moeda in valores:
            saldo += valores[moeda]
    return saldo

def selecionar_produto(codigo, saldo, stock):
    for item in stock:
        if item["cod"] == codigo:
            if item["quant"] == 0:
                print("maq: Produto esgotado!")
                return saldo
            if saldo < item["preco"] * 100:
                print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                print(f"maq: Saldo = {saldo}c; Pedido = {int(item['preco'] * 100)}c")
                return saldo
            item["quant"] -= 1
            saldo -= int(item["preco"] * 100)
            print(f"maq: Pode retirar o produto dispensado \"{item['nome']}\"")
            print(f"maq: Saldo = {saldo}c")
            return saldo
    print("maq: Produto inexistente!")
    return saldo

def devolver_troco(saldo):
    valores = [50, 20, 10, 5, 2, 1]
    troco = {}
    for moeda in valores:
        if saldo >= moeda:
            troco[moeda] = saldo // moeda
            saldo %= moeda
    return troco

def adicionar_produto(stock, codigo, nome, quantidade, preco):
    for item in stock:
        if item["cod"] == codigo:
            item["quant"] += quantidade
            print("maq: Produto atualizado com sucesso!")
            return
    stock.append({"cod": codigo, "nome": nome, "quant": quantidade, "preco": preco})
    print("maq: Novo produto adicionado!")

def main():
    stock = carregar_stock()
    print(f"maq: {datetime.date.today()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    saldo = 0

    while True:
        comando = input(">> ").strip().upper()
        if comando == "LISTAR":
            listar_produtos(stock)
        elif comando.startswith("MOEDA"):
            saldo += processar_moedas(comando[6:].strip())
            print(f"maq: Saldo = {saldo}c")
        elif comando.startswith("SELECIONAR"):
            codigo = comando.split()[1]
            saldo = selecionar_produto(codigo, saldo, stock)
        elif comando.startswith("ADICIONAR"):
            _, codigo, nome, quantidade, preco = comando.split(None, 4)
            adicionar_produto(stock, codigo, nome, int(quantidade), float(preco))
        elif comando == "SAIR":
            troco = devolver_troco(saldo)
            if troco:
                print("maq: Pode retirar o troco:", ", ".join([f"{v}x {k}c" for k, v in troco.items()]))
            print("maq: Até à próxima")
            guardar_stock(stock)
            break
        else:
            print("maq: Comando não reconhecido!")

if __name__ == "__main__":
    main()
