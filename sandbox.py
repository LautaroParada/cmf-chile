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
# sin argumentos
resp = cliente.get_dolares()
