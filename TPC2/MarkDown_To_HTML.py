import doctest
import re


def markdown_to_html(texto_markdown):
    """Converte um texto em Markdown para HTML.

    >>> markdown_to_html("# Exemplo")
    '<h1>Exemplo</h1>'

    >>> markdown_to_html("Este é um **exemplo** ...")
    'Este é um <b>exemplo</b> ...'

    >>> markdown_to_html("Este é um *exemplo* ...")
    'Este é um <i>exemplo</i> ...'

    >>> print(markdown_to_html("1. Primeiro item\\n2. Segundo item\\n3. Terceiro item"))
    <ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
    </ol>

    >>> markdown_to_html("Como pode ser consultado em [página da UC](http://www.uc.pt)")
    'Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>'

    >>> markdown_to_html("Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...")
    'Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...'
    """
    
    linhas = texto_markdown.splitlines()
    string_html = []
    na_lista = False

    for linha in linhas:
        # Lista Numerada
        lista_match = re.match(r"^\d+\.\s+(.*)$", linha)
        if lista_match:
            if not na_lista:
                string_html.append("<ol>")
                na_lista = True
            content = aplica_estilos(lista_match.group(1))
            string_html.append(f"<li>{content}</li>")
            continue
        else:
            if na_lista:
                string_html.append("</ol>")
                na_lista = False

        # Cabeçalhos (#, ##, ###)
        cabecalho = re.match(r"^(#{1,3})\s+(.*)$", linha)
        if cabecalho:
            level = len(cabecalho.group(1))
            content = aplica_estilos(cabecalho.group(2))
            string_html.append(f"<h{level}>{content}</h{level}>")
            continue

        # Linhas Normais
        string_html.append(aplica_estilos(linha))

    if na_lista:
        string_html.append("</ol>")

    return "\n".join(string_html)

def aplica_estilos(text):
    """Aplica estilos inline: Imagens, Links, Bold e Itálico."""
    # Imagens: de ![alt](src) para <img src="src" alt="alt"/> (processar ANTES dos links)
    text = re.sub(
        r"!\s*\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1"/>', text
    )

    # Links: de [texto](url) para <a href="url">texto</a>
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)

    # Bold: de **texto** para <b>texto</b>
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)

    # Itálico: de *texto* para <i>texto</i>
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)

    return text


if __name__ == "__main__":
    # 1. Executa os testes por doctestes
    doctest.run_docstring_examples(markdown_to_html, globals(), verbose=True)