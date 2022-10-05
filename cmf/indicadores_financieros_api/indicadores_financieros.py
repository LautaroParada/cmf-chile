# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:28:20 2022

@author: lauta
"""

from cmf.request_handler_class import RequestHandler
from dateutil.relativedelta import relativedelta
from datetime import datetime

class IndicadoresFinancierosChilenos(RequestHandler):
    def __init__(self, api_key:str, timeout:str):
        super().__init__(api_key, timeout)
        
    def __validador_fechas(self, dates_dict, freq:str='D'):
        
        # Condiciones logicas
        today_ = datetime.today()
        year_ago = today_ - relativedelta(years=1)
        
        if freq == 'D':            
            # Si es que el diccionario esta vacio
            if len(dates_dict) == 0:
                print('entro al caso base')
                dates_dict['from_'] = year_ago.strftime('%Y/%m/%d')            
                dates_dict['to_'] = today_.strftime('%Y/%m/%d')
        
            else:
                # si falta el "desde"
                if 'from_' not in dates_dict:
                    print('NO detecto el from_')
                    # verificar si el "to_ es menor que le fecha de hoy
                    if today_ > datetime.strptime(dates_dict['to_'], "%Y/%m/%d"):
                        # si la fecha "hasta" es menor que la fecha actual
                        # ocupar la fecha propuesta por el usuario y restar un año a esa fecha
                        new_today = datetime.strptime(dates_dict['to_'], "%Y/%m/%d")
                        dates_dict['from_'] = (new_today - relativedelta(years=1)).strftime('%Y/%m/%d')
                    
                    else:
                        # en otro caso, mantener la fecha y restar un año
                        dates_dict['from_'] = year_ago.strftime('%Y/%m/%d')
                
                # si falta el "hasta"
                if 'to_' not in dates_dict:
                    print('NO detecto el to_')
                    dates_dict['to_'] = today_.strftime('%Y/%m/%d')
                    
        elif freq == 'M':
            # Si es que el diccionario esta vacio
            if len(dates_dict) == 0:
                print('Entro al caso base mensual')
                dates_dict['from_'] = year_ago.strftime('%Y/%m')
                dates_dict['to_'] = today_.strftime('%Y/%m')
                
            else:
                # si falta el "desde"
                if 'from_' not in dates_dict:
                    print('No detecto el from_ en el caso mensual')
                    # verificar si el "to_" es menor que el mes solicitado por el usuario
                    if today_ > datetime.strptime(dates_dict['to_'], '%Y/%m'):
                        new_today = datetime.strptime(dates_dict['to_'], "%Y/%m")
                        dates_dict['from_'] = (new_today - relativedelta(years=1)).strftime("%Y/%m")
                        
                    else:
                        dates_dict['from_'] = year_ago.strftime("%Y/%m")
                
                # si falta el "hasta"
                if 'to_' not in dates_dict:
                    print("NO detecto el to_ mensual")
                    dates_dict['to_'] = today_.strftime('%Y/%m')
            
                
        return dates_dict
    
    def __endpoint_builder(self, root, dates_dict_, freq:str='D'):
        
        if freq == 'D':
            return root.format(
                # elementos de la fecha inicial
                dates_dict_['from_'][:4],
                dates_dict_['from_'][5:7],
                dates_dict_['from_'][-2:],
                # Elementos de la fecha final
                dates_dict_['to_'][:4],
                dates_dict_['to_'][5:7],
                dates_dict_['to_'][-2:]
                )
        
        elif freq == 'M':
            return root.format(
                # elementos de la fecha inicial
                dates_dict_['from_'][:4],
                dates_dict_['from_'][5:7],
                # Elementos de la fecha final
                dates_dict_['to_'][:4],
                dates_dict_['to_'][5:7]
                )
        
    def get_dolares(self, codigo:str='Dolares', **query_params):        
        query_params_ = self.__validador_fechas(query_params)     
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/periodo/{}/{}/dias_i/{}/{}/{}/dias_f/{}",
            query_params_
            )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_euros(self, codigo:str='Euros', **query_params):
        query_params_ = self.__validador_fechas(query_params)
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/euro/periodo/{}/{}/dias_i/{}/{}/{}/dias_f/{}",
            query_params_
            )
        return super().handle_request(self.endpoint, query_params, codigo)
    
    def get_ipc(self, codigo:str='IPCs', **query_params):
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/ipc/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
            )
        return super().handle_request(self.endpoint, query_params, codigo)