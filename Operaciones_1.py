def normalizar(df,columna):
    df_norm = df.copy()
    df_norm[columna] = (df_norm[columna] - df_norm[columna].mean())/df_norm[columna].std()

    return df_norm


def estandarizar(df, columna):
    df_estand = df.copy()
    df_estand[columna] = (df_estand[columna]-df_estand[columna].min())/ (df_estand[columna].max() - df_estand[columna].min())

    return df_estand