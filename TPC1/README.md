# TPC 1 - Expressão Regular
### Enunciado
Expressão regular para apanhar strings binarias que não contenham a substring "011".

---

### Resolução
* [TPC1 - Expressão Regular](Expressao_Regular.txt)

Uma expressão regular que proíbe substrings da forma `011` pode ser expressa através da seguinte forma(com suporte para motores padrão como o [Regex101](https://regex101.com/)):

^1*(01?)*$

### Explicação
- ^ e $ - inicio e fim da linha
- 1* -  Permite qualquer quantidade de 1s antes do primeiro 0
- (01?)* - exige um 0 e depois, o 1 seguinte é opcional, ou seja, se existir um 1, a sequencia fecha para não permitir um segundo 1, isto pode repetir-se varias vezes

## Exemplos:
| ✅ Strings aceites | ❌ Strings rejeitadas |
|---|---|
| `1101` | `10111` |
| `101010` | `011011` |
