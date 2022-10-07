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
resp = cliente.get_euros(to_='2005/05/17')
resp = cliente.get_ipc(to_='2009/05', from_='2000/01')
resp = cliente.get_tip()
resp = cliente.get_codigos()
resp = cliente.get_tmc(to_='2000/01', from_='1998/01')
resp = cliente.get_uf()
resp = cliente.get_utm()

#%% Testeando los reportes bancarios

resp = cliente.ac_capital_basico(cantidad='30', instituciones='001')
resp = cliente.ac_patrimonio_efectivo(cantidad='30', instituciones='001')
resp = cliente.ac_riesgo_credito(cantidad='30', instituciones='001')
resp = cliente.ac_capital_activos(cantidad='30', instituciones='001')
