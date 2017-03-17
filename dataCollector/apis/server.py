#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-17 10:17:49
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import Flask
from apiServer import typhoon_list

app = Flask(__name__)
app.register_blueprint(typhoon_list)


if __name__ == '__main__':
    app.run(debug=True,port=44444)
