
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<COMMENT>#[^\n]*)|(?P<LIMIT>LIMIT\b)|(?P<VAR>\?[a-zA-Z0-9_]+)|(?P<LANG>@[a-zA-Z]{2})|(?P<STRING>"[^"]*")|(?P<NUM>\d+)|(?P<DELIM>[\{\}\.])|(?P<ID>[a-zA-Z_][a-zA-Z0-9_:]*)|(?P<SKIP>[ \t]+)|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['COMMENT']:
            t = ("COMMENT", dic['COMMENT'], linha, m.span())

        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())

        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())

        elif dic['LANG']:
            t = ("LANG", dic['LANG'], linha, m.span())

        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())

        elif dic['NUM']:
            t = ("NUM", dic['NUM'], linha, m.span())

        elif dic['DELIM']:
            t = ("DELIM", dic['DELIM'], linha, m.span())

        elif dic['ID']:
            t = ("ID", dic['ID'], linha, m.span())

        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())

        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())

        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())

        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
            
        # Filtra espacos e comentarios da lista final de tokens
        if not dic.get('SKIP') and not dic.get('COMMENT') and t[0] != 'UNKNOWN':
            reconhecidos.append(t)
            
        # Incrementa a linha ao encontrar o token NEWLINE
        if dic.get('NEWLINE'):
            linha += 1
            
    return reconhecidos

if __name__ == "__main__":
    input_texto = sys.stdin.read()
    for tok in tokenize(input_texto):
        print(tok)

