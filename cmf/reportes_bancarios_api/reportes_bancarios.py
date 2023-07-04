# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 08:26:36 2022

@author: lauta
"""

from cmf.request_handler_class import RequestHandler
from datetime import datetime, timedelta

class ReportesBancariosChilenos(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        """
        Clase para interactuar con la API de Reportes Bancarios Chilenos.
        
        Args:
            api_key (str): Clave de API para acceder a los servicios.
            timeout (int): Tiempo máximo de espera para las solicitudes en segundos.
        """
        super().__init__(api_key, timeout)
        # URL raices de cada endpoint
        self.URL_CALL = None # ruta final para solicitar datos a la API
        self.ROOT_ADECUACION = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/adecuacion'
        self.BALANCES_BANCOS = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/balances'
        self.ROOT_FICHAS = 'https://api.cmfchile.cl/api-sbifv3/recursos_api'
        self.ROOT_ESTADO_RESULTADOS = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/resultados'
        
        
    # ----------------------------------------
    # Metodos de ayuda para el manejo de casos
    # ----------------------------------------
    
    def __endpoint_builder(self, root:str, endpoint:str):
        """
        Construye la URL final para la solicitud a la API.
        
        Args:
            root (str): URL raíz del endpoint.
            endpoint (str): Ruta específica del endpoint.
        """
        self.URL_CALL = f"{root}{endpoint}"

    def __obtener_mes_y_anio_hace_tres_meses(self):
        """
        Obtiene el mes y el año de hace tres meses atrás con base en la fecha actual.
    
        Returns:
            str: El mes en formato 0X, donde X es un número de 1 a 9.
            int: El año de hace tres meses atrás.
        """
        # Obtener la fecha actual
        fecha_actual = datetime.now()
    
        # Restar 3 meses a la fecha actual
        fecha_hace_tres_meses = fecha_actual - timedelta(days=3 * 30)
    
        # Obtener el mes y el año de hace tres meses
        mes_hace_tres_meses = fecha_hace_tres_meses.strftime("%m")
        anio_hace_tres_meses = fecha_hace_tres_meses.year
    
        return mes_hace_tres_meses, anio_hace_tres_meses

    
    # ----------------------------------------
    # Metodos para solicitar datos a la API
    # ----------------------------------------
    
    def instituciones_bancarias(self, **query_params):
        """
        Obtener el listado completo de instituciones bancarias de hace tres meses atrás.
        
        Args:
            query_params: Parámetros adicionales de consulta (opcional).
        
        Returns:
            dict: Los datos de las instituciones bancarias.
        """
        mes_ref, anio_ref = self.__obtener_mes_y_anio_hace_tres_meses()
        
        codigo = 'DescripcionesCodigosDeInstituciones'
        self.__endpoint_builder(
            self.BALANCES_BANCOS,
            f"/{anio_ref}/{mes_ref}/instituciones"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)

    
    # ----------------------------------------
    # Adecuacion de Capital
    # ----------------------------------------
        
    def ac_capital_basico(self, **query_params):
        """
        Obtiene el capital básico para múltiples períodos de tiempo de las instituciones bancarias especificadas.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'cantidad' y 'instituciones'.
    
        Returns:
            dict: Los datos del capital básico para los períodos y las instituciones especificadas.
        """
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/regresionmensual/{query_params['cantidad']}/instituciones/{query_params['instituciones']}/indicadores/capbas"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def ac_patrimonio_efectivo(self, **query_params):
        """
        Obtiene el patrimonio efectivo para múltiples períodos de tiempo de las instituciones bancarias especificadas.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'cantidad' y 'instituciones'.
    
        Returns:
            dict: Los datos del patrimonio efectivo para los períodos y las instituciones especificadas.
        """
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/regresionmensual/{query_params['cantidad']}/instituciones/{query_params['instituciones']}/indicadores/patefe"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def ac_riesgo_credito(self, **query_params):
        """
        Obtiene los activos ponderados por riesgo de crédito (IRS) para múltiples períodos de tiempo de las instituciones bancarias especificadas.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'cantidad' y 'instituciones'.
    
        Returns:
            dict: Los datos de los activos ponderados por riesgo de crédito para los períodos y las instituciones especificadas.
        """
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/regresionmensual/{query_params['cantidad']}/instituciones/{query_params['instituciones']}/indicadores/irs"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def ac_capital_activos(self, **query_params):
        """
        Obtiene el cociente de capital básico / activos totales (IRE) para múltiples períodos de tiempo de las instituciones bancarias especificadas.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'cantidad' y 'instituciones'.
    
        Returns:
            dict: Los datos del cociente de capital básico / activos totales para los períodos y las instituciones especificadas.
        """
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/regresionmensual/{query_params['cantidad']}/instituciones/{query_params['instituciones']}/indicadores/ire"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def ac_componentes_todos(self, **query_params):
        """
        Obtiene todas las cifras de los componentes de la Adecuación de Capital para la institución y el período de tiempo especificados.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'year', 'month' y 'instituciones'.
    
        Returns:
            dict: Los datos de todos los componentes de la Adecuación de Capital para la institución y el período de tiempo especificados.
        """
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/anhos/{query_params['year']}/meses/{query_params['month']}/instituciones/{query_params['instituciones']}/componentes"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)


    # ----------------------------------------
    # Balance Mensual de Bancos
    # ----------------------------------------
    
    def bs_institucion(self, **query_params):
        """
        Obtiene el balance de una institución con resultados para todos los meses del año especificado.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'year' y 'instituciones'.
    
        Returns:
            dict: Los datos del balance de la institución para todos los meses del año especificado.
        """
        codigo = 'CodigosBalances'
        self.__endpoint_builder(
            self.BALANCES_BANCOS,
            f"/{query_params['year']}/instituciones/{query_params['instituciones']}"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def bs_lista_cuentas(self, **query_params):
        """
        Obtiene la lista de cuentas existentes en el balance durante el mes y el año especificado.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'year' y 'month'.
    
        Returns:
            dict: La lista de cuentas existentes en el balance durante el mes y el año especificado.
        """
        codigo = 'DescripcionesCodigosContables'
        self.__endpoint_builder(
            self.BALANCES_BANCOS, 
            f"/{query_params['year']}/{query_params['month']}/cuentas"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def bs_cuentas_instituciones(self, **query_params):
        """
        Obtiene el detalle de una cuenta del balance durante el año especificado para todas las instituciones.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'year' y 'codigo_cuenta'.
    
        Returns:
            dict: Los datos del detalle de la cuenta del balance durante el año especificado para todas las instituciones.
        """
        codigo = 'CodigosBalances'
        self.__endpoint_builder(
            self.BALANCES_BANCOS,
            f"/{query_params['year']}/cuentas/{query_params['codigo_cuenta']}"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def bs_historico_cuenta_institucion(self, **query_params):
        """
        Obtiene el detalle de una cuenta del balance durante el mes especificado y un periodo predeterminado de años para las instituciones especificadas.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'periodo', 'month', 'codigo_cuenta' e 'instituciones'.
    
        Returns:
            dict: Los datos del detalle de la cuenta del balance durante el mes especificado y el periodo de años para las instituciones especificadas.
        """
        codigo = 'CodigosBalances'
        self.__endpoint_builder(
            self.BALANCES_BANCOS, 
            f"/{query_params['periodo']}/{query_params['month']}/cuentas/{query_params['codigo_cuenta']}/instituciones/{query_params['instituciones']}"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)

    
    # ----------------------------------------
    # Estado de Resultado de Bancos
    # ----------------------------------------
    
    def er_institucion(self, **query_params):
        """
        Obtiene el estado de resultados de una institución para el año especificado.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'year' y 'instituciones'.
    
        Returns:
            dict: Los datos del estado de resultados de la institución para el año especificado.
        """
        codigo = 'CodigosEstadosDeResultado'
        self.__endpoint_builder(
            self.ROOT_ESTADO_RESULTADOS, 
            f"/{query_params['year']}/instituciones/{query_params['instituciones']}"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def er_lista_cuentas(self, **query_params):
        """
        Obtiene la lista de cuentas existentes en el estado de resultados durante el mes y el año especificado.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'year' y 'month'.
    
        Returns:
            dict: La lista de cuentas existentes en el estado de resultados durante el mes y el año especificado.
        """
        codigo = 'DescripcionesCodigosContables'
        self.__endpoint_builder(
            self.ROOT_ESTADO_RESULTADOS, 
            f"/{query_params['year']}/{query_params['month']}/cuentas"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def er_cuenta_instituciones(self, **query_params):
        """
        Obtiene el detalle de una cuenta del estado de resultados durante el mes y el año especificado para todas las instituciones.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'year', 'month' y 'codigo_cuenta'.
    
        Returns:
            dict: Los datos del detalle de la cuenta del estado de resultados durante el mes y el año especificado para todas las instituciones.
        """
        codigo = 'CodigosEstadosDeResultado'
        self.__endpoint_builder(
            self.ROOT_ESTADO_RESULTADOS, 
            f"/{query_params['year']}/{query_params['month']}/cuentas/{query_params['codigo_cuenta']}"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)


    # ----------------------------------------
    # Fichas Bancarias
    # ----------------------------------------
    
    def fb_perfil_institucion(self, **query_params):
        """
        Obtiene el perfil de una institución financiera para el año y mes especificados.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'instituciones', 'year' y 'month'.
    
        Returns:
            dict: Los datos del perfil de la institución financiera para el año y mes especificados.
        """
        codigo = 'Perfiles'
        self.__endpoint_builder(
            self.ROOT_FICHAS, 
            f"/perfil/instituciones/{query_params['instituciones']}/{query_params['year']}/{query_params['month']}"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def fb_accionistas_institucion(self, **query_params):
        """
        Obtiene los accionistas de una institución financiera para el año y mes especificados.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'instituciones', 'year' y 'month'.
    
        Returns:
            dict: Los datos de los accionistas de la institución financiera para el año y mes especificados.
        """
        codigo = 'Accionistas'
        self.__endpoint_builder(
            self.ROOT_FICHAS, 
            f"/accionistas/instituciones/{query_params['instituciones']}/anhos/{query_params['year']}/meses/{query_params['month']}/ficha"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def fb_ejecutivos_institucion(self, **query_params):
        """
        Obtiene los ejecutivos principales de una institución financiera para el año y mes especificados.
    
        Args:
            query_params: Parámetros adicionales de consulta, incluyendo 'instituciones', 'year' y 'month'.
    
        Returns:
            dict: Los datos de los ejecutivos principales de la institución financiera para el año y mes especificados.
        """
        codigo = 'Integrantes'
        self.__endpoint_builder(
            self.ROOT_FICHAS, 
            f"/integrantes/instituciones/{query_params['instituciones']}/anhos/{query_params['year']}/meses/{query_params['month']}"
        )
        return super().handle_request(self.URL_CALL, query_params, codigo)