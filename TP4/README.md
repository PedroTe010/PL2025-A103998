# Resolução do TP4

![Foto do Autor](https://avatars.githubusercontent.com/u/131169410?v=4) 

### **Data:** 2 de Março de 2025  
### **Autor:**  
- **Nome:** Pedro Manuel Dias Teixeira
- **Número de Aluno:** A103998

---

## Resumo
Este programa em Python é um analisador léxico para uma liguagem de query.

---

## Resultados
Acompanhado do programa está um ficheiro .txt para input no programa.

A query presente no ficheiro é a mesma do guião:

```
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

---
