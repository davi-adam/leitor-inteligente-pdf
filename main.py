from services.pdf_reader import extrair_texto_pdf
from services.extratores import (
    identificar_tipo_documento,
    extrair_cnpj,
    extrair_porcentagem,
    extrair_vigencia
)

def main():
    caminho = input("Digite o caminho do PDF: ")

    texto = extrair_texto_pdf(caminho)
    
    tipo = identificar_tipo_documento(texto)
    cnpjs = extrair_cnpj(texto)
    porcentagens = extrair_porcentagem(texto)
    vigencia = extrair_vigencia(texto)

    resultado = {
        "tipo": tipo,
        "cnpjs": cnpjs,
        "porcentagens": porcentagens,
        "vigencia": vigencia
    }

    print("Resultado da análise:")
    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()