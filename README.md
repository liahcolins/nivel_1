# Desafio Nível 1 — PDV com Descontos (Python)

## O que o código faz

Este programa simula um Ponto de Venda (PDV). Ele recebe o valor de cada compra e a idade do cliente, calcula os descontos aplicáveis, mostra o valor final e registra as compras em uma lista. Quando o usuário digita `0` como valor da compra, o programa encerra o registro e apresenta um resumo do dia.

## Como o código funciona

1. Solicita o valor da compra. Se o valor for negativo, exibe um aviso e solicita outro valor. Se o valor for `0`, encerra o loop de compras.
2. Solicita a idade do cliente. Se a idade for negativa, pede a idade novamente, mantendo o valor da compra já informado.
3. Se a idade for maior ou igual a 65 anos, aplica 20% de desconto sobre o valor original.
4. Verifica o valor depois do desconto por idade. Se esse valor for **maior que R$ 100,00**, aplica mais 10% sobre ele. Portanto, um valor de exatamente R$ 100,00 não recebe o desconto adicional.
5. Calcula o total de descontos e o valor final, exibindo os valores em reais com duas casas decimais.
6. Usa `historico.append()` para guardar os dados de cada compra em uma lista.
7. Quando o usuário digita `0`, percorre o histórico e calcula a quantidade de compras, o total bruto, o total de descontos e o total final.

## Como executar

Tenha o Python 3 instalado. Abra um terminal na pasta `nivel_1` e execute:

```bash
python pdv.py
```

Quando quiser encerrar, digite `0` na pergunta do valor da compra.

## Casos de teste

Use cada linha como uma compra independente e compare o valor final mostrado pelo programa com a última coluna. Para encerrar a execução, digite `0` no valor da compra.

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---:|---:|---:|---:|---:|---:|
| 1 | 50,00 | 30 | 0% | 0% | R$ 50,00 |
| 2 | 100,00 | 30 | 0% | 0% | R$ 100,00 |
| 3 | 80,00 | 65 | 20% | 0% | R$ 64,00 |
| 4 | 100,00 | 70 | 20% | 0% | R$ 80,00 |
| 5 | 125,00 | 70 | 20% | 0% | R$ 100,00 |
| 6 | 200,00 | 30 | 0% | 10% | R$ 180,00 |
| 7 | 101,00 | 30 | 0% | 10% | R$ 90,90 |
| 8 | 200,00 | 65 | 20% | 10% | R$ 144,00 |
| 9 | 1.000,00 | 80 | 20% | 10% | R$ 720,00 |
| 10 | 200,00 | 64 | 0% | 10% | R$ 180,00 |

## Estrutura da entrega

```text
nivel_1/
├── pdv.py       # Código do PDV
└── README.md    # Documentação e casos de teste
```

## Observações

- O desconto de 20% é aplicado primeiro e somente quando a idade é maior ou igual a 65 anos.
- O desconto adicional de 10% usa o valor que restou após o desconto por idade e só se aplica quando esse valor é estritamente maior que R$ 100,00.
- O histórico é mantido em memória durante a execução do programa.
- O programa segue as restrições do desafio: não utiliza `def` nem `try/except`.
