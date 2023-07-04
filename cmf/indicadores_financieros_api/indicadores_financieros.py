# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:28:20 2022

@author: lauta
"""

from cmf.request_handler_class import RequestHandler
from dateutil.relativedelta import relativedelta
from datetime import datetime

class IndicadoresFinancierosChilenos(RequestHandler):
    def __init__(self, api_key:str, timeout:int):
        super().__init__(api_key, timeout)
        
    # ----------------------------------------
    # Metodos de ayuda para el manejo de casos
    # ----------------------------------------
        
    def __validador_fechas(self, dates_dict, freq: str = 'D'):
        """
        Valida y completa un diccionario de fechas según la frecuencia especificada.
    
        Args:
            dates_dict (dict): El diccionario de fechas a validar y completar.
            freq (str, optional): La frecuencia de las fechas ('D' para días o 'M' para meses). 
                Por defecto, es 'D'.
    
        Returns:
            dict: El diccionario de fechas actualizado y completo.
    
        Raises:
            ValueError: Si se proporciona una frecuencia inválida.
    
        """
        today = datetime.today()  # Fecha actual
        year_ago = today - relativedelta(years=1)  # Fecha de hace un año
    
        if freq == 'D':  # Validación para frecuencia diaria
            if 'from_' not in dates_dict:  # Si falta la clave 'from_'
                if 'to_' in dates_dict and today > datetime.strptime(dates_dict['to_'], "%Y/%m/%d"):
                    # Si existe la clave 'to_' y la fecha 'to_' es mayor que la fecha actual
                    new_today = datetime.strptime(dates_dict['to_'], "%Y/%m/%d")
                    dates_dict['from_'] = (new_today - relativedelta(years=1)).strftime('%Y/%m/%d')
                else:
                    # Si no existe la clave 'to_' o la fecha 'to_' es menor o igual a la fecha actual
                    dates_dict['from_'] = year_ago.strftime('%Y/%m/%d')
    
            if 'to_' not in dates_dict:  # Si falta la clave 'to_'
                dates_dict['to_'] = today.strftime('%Y/%m/%d')  # Asignar fecha actual
    
        elif freq == 'M':  # Validación para frecuencia mensual
            if 'from_' not in dates_dict:  # Si falta la clave 'from_'
                if 'to_' in dates_dict and today > datetime.strptime(dates_dict['to_'], '%Y/%m'):
                    # Si existe la clave 'to_' y la fecha 'to_' es mayor que el mes actual
                    new_today = datetime.strptime(dates_dict['to_'], "%Y/%m")
                    dates_dict['from_'] = (new_today - relativedelta(years=1)).strftime('%Y/%m')
                else:
                    # Si no existe la clave 'to_' o la fecha 'to_' es menor o igual al mes actual
                    dates_dict['from_'] = year_ago.strftime('%Y/%m')
    
            if 'to_' not in dates_dict:  # Si falta la clave 'to_'
                dates_dict['to_'] = today.strftime('%Y/%m')  # Asignar mes actual
    
        else:
            raise ValueError("Frecuencia inválida. La frecuencia debe ser 'D' para días o 'M' para meses.")
    
        return dates_dict

    
    def __endpoint_builder(self, root, dates_dict_, freq: str = 'D'):
        """
        Construye el endpoint para la API según el formato de fechas especificado.
    
        Args:
            root (str): El root del endpoint.
            dates_dict_ (dict): El diccionario de fechas.
            freq (str, optional): La frecuencia de las fechas ('D' para días o 'M' para meses). 
                Por defecto, es 'D'.
    
        Returns:
            str: El endpoint construido con las fechas correspondientes.
    
        """
        if freq == 'D':  # Construcción de endpoint para frecuencia diaria
            return root.format(
                # Elementos de la fecha inicial
                dates_dict_['from_'][:4],  # Año inicial
                dates_dict_['from_'][5:7],  # Mes inicial
                dates_dict_['from_'][-2:],  # Día inicial
                # Elementos de la fecha final
                dates_dict_['to_'][:4],  # Año final
                dates_dict_['to_'][5:7],  # Mes final
                dates_dict_['to_'][-2:]  # Día final
            )
    
        elif freq == 'M':  # Construcción de endpoint para frecuencia mensual
            return root.format(
                # Elementos de la fecha inicial
                dates_dict_['from_'][:4],  # Año inicial
                dates_dict_['from_'][5:7],  # Mes inicial
                # Elementos de la fecha final
                dates_dict_['to_'][:4],  # Año final
                dates_dict_['to_'][5:7]  # Mes final
            )
    
    # ----------------------------------------
    # Metodos para solicitar datos a la API
    # ----------------------------------------

    def get_dolares(self, **query_params):
        """
        Obtiene los datos de tipo de cambio de dólares para un período y días especificados.
    
        Args:
            **query_params: Los parámetros de consulta, como 'from_' (fecha de inicio) y 'to_' (fecha de fin).
    
        Returns:
            dict: Los datos de tipo de cambio de dólares.
    
        """
        codigo = 'Dolares'
        query_params_ = self.__validador_fechas(query_params)
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/periodo/{}/{}/dias_i/{}/{}/{}/dias_f/{}",
            query_params_
        )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_euros(self, **query_params):
        """
        Obtiene los datos de tipo de cambio de euros para un período y días especificados.
    
        Args:
            **query_params: Los parámetros de consulta, como 'from_' (fecha de inicio) y 'to_' (fecha de fin).
    
        Returns:
            dict: Los datos de tipo de cambio de euros.
    
        """
        codigo = 'Euros'
        query_params_ = self.__validador_fechas(query_params)
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/euro/periodo/{}/{}/dias_i/{}/{}/{}/dias_f/{}",
            query_params_
        )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_ipc(self, **query_params):
        """
        Obtiene los datos del índice de precios al consumidor (IPC) para un período y meses especificados.
    
        Args:
            **query_params: Los parámetros de consulta, como 'from_' (fecha de inicio) y 'to_' (fecha de fin).
    
        Returns:
            dict: Los datos del IPC.
    
        """
        codigo = 'IPCs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/ipc/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
        )
        return super().handle_request(self.endpoint, query_params_, codigo)

    def get_tip(self, **query_params):
        """
        Obtiene los datos de la Tasa de Interés Política Monetaria (TIP) para un período y meses especificados.
    
        Args:
            **query_params: Los parámetros de consulta, como 'from_' (fecha de inicio) y 'to_' (fecha de fin).
    
        Returns:
            dict: Los datos de la TIP.
    
        """
        codigo = 'TIPs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/tip/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
        )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_tmc(self, **query_params):
        """
        Obtiene los datos de la Tasa Máxima Convencional (TMC) para un período y meses especificados.
    
        Args:
            **query_params: Los parámetros de consulta, como 'from_' (fecha de inicio) y 'to_' (fecha de fin).
    
        Returns:
            dict: Los datos de la TMC.
    
        """
        codigo = 'TMCs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/tmc/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
        )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_uf(self, **query_params):
        """
        Obtiene los datos de la Unidad de Fomento (UF) para un período y meses especificados.
    
        Args:
            **query_params: Los parámetros de consulta, como 'from_' (fecha de inicio) y 'to_' (fecha de fin).
    
        Returns:
            dict: Los datos de la UF.
    
        """
        codigo = 'UFs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/uf/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
        )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_utm(self, **query_params):
        """
        Obtiene los datos de la Unidad Tributaria Mensual (UTM) para un período y meses especificados.
    
        Args:
            **query_params: Los parámetros de consulta, como 'from_' (fecha de inicio) y 'to_' (fecha de fin).
    
        Returns:
            dict: Los datos de la UTM.
    
        """
        codigo = 'UTMs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/utm/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
        )
        return super().handle_request(self.endpoint, query_params_, codigo)
