import pandas as pd
import requests
import time
import os

arquivoentrada = r'C:\Users\Exata\OneDrive - Exata Tech\Área de Trabalho\Projetos Exata\python_exata\SeguradorasNormalização1.xlsx'
arquivosaida = 'resultado_final.xlsx'

def tratar_cnpj(cnpj_sujo):
    cnpj = str(cnpj_sujo).strip()
    for char in [".", "-", "/", " "]:
        cnpj = cnpj.replace(char, "")
    return cnpj.zfill(14)

def consultar_razao_social(cnpj):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('razao_social')
        elif response.status_code == 429:
            time.sleep(2)
            return consultar_razao_social(cnpj)
        return "Não encontrado/Erro"
    except:
        return "Falha na conexão"

# 1. Lendo o arquivo
df = pd.read_excel(arquivoentrada)

# 2. Forçando a Coluna H (índice 7) a ser TEXTO
col_h_nome = df.columns[7]
df[col_h_nome] = df[col_h_nome].astype(str).str.replace('\.0$', '', regex=True)

print(f"A coluna {col_h_nome} (H) foi convertida para texto.")

# 3. Resto do processamento
df['cnpj_limpo'] = df['Cliente CNPJ'].apply(tratar_cnpj)

df2 = df[["cnpj_limpo"]].drop_duplicates()
df2['razao_social'] = df2['cnpj_limpo'].apply(consultar_razao_social)

df_final = pd.merge(left=df, right=df2, how="left", on='cnpj_limpo')

# 4. Salvando
df_final.to_excel(arquivosaida, index=False)
print(f"Pronto! Arquivo '{arquivosaida}' gerado.")