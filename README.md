# 📄 Leitor Inteligente de PDF - Seguro Garantia

Projeto de automação para leitura de editais e contratos, com extração automática de informações relevantes para cotação de Seguro Garantia.

---

## Funcionalidades

- Leitura de arquivos PDF
- Identificação do tipo de documento (Edital ou Contrato)
- Extração de CNPJ
- Extração de porcentagem de garantia (com contexto)
- Extração de vigência com regra de negócio:
  - < 90 dias → ajusta para 90 dias
  - ≥ 90 dias → mantém

---

## Diferencial

O sistema não apenas extrai dados, mas aplica regras reais de negócio utilizadas no mercado de seguros.

---

## Tecnologias utilizadas

- Python
- pdfplumber
- Regex (`re`)