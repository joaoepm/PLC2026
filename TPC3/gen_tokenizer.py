import sys
import json

def main():
    if len(sys.argv) < 2:
        print("Uso: python gen_tokenizer.py <ficheiro_json> > analisador_lexico.py")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            tokens = json.load(f)
           
        tokens_regex = '|'.join([f"(?P<{t['id']}>{t['expreg']})" for t in tokens])

        code = f"""
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'{tokens_regex}', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['{tokens[0]['id']}']:
            t = ("{tokens[0]['id']}", dic['{tokens[0]['id']}'], linha, m.span())
"""

        for t in tokens[1:]:
            code += f"""
        elif dic['{t['id']}']:
            t = ("{t['id']}", dic['{t['id']}'], linha, m.span())
"""

        code += """
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
"""
        print(code)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not valid JSON.")
        sys.exit(1)

if __name__ == "__main__":
    main()