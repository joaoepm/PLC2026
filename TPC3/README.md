# TPC3 — Analisador Léxico

## 1. Resumo e Objetivos

O objetivo deste trabalho (TPC3) consiste na construção de um **analisador léxico** para consultas.

A solução foi desenvolvida segundo uma **metodologia declarativa**:
1. Especificação dos tokens e expressões regulares num ficheiro JSON (`tokens.json`).
2. Geração automática do código Python do analisador léxico através de um script gerador (`gen_tokenizer.py`).
3. Análise e extração da sequência de tokens a partir do código gerado (`analisador_lexico.py`).

---

## 2. Requisitos Cumpridos

O analisador processa a entrada e reconhece os seguintes elementos segundo a especificação do enunciado:

- **Comentários (`COMMENT`):** Linhas iniciadas por `#` são ignoradas e filtradas da lista final de tokens.
- **Variáveis (`VAR`):** Identificadores começados por `?` (ex: `?nome`, `?desc`, `?s`, `?w`).
- **Identificador de Língua (`LANG`):** Tag de idioma começada por `@` seguida de 2 carateres (ex: `@en`).
- **Strings (`STRING`):** Sequências delimitadas por aspas (ex: `"Chuck Berry"`).
- **Valores Numéricos (`NUM`):** Sequências de dígitos numéricos (ex: `1000`).
- **Palavras Reservadas (`LIMIT`):** Reconhecimento explícito da palavra reservada `LIMIT`.
- **Delimitadores (`DELIM`):** Símbolos de pontuação e agrupamento `{`, `}` e `.`.
- **Identificadores/Conceitos (`ID`):** Prefixos RDF, propriedades e conceitos (ex: `select`, `where`, `dbo:MusicalArtist`, `foaf:name`, `a`).
- **Gestão de Espaços e Linhas (`SKIP`, `NEWLINE`):** Espaços em branco são ignorados e as quebras de linha (`\n`) incrementam corretamente o contador da linha onde cada *token* ocorre.

---

## 3. Instruções de Execução

### Passo 1: Gerar o Analisador Léxico
Para criar/atualizar o ficheiro `analisador_lexico.py` a partir da especificação `tokens.json`, executa:

```
python gen_tokenizer.py tokens.json > analisador_lexico.py
```

### Passo 2: Executar o Analisador com o Exemplo
Para processar a consulta contida no ficheiro `exemplo.txt` e imprimir a lista de tokens num ficheiro output:

```
python analisador_lexico.py < exemplo.txt > output.txt
```

---

## 4. Resultados

Ao processar o ficheiro `exemplo.txt`, o analisador devolve os tokens no formato `(TIPO, VALOR, LINHA, SPAN)` num ficheiro `output.txt`:

### Input:
```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

### Output:

```
('NEWLINE', '\n', 1, (31, 32))
('NEWLINE', '\n', 2, (32, 33))
('ID', 'select', 3, (33, 39))
('VAR', '?nome', 3, (40, 45))
('VAR', '?desc', 3, (46, 51))
('ID', 'where', 3, (52, 57))
('DELIM', '{', 3, (58, 59))
('NEWLINE', '\n', 3, (59, 60))
('VAR', '?s', 4, (64, 66))
('ID', 'a', 4, (67, 68))
('ID', 'dbo:MusicalArtist', 4, (69, 86))
('DELIM', '.', 4, (86, 87))
('NEWLINE', '\n', 4, (87, 88))
('VAR', '?s', 5, (92, 94))
('ID', 'foaf:name', 5, (95, 104))
('STRING', '"Chuck Berry"', 5, (105, 118))
('LANG', '@en', 5, (118, 121))
('DELIM', '.', 5, (122, 123))
('NEWLINE', '\n', 5, (123, 124))
('VAR', '?w', 6, (128, 130))
('ID', 'dbo:artist', 6, (131, 141))
('VAR', '?s', 6, (142, 144))
('DELIM', '.', 6, (144, 145))
('NEWLINE', '\n', 6, (145, 146))
('VAR', '?w', 7, (150, 152))
('ID', 'foaf:name', 7, (153, 162))
('VAR', '?nome', 7, (163, 168))
('DELIM', '.', 7, (168, 169))
('NEWLINE', '\n', 7, (169, 170))
('VAR', '?w', 8, (174, 176))
('ID', 'dbo:abstract', 8, (177, 189))
('VAR', '?desc', 8, (190, 195))
('NEWLINE', '\n', 8, (195, 196))
('DELIM', '}', 9, (196, 197))
('LIMIT', 'LIMIT', 9, (198, 203))
('NUM', '1000', 9, (204, 208))
```

---

## 5. Estrutura do Projeto

- [tpc3.pdf](tpc3.pdf) - Enunciado do TPC3
- [tokens.json](tokens.json) - Especificação declarativa dos tokens e REs
- [gen_tokenizer.py](gen_tokenizer.py) - Script em Python que gera o analisador léxico
- [analisador_lexico.py](analisador_lexico.py) - Analisador léxico gerado automaticamente
- [exemplo.txt](exemplo.txt) - Ficheiro de entrada de teste
- [output.txt](output.txt) - Ficheiro de saída com os tokens