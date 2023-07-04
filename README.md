# Cliente de Python para la API de la CMF

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://shields.io/) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)


Este paquete de Python proporciona una interfaz fácil de usar para la API de la Comisión para el Mercado Financiero de Chile (CMF). Permite recuperar reportes bancarios e indicadores financieros para un análisis más profundo.

## Requisitos mínimos

- Python 3.8+
- requests
- dateutil

## Instalación

El paquete se puede instalar fácilmente utilizando `pip`. Solo necesitas ejecutar el siguiente comando:

```bash
pip install cmf
```

## Uso básico

`CmfBancos` es una clase que unifica la funcionalidad de las clases `IndicadoresFinancierosChilenos` y `ReportesBancariosChilenos`, permitiendo un acceso más conveniente a todas las funciones.

La clase `CmfBancos` hereda de ambas clases, por lo que todos los métodos descritos anteriormente para `IndicadoresFinancierosChilenos` y `ReportesBancariosChilenos` están disponibles en una instancia de `CmfBancos`.

Para crear una instancia de `CmfBancos`, necesitas proveer tu API key como un argumento al inicializador. Puedes también proporcionar un tiempo de espera (en segundos) que se utilizará para todas las solicitudes a la API.

Ejemplo de uso:

```python
from cmf import CmfBancos
import os

# Utiliza la variable de entorno CMF_API_KEY para la API key
api_key = os.getenv("CMF_API_KEY")

# Crea una instancia de CmfBancos
cmf_client = CmfBancos(api_key)

# Ahora puedes utilizar todos los métodos descritos anteriormente
dolares = cmf_client.get_dolares(from_="2023/01/01", to_="2023/07/01")
balance = cmf_client.get_balance_situacion("001", "2023/01/01", "2023/07/01")

print(dolares)
print(balance)
```

## Documentación de los métodos

### Métodos de la clase `IndicadoresFinancierosChilenos`

Por defecto, si no se proporciona una fecha de inicio (`from_`), se establecerá en un año antes de la fecha de fin (`to_`). Si no se proporciona una fecha de fin, se establecerá en la fecha actual. Si no se proporcionan ambas fechas, la fecha de inicio será un año antes de la fecha actual y la fecha de fin será la fecha actual. Todos los métodos aceptan el formato "YYYY/MM/DD" si se desean datos diarios. Si se desean datos mensuales se debe ingresar el formato "YYYY/MM".

Los siguientes son los métodos disponibles en la clase `IndicadoresFinancierosChilenos`:

- `get_dolares(from_:str = None, to_:str = None)`: 
  - **from_** (str, optional): La fecha de inicio en formato "YYYY/MM/DD" para obtener los datos de tipo de cambio de dólares. 
  - **to_** (str, optional): La fecha de fin en formato "YYYY/MM/DD" para obtener los datos de tipo de cambio de dólares.

  Obtiene los datos de tipo de cambio de dólares para el período especificado.
  
  Ejemplo de uso:
  
  ```python
  dolares = cmf_client.get_dolares(from_="2023/01/01", to_="2023/07/01")
  print(dolares)
  ```

- `get_euros(from_:str = None, to_:str = None)`: 
  - **from_** (str, optional): La fecha de inicio en formato "YYYY/MM/DD" para obtener los datos de tipo de cambio de euros. 
  - **to_** (str, optional): La fecha de fin en formato "YYYY/MM/DD" para obtener los datos de tipo de cambio de euros.
  
  Obtiene los datos de tipo de cambio de euros para el período especificado.
  
  Ejemplo de uso:
  
  ```python
  euros = cmf_client.get_euros(from_="2023/01/01", to_="2023/07/01")
  print(euros)
  ```

- `get_ipc(from_:str = None, to_:str = None)`: 
  - **from_** (str, optional): El mes de inicio en formato "YYYY/MM" para obtener los datos del Índice de Precios al Consumidor (IPC). 
  - **to_** (str, optional): El mes de fin en formato "YYYY/MM" para obtener los datos del IPC.
  
  Obtiene los datos del Índice de Precios al Consumidor (IPC) para el período especificado.
  
  Ejemplo de uso:
  
  ```python
  ipc = cmf_client.get_ipc(from_="2023/01", to_="2023/07")
  print(ipc)
  ```

- `get_tip(from_:str = None, to_:str = None)`: 
  - **from_** (str, optional): El mes de inicio en formato "YYYY/MM" para obtener los datos de la Tasa de Interés Promedio (TIP). 
  - **to_** (str, optional): El mes de fin en formato "YYYY/MM" para obtener los datos de la TIP.
  
  Obtiene los datos de la Tasa de Interés Promedio (TIP) para el período especificado.
  
  Ejemplo de uso:
  
  ```python
  tip = cmf_client.get_tip(from_="2023/01", to_="2023/07")
  print(tip)
  ```

- `get_tmc(from_:str = None, to_:str = None)`: 
  - **from_** (str, optional): El mes de inicio en formato "YYYY/MM" para obtener los datos de la Tasa Máxima Convencional (TMC). 
  - **to_** (str, optional): El mes de fin en formato "YYYY/MM" para obtener los datos de la TMC.


  
  Obtiene los datos de la Tasa Máxima Convencional (TMC) para el período especificado.
  
  Ejemplo de uso:
  
  ```python
  tmc = cmf_client.get_tmc(from_="2023/01", to_="2023/07")
  print(tmc)
  ```

