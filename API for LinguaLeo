import json
from http.cookiejar import CookieJar
import sys
import urllib
import httplib2
import urllib3
import requests
from http.client import HTTPSConnection
login = ..."
password = "..."
API_URL = "https://api.lingualeo.com/"
response = requests.Session()
auth_status = None

#LogIn function
def auth(login, password):
    urlParameters = "email=" + login + "&password=" + password
    requestUrl = API_URL + "login"
    postData = urlParameters.encode('utf-8')
    postDataLength = str(len(postData))
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Content-Length": postDataLength}
    auth_function = response.post(url=requestUrl, data = postData, headers=headers, allow_redirects = False)
    global auth_status
    if auth_function.status_code == 200:
        auth_status = True
        print("Successful authentification")
    else:
        auth_status = False
        print("Authentification Failed. Check your login and password and try again")

#Function of using internal API for word translation
def translation(word):
    requestUrl = API_URL + "gettranslates" +"?" + "word=" + word
    translate = response.get(url=requestUrl,  allow_redirects = False, stream = True)
    translate = translate.json()
    translate = translate["translate"][0]['translate_value']
    return translate

#Function of using yandex api to translate, now is paid
def Ytranslate(word):
    API_URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    API_key = "..."
    requestUrl = API_URL + "?" +"key="+ API_key + "&"+ "text=" + word + "&" +  "lang=en-ru"
    translate = response.get(url=requestUrl,  allow_redirects = False, stream = True)
    translate = translate.json()
    translate = translate['text']
    translate=translate[0]
    return translate

#Function of using internal API to add word to LinguaLeo dictionary
def add_word(word, translate):
    if auth_status == False or auth_status == None:
        print("plase, run auth")
    else:
        urlParameters = "word=" + word + "&tword=" + translate + "&context="
        requestUrl = API_URL + "addword"
        postData = urlParameters.encode('utf-8')
        postDataLength = str(len(postData))
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Content-Length": postDataLength}
        add = response.post(url=requestUrl, headers = headers, data = postData, allow_redirects = False, stream = True)
        if add.status_code != 200: print("Fail")
