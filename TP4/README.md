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

Resultados:
```
[SELECT] -> select
[None] ->
[VARIABLE] -> ?nome
[None] ->
[VARIABLE] -> ?desc
[None] ->
[WHERE] -> where
[None] ->
[START] -> {
[None] ->

[VARIABLE] -> ?s
[None] ->
[COMPONENT] -> a
[None] ->
[CONNECTION] -> dbo:
[COMPONENT] -> MusicalArtist
[END OF QUERY] -> .
[None] ->

[VARIABLE] -> ?s
[None] ->
[CONNECTION] -> foaf:
[COMPONENT] -> name
[None] ->
[STRING] -> "Chuck Berry"
[LANGUAGE] -> @en
[None] ->
[END OF QUERY] -> .
[None] ->

[VARIABLE] -> ?w
[None] ->
[CONNECTION] -> dbo:
[COMPONENT] -> artist
[None] ->
[VARIABLE] -> ?s
[END OF QUERY] -> .
[None] ->

[VARIABLE] -> ?w
[None] ->
[CONNECTION] -> foaf:
[COMPONENT] -> name
[None] ->
[VARIABLE] -> ?nome
[END OF QUERY] -> .
[None] ->

[VARIABLE] -> ?w
[None] ->
[CONNECTION] -> dbo:
[COMPONENT] -> abstract
[None] ->
[VARIABLE] -> ?desc
[None] ->

[END] -> }
[None] ->
[COMPONENT] -> LIMIT
[None] ->
[NUMBER] -> 1000
```

---
