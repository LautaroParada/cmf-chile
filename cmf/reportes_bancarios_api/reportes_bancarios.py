# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 08:26:36 2022

@author: lauta
"""

from cmf.request_handler_class import RequestHandler
from datetime import datetime, timedelta

class ReportesBancariosChilenos(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
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
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/regresionmensual/{query_params['cantidad']}/instituciones/{query_params['instituciones']}/indicadores/capbas"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def ac_patrimonio_efectivo(self, **query_params):
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/regresionmensual/{query_params['cantidad']}/instituciones/{query_params['instituciones']}/indicadores/patefe"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def ac_riesgo_credito(self, **query_params):
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/regresionmensual/{query_params['cantidad']}/instituciones/{query_params['instituciones']}/indicadores/irs"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def ac_capital_activos(self, **query_params):
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/regresionmensual/{query_params['cantidad']}/instituciones/{query_params['instituciones']}/indicadores/ire"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def ac_componentes_todos(self, **query_params):
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
        codigo = 'CodigosBalances'
        self.__endpoint_builder(
            self.BALANCES_BANCOS,
            f"/{query_params['year']}/instituciones/{query_params['instituciones']}"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def bs_lista_cuentas(self, **query_params):
        codigo = 'DescripcionesCodigosContables'
        self.__endpoint_builder(
            self.BALANCES_BANCOS, 
            f"/{query_params['year']}/{query_params['month']}/cuentas"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def bs_cuentas_instituciones(self, **query_params):
        codigo = 'CodigosBalances'
        self.__endpoint_builder(
            self.BALANCES_BANCOS,
            f"/{query_params['year']}/cuentas/{query_params['codigo_cuenta']}"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def bs_historico_cuenta_institucion(self, **query_params):
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
        Estado de Resultados de una institución para el año especificado
        """
        codigo = 'CodigosEstadosDeResultado'
        self.__endpoint_builder(
            self.ROOT_ESTADO_RESULTADOS, 
            f"/{query_params['year']}/instituciones/{query_params['instituciones']}"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def er_lista_cuentas(self, **query_params):
        """
        Lista de cuentas existentes en el Estado de Resultados durante el mes 
        del año especificado

        """
        codigo = 'DescripcionesCodigosContables'
        self.__endpoint_builder(
            self.ROOT_ESTADO_RESULTADOS, 
            f"/{query_params['year']}/{query_params['month']}/cuentas"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def er_cuenta_instituciones(self, **query_params):
        """
        Detalle de una cuenta del Estado de Resultados durante el mes del año 
        especificado para todas las instituciones
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
        codigo = 'Perfiles'
        self.__endpoint_builder(
            self.ROOT_FICHAS, 
            f"/perfil/instituciones/{query_params['instituciones']}/{query_params['year']}/{query_params['month']}"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def fb_accionistas_institucion(self, **query_params):
        codigo = 'Accionistas'
        self.__endpoint_builder(
            self.ROOT_FICHAS, 
            f"/accionistas/instituciones/{query_params['instituciones']}/anhos/{query_params['year']}/meses/{query_params['month']}/ficha"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def fb_ejecutivos_institucion(self, **query_params):
        codigo = 'Integrantes'
        self.__endpoint_builder(
            self.ROOT_FICHAS, 
            f"/integrantes/instituciones/{query_params['instituciones']}/anhos/{query_params['year']}/meses/{query_params['month']}"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)