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
    
    def __endpoint_builder(self, root, endpoint):
        self.URL_CALL = f"{root}/{endpoint}"
        
        