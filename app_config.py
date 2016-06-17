from flask import Flask
from suds.client import Client


data_url = 'http://115.28.206.58:8080/bank'
buss_url = 'http://localhost:7789'
app = Flask(__name__, static_url_path='/static')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
soap_client = Client(buss_url + '/?wsdl')
