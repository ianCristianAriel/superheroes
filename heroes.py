from lectura_archivos_texto import lectura_csv as lectura
from graficas import genera_grafico_barras as grafico_barras
from graficas import genera_grafico_circular as grafico_circular

# Abrire el archivo del CSV
path = ('./heroess.csv')

# Filtre los super heroes en Seniors y Juniors
# Iterar las listas y chequear los valores dentro de las colunmnas a evaluar, si son iguales o superiores se almacenan su diccionario dentro de la
# lista de seniors y, si son inferiores se almacena su diccionario dentro de las lista de juniors

seniors = []
juniors = []


def filtro(lista):
    for d in lista:
        # Si conside con todas las caracteristicas mas desarrolladas, es senior
        if (d['Power'] >= 100) and (d['IQ'] > 150 and d['IQ'] < 200) and (d['Combat' >= 90]) and (d['Alignment'] == 'Good'):
            seniors.append(d)
        else:
            # Por el contrario, es junior
            juniors.append(d)
    resultado = {
        'juniors': len(juniors),
        'seniors': len(seniors),
    }
    labels = resultado.labels()
    values = resultado.values()

    grafico_barras(labels, values)
    grafico_circular(labels, values)


if __name__ == '__main__':
    filtro(lectura(path))
