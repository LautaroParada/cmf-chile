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
        
    # ----------------------------------------
    # Metodos de ayuda para el manejo de casos
    # ----------------------------------------
        
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
    
    # ----------------------------------------
    # Metodos para solicitar datos a la API
    # ----------------------------------------
        
    def get_dolares(self, **query_params):
        codigo = 'Dolares'
        query_params_ = self.__validador_fechas(query_params)     
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/periodo/{}/{}/dias_i/{}/{}/{}/dias_f/{}",
            query_params_
            )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_euros(self, **query_params):
        codigo = 'Euros'
        query_params_ = self.__validador_fechas(query_params)
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/euro/periodo/{}/{}/dias_i/{}/{}/{}/dias_f/{}",
            query_params_
            )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_ipc(self, **query_params):
        codigo = 'IPCs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/ipc/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
            )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_tip(self, **query_params):
        codigo = 'TIPs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/tip/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
            )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_codigos(self):
        codigos_tip = {
            '1':'Operaciones no reajustables en moneda nacional',
            '2':'Operaciones no reajustables en moneda nacional de menos de 90 días - de menos de 90 días',
            '3':'Operaciones no reajustables en moneda nacional 90 días o más - de 90 días o más',
            '4':'Operaciones no reajustables en moneda nacional 90 días o más - Inferiores o iguales al equivalente de 100 unidades de fomento',
            '5':'Operaciones no reajustables en moneda nacional 90 días o más - Inferiores o iguales al equivalente de 200 unidades de fomento y superiores al equivalente de 100',
            '6':'Operaciones no reajustables en moneda nacional 90 días o más - Superiores al equivalente de 200 unidades de fomento',
            '7':'Operaciones no reajustables en moneda nacional 90 días o más - Inferiores o iguales al equivalente de 200 unidades de fomento',
            '8':'Operaciones no reajustables en moneda nacional 90 días o más - Inferiores o iguales al equivalente de 5.000 unidades de fomento y superiores al equivalente de 200',
            '9':'Operaciones no reajustables en moneda nacional 90 días o más - Superiores al equivalente de 5.000 unidades de fomento',
            '10':'Operaciones no reajustable en moneda nacional menores de 90 días - Inferiores al equivalente de 5.000 unidades de fomento',
            '11':'Operaciones no reajustable en moneda nacional menores de 90 días - Superiores al equivalente de 5.000 unidades de fomento',
            '12':'Operaciones reajustables en moneda nacional Menores a un año',
            '13':'Operaciones reajustables en moneda nacional De un año o más. Inferiores o iguales al equivalente de 2000 unidades de fomento',
            '14':'Operaciones reajustables en moneda nacional De un año o más. Superiores al equivalente de 2000 unidades de fomento',
            '15':'Operaciones reajustables en moneda nacional Expresadas en Moneda Extranjera',
            '20':'Operaciones reajustables en moneda nacional De un año o más.',
            '21':'Operaciones reajustables en moneda nacional Menores a un año',
            '22':'Operaciones reajustables en moneda nacional De un año o más. Superiores al equivalente de 2000 unidades de fomento',
            '23':'Operaciones reajustables en moneda nacional De un año o más',
            '24':'Operaciones reajustables en moneda nacional De un año o más. Inferiores o iguales al equivalente de 2000 unidades de fomento',
            '25':'Operaciones no reajustables en moneda nacional de menos de 90 días Superiores al equivalente de 5.000 unidades de fomento',
            '26':'Operaciones no reajustables en moneda nacional de menos de 90 días Inferiores o iguales al equivalente de 5.000 unidades de fomento',
            '27':'Operaciones no reajustables en moneda nacional de 90 días o más - Inferiores o iguales al equivalente de 5.000 unidades de fomento y superiores al equivalente de 200 unidades de fomento',
            '28':'Operaciones no reajustables en moneda nacional de 90 días o más - Inferiores o iguales al equivalente de 100 unidades de fomento',
            '29':'Operaciones no reajustables en moneda nacional de 90 días o más - Superiores al equivalente de 5.000 unidades de fomento',
            '30':'Operaciones no reajustables en moneda nacional de 90 días o más - Inferiores o iguales al equivalente de 200 unidades de fomento',
            '31':'Operaciones no reajustables en moneda nacional de 90 días o más - Inferiores o iguales al equivalente de 200 unidades de fomento y superiores al equivalente de 100 unidades de fomento',
            '32':'Operaciones no reajustables en moneda nacional de 90 días o más - Superiores al equivalente de 200 unidades de fomento',
            '33':'Operaciones no reajustables en moneda nacional 90 días o más - Inferiores o iguales al equivalente de 200 unidades de fomento',
            '34':'Operaciones no reajustables en moneda nacional 90 días o más - Superiores al equivalente de 5.000 unidades de fomento',
            '35':'Operaciones no reajustables en moneda nacional 90 días o más - Inferiores o iguales al equivalente de 5.000 unidades de fomento y superiores al equivalente de 200 unidades de fomento',
            '36':'Operaciones expresadas en moneda extranjera',
            '37':'Operaciones no reajustables en moneda nacional de menos de 90 días',
            '38':' Operaciones en dólares de EE.UU. o expresadas en moneda extranjera',
            '39':'Operaciones no reajustables en moneda nacional de 90 días o más',
            '40':'Operaciones reajustables en moneda nacional',
            '41':'Operaciones expresadas en moneda extranjera Inferiores o iguales al equivalente de 2.000 unidades de fomento',
            '42':'Operaciones expresadas en moneda extranjera Superiores al equivalente de 2.000 unidades de fomento',
            '43':'Operaciones cuyo mecanismo de pago consista en la deducción de las respectivas cuotas directamente de la pensión del deudor',
            '44':'Operaciones no reajustables en moneda nacional 90 días o más - Inferiores o iguales al equivalente de 200 unidades de fomento y superiores al equivalente de 50 unidades de fomento',
            '45':'Operaciones no reajustables en moneda nacional 90 días o más - Inferiores o iguales al equivalente de 50 unidades de fomento',
            }
        
        return codigos_tip
    
    def get_tmc(self, **query_params):
        codigo = 'TMCs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/tmc/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
            )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_uf(self, **query_params):
        codigo = 'UFs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/uf/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
            )
        return super().handle_request(self.endpoint, query_params_, codigo)
    
    def get_utm(self, **query_params):
        codigo = 'UTMs'
        query_params_ = self.__validador_fechas(query_params, freq='M')
        self.endpoint = self.__endpoint_builder(
            "https://api.cmfchile.cl/api-sbifv3/recursos_api/utm/periodo/{}/{}/{}/{}",
            query_params_,
            freq='M'
            )
        return super().handle_request(self.endpoint, query_params_, codigo)