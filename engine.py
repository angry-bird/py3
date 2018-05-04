#!usr/bin/env python
# -*-coding:utf-8 -*-

'''
| author: zuoshi300@qq.com
| date: 05/02/2018
| desc: search with api on zoomeye, shodan and censys
| version: 0.1
'''

import os
import configparser
import requests
import json
import math

class engine:
    file_conf = 'config.ini'

    def __init__(self, credent ,keyword):
        self.credent = credent
        self.keyword = keyword

    def getHeader(self):
        pass
    def searchKeyword(self, keyword):
        pass

class zoomeye(engine):
    __apiURL = 'https://api.zoomeye.org/'
    resourceURL = __apiURL + 'resources-info'
    queryWebURL = __apiURL + 'web/search?query='
    queryHostURL = __apiURL + 'host/search?query='
    loginURL = __apiURL + 'user/login'
    pass
    # def __init__(self, user, passwd):
    #     self.user = user
    #     self.passwd = passwd
    def getConf(self):
        conf = configparser.ConfigParser()
        conf.read(file_conf)
        return token

demo = zoomeye('root', 'weblogit')
demo.loginURL = demo.queryHostURL
print (demo.loginURL)
