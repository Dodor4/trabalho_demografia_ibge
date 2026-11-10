import numpy as np
import pandas as pd

def calcular_estatisticas(df, coluna):
    """
    Calcula estatísticas descritivas completas:
    - Tendência Central: Média, Mediana
    - Dispersão: Desvio Padrão, IQR (Intervalo Interquartil)
    - Detecção de Outliers (Regra 1.5 * IQR)
    """
    dados = df[coluna].dropna()
    
    if len(dados) == 0:
        return {}

    media = dados.mean()
    mediana = dados.median()
    desvio_padrao = dados.std()
    
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1
    
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    
    outliers = dados[(dados < limite_inferior) | (dados > limite_superior)]
    
    return {
        "media": media,
        "mediana": mediana,
        "desvio_padrao": desvio_padrao,
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "outliers_count": len(outliers),
        "outliers_list": outliers.tolist()
    }
