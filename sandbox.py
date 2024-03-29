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
resp = cliente.get_tmc(to_='2000/01', from_='1998/01')
resp = cliente.get_uf()
resp = cliente.get_utm()

#%% Testeando los reportes bancarios

# Bancos Disponibles para el mercado chileno
resp = cliente.instituciones_bancarias()

# Adecuacion de capital - EL ULTIMO MES DISPONIBLE ES 2020/11
resp = cliente.ac_capital_basico(cantidad='12', instituciones='001')
resp = cliente.ac_patrimonio_efectivo(cantidad='30', instituciones='001')
resp = cliente.ac_riesgo_credito(cantidad='30', instituciones='001')
resp = cliente.ac_capital_activos(cantidad='30', instituciones='001')
resp = cliente.ac_componentes_todos(year='2020', month='11', instituciones='001')

# Balances bancarios
resp = cliente.bs_institucion(instituciones='001', year='2023') # Timeout error
resp = cliente.bs_lista_cuentas(year='2022', month='09') # funciona con 1 o 2 meses de retraso
resp = cliente.bs_cuentas_instituciones(year='2022', codigo_cuenta='246000304')
resp = cliente.bs_historico_cuenta_institucion(periodo='periodo3', month='06', 
                                              codigo_cuenta='246000304',
                                              instituciones='001')

# Estado de Resultados
resp = cliente.er_institucion(instituciones='001', year='2022') # Timeout error
resp = cliente.er_lista_cuentas(year='2023', month='01')
resp = cliente.er_cuenta_instituciones(year='2023', month='01', codigo_cuenta='431850214')

# Fichas Bancarias
resp = cliente.fb_perfil_institucion(year='2022', month='10', instituciones='001')
resp = cliente.fb_accionistas_institucion(year='2022', month='10', instituciones='001')
resp = cliente.fb_ejecutivos_institucion(year='2022', month='10', instituciones='001')
