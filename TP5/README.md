# Resolução do TP5

![Foto do Autor](https://avatars.githubusercontent.com/u/131169410?v=4) 

### **Data:** 25 de Março de 2025  
### **Autor:**  
- **Nome:** Pedro Manuel Dias Teixeira
- **Número de Aluno:** A103998

---

## Resumo
Este programa em Python simula o funcionamento de uma Vending Machine, permitindo listar produtos, inserir moedas, selecionar itens, adicionar novos produtos e devolver troco. O stock é armazenado num ficheiro JSON (`stock.json`), garantindo que o estado da aplicação é mantido entre execuções.  

---

## Funcionalidades  
- **Carregamento e salvamento do stock**: O stock é lido do ficheiro `stock.json` ao iniciar e guardado ao sair.  
- **Listagem de produtos disponíveis**: Comando `LISTAR` exibe os produtos e respetivas quantidades.  
- **Inserção de moedas**: O utilizador pode inserir moedas com o comando `MOEDA`.  
- **Seleção de produtos**: Comando `SELECIONAR <CÓDIGO>` permite comprar um produto, se houver saldo suficiente.  
- **Devolução de troco**: Se houver saldo restante ao sair, a máquina devolve o troco na menor quantidade possível de moedas.  
- **Adição de produtos**: Comando `ADICIONAR <CÓDIGO> <NOME> <QUANTIDADE> <PREÇO>` para adicionar novos produtos ou atualizar stock.  

---
