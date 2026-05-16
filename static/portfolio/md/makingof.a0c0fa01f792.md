# Making Of

---

## Introdução
O Making Of documenta o desenvolvimento da aplicação Django desde a fase inicial até à versão final.

---

## Definição inicial do projeto
O projeto começou com uma estrutura simples baseada em:
- Licenciatura
- Ano
- Unidade Curricular
- Projeto

---

## Evolução do modelo de dados
Com a análise dos ficheiros JSON, o modelo foi expandido com novas entidades:
- Tecnologia
- Competencia
- Formacao
- TFC

---

## Relações entre entidades
Foram usadas relações do Django:
- ForeignKey (1-N)
- ManyToMany (N-N)

Exemplo:
- Uma UC tem vários docentes
- Um projeto pode ter várias tecnologias

---

## Automação com loaders
Foram criados scripts para importar dados automaticamente:
- loader.py
- loadertfc.py

---

## Ajustes finais
- Correção de campos
- Otimização do modelo
- Organização das relações

---

## Conclusão
O sistema evoluiu de um modelo simples para uma aplicação completa e estruturada.