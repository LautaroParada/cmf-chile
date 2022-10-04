# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:22:42 2022

@author: lauta
"""

import requests
from typing import Dict

class RequestHandler():
    def __init__(self, api_key:str):
        # parametros generales de la api
        self.api_key = api_key
        self.resp = None # respuesta para el usuario