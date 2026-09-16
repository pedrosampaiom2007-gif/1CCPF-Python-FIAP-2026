# 1CCPF-Python-FIAP-2026

Repositório de estudos da disciplina de Python da FIAP, turma **1CCPF** (2026). Reúne os exercícios, revisões e pequenos projetos desenvolvidos ao longo das aulas, acompanhando a evolução do conteúdo — dos fundamentos da linguagem até a construção de uma aplicação com persistência de dados.

## Propósito

O objetivo deste repositório é servir como **diário de aprendizado prático**: cada pasta representa uma etapa do curso, guardando o código produzido em sala ou como exercício de fixação. A ideia não é entregar produtos finais polidos, e sim documentar a progressão do aluno — de sintaxe básica e lógica condicional até a organização de um projeto em múltiplos módulos.

## Estrutura do repositório

- **`aula02-variaveis e operadores/`** — Primeiros contatos com Python: variáveis, tipos, operadores aritméticos/relacionais/lógicos, entrada e saída de dados, estruturas condicionais (`if`/`else`, `match`/`case`) e definição de funções simples.

- **`api e revisao/`** — Exercícios de revisão com foco em estruturas de dados e lógica de análise:
  - Um simulador de monitoramento de status de endpoints de API, que calcula taxa de sucesso, contagem de erros e classifica a "saúde" de cada endpoint com base nos códigos HTTP retornados.
  - Um gerador de relatório a partir de uma lista de e-mails, explorando manipulação de strings, dicionários e tuplas.

- **`mini crm/`** — Projeto mais robusto, organizado no padrão **Model-View-Control**: um mini CRM de cadastro de leads via terminal, com menu interativo para adicionar e listar contatos. Os dados são modelados (`model.py`), persistidos em `data/leads.json` (`control.py`) e a interação com o usuário fica a cargo de `app.py`. Marca o momento em que o curso passa de scripts isolados para uma aplicação com separação de responsabilidades e armazenamento em disco.

## Como executar

Os scripts usam apenas bibliotecas padrão do Python (mais `sqlalchemy` em um exercício pontual), sem dependências externas para rodar a maioria dos exemplos. Para executar qualquer arquivo, use:

\`\`\`bash
python "caminho/do/arquivo.py"
\`\`\`


## Contexto

Trabalho contínuo de sala de aula — o conteúdo é incremental e reflete o que foi ensinado a cada aula, sem pretensão de ser um projeto de produção.
