import re

def identificar_tipo_documento(texto):
    texto = texto.lower()
    if "edital" in texto:
        return "Edital"
    elif "contrato" in texto:
        return "Contrato"
    else:
        return "Não identificado"

def extrair_cnpj(texto):
    padrao = r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}"
    resultado = re.findall(padrao, texto)
    return resultado

def extrair_porcentagem(texto):
    texto = texto.lower()
    if "garantia da proposta" in texto:
        inicio = texto.find("garantia da proposta")
    elif "garantia de execução" in texto:
        inicio = texto.find("garantia de execução")
    else:
        return []
    if inicio == -1:
        return []
    trecho = texto[inicio:inicio+500]
    resultado = re.findall(r"\d+%", trecho)
    return resultado

def extrair_vigencia(texto):
    texto = texto.lower()
    if "vigência" in texto:
        inicio = texto.find("vigência")
    elif "prazo" in texto:
        inicio = texto.find("prazo")
    else:
        return None
    if inicio == -1:
        return None
    trecho = texto[inicio:inicio+300]
    resultado = re.findall(r"\d+\s*dias", trecho)
    if resultado:
        dias = int(resultado[0].split()[0])
    else:
        return None
    if dias < 90:
        return 90
    else:
        return dias