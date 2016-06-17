from flask import Blueprint, render_template
import requests
import json
from app_config import soap_client, data_url

bank_bp = Blueprint('bank', __name__)


def req_text(url, *args):
    req = requests.get(url.format(*args))
    return req.text


@bank_bp.route('')
@bank_bp.route('/index/')
def index():
    return render_template('Index.html')


@bank_bp.route('/check_bank/<int:bank_id>/', methods=['GET'])
def check_bank(bank_id):
    return req_text('{0}/check_bank/{1}/', data_url, str(bank_id))


@bank_bp.route('/check_bank/<int:bank_id>/', methods=['PUT'])
def update_bank(bank_id):
    resp = requests.put('{0}/check_bank/{1}/'.format(data_url, str(bank_id)))
    return resp.text


@bank_bp.route('/get_records/<int:bank_id>/<int:page_num>/<int:page_size>/')
def get_records(bank_id, page_num, page_size):
    return req_text('{0}/get_records/{1}/{2}/{3}/', data_url, str(bank_id), str(page_num), str(page_size))


@bank_bp.route('/get_detail/<string:ID>/')
def get_detail(ID):
    return req_text('{0}/get_detail/{1}/', data_url, ID)


@bank_bp.route('/get_plan/<string:bank_id>/<int:money>/<int:day>/<string:curr>/')
@bank_bp.route('/get_plan/<string:bank_id>/<float:money>/<int:day>/<string:curr>/')
def get_plan(bank_id, money, day, curr):
    result = soap_client.service.get_best_plan(money, day, bank_id, curr)
    return result
