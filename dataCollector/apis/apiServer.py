#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-17 10:14:34
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask.blueprints import Blueprint
from flask_restful import Resource, Api
from pymongo import MongoClient
from flask import jsonify, make_response

typhoon_list = Blueprint('typhoon', __name__)
typhoon_api = Api(typhoon_list)


class Typhoon(Resource):
    def __init__(self):
        self._mongoCli = MongoClient(host='localhost', port=27017)
        self._db = self._mongoCli['nmc']
        self._col = self._db['typhoon']

    def get(self, year):
        results = self._col.find({'year': year}, {"_id": 0})
        response = make_response(jsonify({'typhoon': list(results)}))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers[
            'Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        return response


class Typhoon_info(Resource):
    """docstring for Typhoon_info"""

    def __init__(self):
        self._mongoCli = MongoClient(host='localhost', port=27017)
        self._db = self._mongoCli['nmc']
        self._col = self._db['typhooninfo']

    def get(self, id):
        results = self._col.find({'typhoonid': id}, {"_id": 0})
        response = make_response(jsonify({'typhooninfo': list(results)}))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers[
            'Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        return response


typhoon_api.add_resource(Typhoon, "/apis/typhoon/<int:year>",
                         endpoint='typhoonlist')

typhoon_api.add_resource(Typhoon_info, "/apis/typhooninfo/<int:id>",
                         endpoint='typhooninfo')