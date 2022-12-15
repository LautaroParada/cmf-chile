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
        self.BALANCES_BANCOS = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/balances'
        self.ROOT_FICHAS = 'https://api.cmfchile.cl/api-sbifv3/recursos_api'
        self.ROOT_ESTADO_RESULTADOS = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/resultados'
        
        
    # ----------------------------------------
    # Metodos de ayuda para el manejo de casos
    # ----------------------------------------
    
    def __endpoint_builder(self, root:str, endpoint:str):
        self.URL_CALL = f"{root}{endpoint}"
        
    def instituciones_bancarias(self):
        bancos_chilenos = {
            'Nombre':[
                'BANCO DE CHILE',
                'BANCO INTERNACIONAL',
                'SCOTIABANK CHILE',
                'BANCO DE CREDITO E INVERSIONES',
                'BANCO BICE',
                'HSBC BANK',
                'BANCO SANTANDER-CHILE',
                'ITAÚ CORPBANCA',
                'BANCO SECURITY',
                'BANCO FALABELLA',
                'BANCO RIPLEY',
                'BANCO CONSORCIO',
                'SCOTIABANK AZUL',
                'BANCO BTG PACTUAL CHILE',
                # Bancos Extranjeros
                'BANCO DO BRASIL S.A.',
                'JP MORGAN CHASE BANK, N. A.',
                'BANCO DE LA NACION ARGENTINA',
                'MUFG Bank, Ltd.',
                'CHINA CONSTRUCTION BANK, AGENCIA EN CHILE',
                'BANK OF CHINA, AGENCIA EN CHILE',
                # Bancos Estatales
                'BANCO DEL ESTADO DE CHILE'
                ],
            'CodigoSBIF': [
                '001','009','014','016','028','031','037','039','049','051',
                '053','055','504','059',
                # Bancos extranjeros
                '017','041','043','045','060','061',
                # Bancos Estatales
                '012'                
                ],
            'Tipo':[
                'ECH','ECH','ECH','ECH','ECH','ECH','ECH','ECH','ECH','ECH',
                'ECH','ECH','ECH','ECH',
                # Bancos Extranjeros
                'SBE','SBE','SBE','SBE','SBE','SBE',
                # Bancos Estatales
                'BET'
                ],
            'OperacionConjunta':[
                'Banco Edwards, Citi, Atlas y CrediChile',
                '',
                'BancoDesarrollo','TBanc y Banco Nova','','','Banefe',
                'Desde el 1 de abril de 2016 se fusiona el Banco Corpbanca en Itaú Corpbanca.',
                '','','','','','',
                # Bancos Extranjeros
                '','','','Hasta el 1 de Abril de 2018 operó con el nombre The Bank of Tokyo-Mitsubishi UFJ, Ltd.',
                '','',
                # Bancos Estatales
                ''
                ]
            }
        
        return bancos_chilenos
        
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
        codigo = 'CodigosEstadosDeResultado'
        self.__endpoint_builder(
            self.ROOT_ESTADO_RESULTADOS, 
            f"/{query_params['year']}/instituciones/{query_params['instituciones']}"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def er_lista_cuentas(self, **query_params):
        codigo = 'DescripcionesCodigosContables'
        self.__endpoint_builder(
            self.ROOT_ESTADO_RESULTADOS, 
            f"/{query_params['year']}/{query_params['month']}/cuentas"
            )
        return super().handle_request(self.URL_CALL, query_params, codigo)
    
    def er_cuenta_instituciones(self, **query_params):
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