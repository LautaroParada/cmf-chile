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
        
    def get_dolares(self, codigo:str='Dolares', **query_params):
        
        # Condiciones logicas
        today_ = datetime.today()
        year_ago = today_ - relativedelta(years=1)
        
        # imputar las fechas si es que el usuario no las ingresa
        if query_params['from_'] is None:
            query_params['from_'] = year_ago.strftime('%Y/%m/%d')
            year_i = query_params['from_'][:4]
            month_i = query_params['from_'][5:7]
            day_i = query_params['from_'][-2:]
            
        if query_params['to_'] is None:
            query_params['to_'] = today_.strftime('%Y/%m/%d')
            year_f = query_params['to_'][:4]
            month_f = query_params['to_'][5:7]
            day_f = query_params['to_'][-2:]
         
        self.endpoint = f"https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/periodo/{year_i}/{month_i}/dias_i/{day_i}/{year_f}/{month_f}/dias_f/{day_f}"
        return super().handle_request(self.endpoint, query_params, codigo)