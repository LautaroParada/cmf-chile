# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:24:05 2022

@author: lauta
"""

import os
api_key_ = os.environ['API_CMF']

from cmf import CmfBancos
cliente = CmfBancos(api_key_)

#%% Testeando los indicadores financieros

# Casos del dolar
# Sin argumentos
# Solo con from_ -> desde el from_ hasta la fecha de hoy
# Solo con to_ -> si el to_ es menor a hoy, se ocupa el to_ como "hoy" y se le resta un año
# Ambos -> El from_ debe ser menor que el to_ 
resp = cliente.get_dolares(to_='2012/09/18', from_='2005/10/24')
