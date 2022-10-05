# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:25:33 2022

@author: lauta
"""

from cmf.indicadores_financieros_api import IndicadoresFinancierosChilenos

class CmfBancos(IndicadoresFinancierosChilenos):
    def __init__(self, api_key:str, timeout:int=300):
        # heredar las clases importadas
        IndicadoresFinancierosChilenos.__init__(self, api_key, timeout)