- `get_uf(from_:str = None, to_:str = None)`: 
  - **from_** (str, optional): El mes de inicio en formato "YYYY/MM" para obtener los datos de la Unidad de Fomento (UF). 
  - **to_** (str, optional): El mes de fin en formato "YYYY/MM" para obtener los datos de la UF.
  
  Obtiene los datos de la Unidad de Fomento (UF) para el período especificado.
  
  Ejemplo de uso:
  
  ```python
  uf = cmf_client.get_uf(from_="2023/01", to_="2023/07")
  print(uf)
  ```

- `get_utm(from_:str = None, to_:str = None)`: 
  - **from_** (str, optional): El mes de inicio en formato "YYYY/MM" para obtener los datos de la Unidad Tributaria Mensual (UTM). 
  - **to_** (str, optional): El mes de fin en formato "YYYY/MM" para obtener los datos de la UTM.
  
  Obtiene los datos de la Unidad Tributaria Mensual (UTM) para el período especificado.
  
  Ejemplo de uso:
  
  ```python
  utm = cmf_client.get_utm(from_="2023/01", to_="2023/07")
  print(utm)
  ```

### Métodos de la clase `ReportesBancariosChilenos`

Los siguientes son los métodos disponibles en la clase `ReportesBancariosChilenos`:

- `instituciones_bancarias()`: No recibe ningún parámetro de entrada. Obtiene el listado completo de instituciones bancarias disponibles en Chile de hace tres meses atrás. Para proximas versiones del paquete se espera incluir la funcionalidad de "viaje en el tiempo", es decir, mostrar las instituciones bancarias chilenas para un periodo especifico en el tiempo (e.g. Mayo de 2013)

  Ejemplo de uso:

  ```python
  instituciones = cmf_client.instituciones_bancarias()
  print(instituciones)
  ```

- `ac_capital_basico(cantidad:str, instituciones:str)`: 
  - **cantidad** (str): Períodos de tiempo requeridos para obtener los datos. 
  - **instituciones** (str): El código de las instituciones bancarias especificadas.
  
  Obtiene el capital básico para múltiples períodos de tiempo de las instituciones bancarias especificadas.
  
  Ejemplo de uso:
  
  ```python
  capital_basico = cmf_client.ac_capital_basico(cantidad="12", instituciones="001")
  print(capital_basico)
  ```
  
- `ac_patrimonio_efectivo(cantidad:str, instituciones:str)`: 
  - **cantidad** (str): Períodos de tiempo requeridos para obtener los datos. 
  - **instituciones** (str): El código de las instituciones bancarias especificadas.
  
  Obtiene el patrimonio efectivo para múltiples períodos de tiempo de las instituciones bancarias especificadas.
  
  Ejemplo de uso:
  
  ```python
  patrimonio_efectivo = cmf_client.ac_patrimonio_efectivo(cantidad="12", instituciones="001")
  print(patrimonio_efectivo)
  ```

- `ac_riesgo_credito(cantidad:str, instituciones:str)`: 
  - **cantidad** (str): Períodos de tiempo requeridos para obtener los datos. 
  - **instituciones** (str): El código de las instituciones bancarias especificadas.
  
  Obtiene los activos ponderados por riesgo de crédito (IRS) para múltiples períodos de tiempo de las instituciones bancarias especificadas.
  
  Ejemplo de uso:
  
  ```python
  riesgo_credito = cmf_client.ac_riesgo_credito(cantidad="12", instituciones="001")
  print(riesgo_credito)
  ```

- `ac_capital_activos(cantidad:str, instituciones:str)`: 
  - **cantidad** (str): Períodos de tiempo requeridos para obtener los datos. 
  - **instituciones** (str): El código de las instituciones bancarias especificadas.
  
  Obtiene el cociente de capital básico / activos totales (IRE) para múltiples períodos de tiempo de las instituciones bancarias especificadas.
  
  Ejemplo de uso:
  
  ```python
  capital_activos = cmf_client.ac_capital_activos(cantidad="12", instituciones="001")
  print(capital_activos)
  ```

- `ac_componentes_todos(year:str, month:str, instituciones:str)`: 
  - **year** (str): Año para obtener los datos. 
  - **month** (str): Mes para obtener los datos. 
  - **instituciones** (str): El código de las instituciones bancarias especificadas.
  
  Obtiene todas las cifras de los componentes de la Adecuación de Capital para la institución y el

 año y mes especificados.
  
  Ejemplo de uso:
  
  ```python
  componentes_todos = cmf_client.ac_componentes_todos(year="2023", month="07", instituciones="001")
  print(componentes_todos)
  ```

## Disclaimer

La información contenida en este documento es solo para fines informativos y educativos. Nada de lo contenido en este documento se podrá interpretar como asesoramiento financiero, legal o impositivo. El contenido de este documento corresponde únicamente a la opinión del autor, el cual no es un asesor financiero autorizado ni un asesor de inversiones registrado. El autor no está afiliado como promotor de los servicios de la CMF.

Este documento no es una oferta para vender ni comprar instrumentos financieros. Nunca invierta más de lo que puede permitirse perder. Usted debe consultar a un asesor profesional registrado antes de realizar cualquier inversión.