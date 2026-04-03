# EasyCNPJ
Esta ferramenta automatiza o processo de validação e enriquecimento de dados cadastrais de empresas. O script lê uma lista de CNPJs a partir de uma planilha Excel, consulta as informações oficiais via API e retorna os dados de Razão Social e o CNPJ formatado/limpo diretamente para o arquivo.
# 🔍 Automação de Consulta e Higienização de CNPJ

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

Este projeto automatiza o fluxo de tratamento de dados cadastrais. O script lê uma lista de CNPJs de um arquivo Excel, remove a pontuação (limpeza), consulta os dados atualizados via API (BrasilAPI/ReceitaWS) e retorna a **Razão Social** oficial diretamente para uma nova planilha.

## 🚀 Funcionalidades

- **Sanitização Automática:** Transforma `00.000.000/0001-91` em `00000000000191` antes da consulta.
- **Consulta em Lote:** Processa múltiplos registros de forma sequencial.
- **Enriquecimento de Dados:** Busca o nome empresarial (Razão Social) direto da base da Receita Federal.
- **Exportação Segura:** Gera um novo arquivo Excel com os resultados, evitando a perda dos dados originais.
