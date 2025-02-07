# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd
import zipfile
import os

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    def extraer_zip(ruta_zip,ruta_salida):
        with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
            zip_ref.extractall(ruta_salida)

    def procesar_archivos(ruta_input):
        dataset_test = []
        dataset_train = []
        carpetas = ["test","train"]
        sentimientos = ["negative","neutral","positive"]

        for carpeta in carpetas:

            for sentimiento in sentimientos:

                ruta = f"{ruta_input}/{carpeta}/{sentimiento}"
                for archivo in os.listdir(ruta):

                    with open(f"{ruta}/{archivo}") as file: 
                        linea = file.read()
                        informacion = {"phrase":linea,"target":sentimiento}

                        if carpeta == "test":
                            dataset_test.append(informacion)
                        else:
                            dataset_train.append(informacion)

        return dataset_test,dataset_train
    
    def guardar_archivos(dataset, ruta_salida):
        df = pd.DataFrame(dataset)
        print(df["target"].value_counts())
        df.to_csv(ruta_salida)

    dataset_test = []
    dataset_train = []
    ruta_input = "files/input/input/input"
    ruta_salida = "files/output"

    extraer_zip("files/input.zip",ruta_input)
    dataset_test,dataset_train = procesar_archivos(ruta_input)
    guardar_archivos(dataset_test, f"{ruta_salida}/test_dataset.csv")
    guardar_archivos(dataset_train, f"{ruta_salida}/train_dataset.csv")

if __name__ == '__main__':
    pregunta_01()