# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:22:42 2022

@author: lauta
"""

import requests
from typing import Dict

class RequestHandler():
    def __init__(self, api_key:str, timeout:int):
        # parametros generales de la api
        self.api_key = api_key
        self.timeout = timeout
        self.resp = None # respuesta para el usuario
        
    # ---------------------------
    # Metodos para el procesamiento de las respuestas
    # ---------------------------
    
    def handle_request(self, endpoint_url, query_params: Dict[str, str], codigo:str):
        
        # Concatenar los parametros de la solicitud
        query_params_ = self.__append_fmt(query_params)
        
        self.resp = requests.get(
                url = endpoint_url,
                params = query_params_,
                timeout = self.timeout
            )
        
        # Manejo de errores
        if self.resp.status_code == 200:
            # la serie viene con un codigo de "cabecera" segun sea lo que se solicite
            # ver cada metodo para la definicion de cada codigo
            return self.resp.json()[codigo]
        else:
            self.resp.raise_for_status()
        
    def __append_fmt(self, dict_to_append):
        """
        Metodo para forzar una salida en JSON

        Parameters
        ----------
        dict_to_append : dict
            Parametros de la solicitud.

        Returns
        -------
        dict_to_append : dict
            Diccionario completo para estandarizar la respuesta a JSON.

        """
        # agregar estas claves y valores al diccionario que venga de la solicitud
        dict_to_append['formato'] = 'json'
        dict_to_append['apikey'] = self.api_key
        
        # referencias para los indicadores financieros
        # borrar los rango de fechas debido a que no sirven como parametro de la solicitud
        # Se verifica si la clave existe en el diccionario
        if 'from_' in dict_to_append:
            del dict_to_append['from_']
            
        if 'to_' in dict_to_append:
            del dict_to_append['to_']
        
            
        return dict_to_append