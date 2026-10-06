# TPC 2 - Conversor de Markdown para HTML
### Enunciado
Criar em Python um pequeno conversor de Markdown para HTML que processe os elementos básicos da "Basic Syntax" (Cabeçalhos, Bold, Itálico, Listas numeradas, Links e Imagens).

---

### Resolução
* [TPC 2 - Markdown To HTML](MarkDown_To_HTML.py)

O conversor foi implementado em Python utilizando expressões regulares (`re.sub` e `re.match`) para identificar e substituir os marcadores de Markdown pelas respetivas *tags* HTML.

### Funcionalidades e Regras
- **Cabeçalhos (`#`, `##`, `###`):** Converte marcadores no início da linha para `<h1>`, `<h2>` e `<h3>`.
- **Bold (`**texto**`):** Converte texto entre `**` para `<b>`.
- **Itálico (`*texto*`):** Converte texto entre `*` para `<i>`.
- **Listas Numeradas:** Identifica linhas iniciadas por números (`1. `) e envolve-as num bloco `<ol>` com elementos `<li>`.
- **Links (`[texto](url)`):** Converte para `<a href="url">texto</a>`.
- **Imagens (`![alt](src)`):** Converte para `<img src="src" alt="alt"/>` (processadas antes dos links para evitar ambiguidades).

## Exemplos:
| Entrada (Markdown) | Saída (HTML) |
|---|---|
| `# Exemplo` | `<h1>Exemplo</h1>` |
| `Este é um **exemplo**` | `Este é um <b>exemplo</b>` |
| `Este é um *exemplo*` | `Este é um <i>exemplo</i>` |
| `[página da UC](http://www.uc.pt)` | `<a href="http://www.uc.pt">página da UC</a>` |
| `![coelho](http://coelho.com)` | `<img src="http://coelho.com" alt="coelho"/>` |