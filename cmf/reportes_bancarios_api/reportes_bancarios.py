# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 08:26:36 2022

@author: lauta
"""

from cmf.request_handler_class import RequestHandler

class ReportesBancariosChilenos(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        super().__init__(api_key, timeout)
        # URL raices de cada endpoint
        self.URL_CALL = None # ruta final para solicitar datos a la API
        self.ROOT_ADECUACION = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/adecuacion'
        
        
    # ----------------------------------------
    # Metodos de ayuda para el manejo de casos
    # ----------------------------------------
    
    def __endpoint_builder(self, root:str, endpoint:str):
        self.URL_CALL = f"{root}{endpoint}"
        
    # ----------------------------------------
    # Metodos para solicitar datos a la API
    # ----------------------------------------
    
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
    
    def ac_limite_patrimonio(self, **query_params):
        codigo = 'AdecuacionDeCapital'
        self.__endpoint_builder(
            self.ROOT_ADECUACION, 
            f"/anhos/{query_params['year']}/meses/{query_params['month']}/instituciones/{query_params['instituciones']}/componentes/limites"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)