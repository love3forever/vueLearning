#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-16 09:04:07
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from requests import Session
from pymongo import MongoClient
from json import loads
from datetime import datetime, date, time
from time import localtime, strftime
from multiprocessing import Pool


session = Session()
mongocli = MongoClient()
db = mongocli['nmc']
col = db['typhoon']
infocol = db['typhooninfo']


baseUrl = "http://typhoon.nmc.cn/weatherservice/typhoon/jsons/list_{}"
infoUrl = "http://typhoon.nmc.cn/weatherservice/typhoon/jsons/view_{}"

direction_dict = {
    'W': '西',
    'N': '北',
    'S': '南',
    'E': '东'
}

typhoon_dict = {
    'TS': '热带风暴',
    'STS': '强热带风暴',
    'TY': '台风',
    'STY': '强台风',
    'SuperTY': '超强台风',
    'TD': '热带低压',
    '弱于TD': '弱于热带低压'
}


def get_typhoon_data(year):
    '''
    获取1949年至今我国台风记录
    '''
    url = baseUrl.format(year)
    origin_data = session.get(url)
    parsed_data = data_parser(origin_data.content)
    typhoon_list = parsed_data['typhoonList']
    year_data = []
    for item in typhoon_list:
        typhoon_data = {}
        typhoon_data['typhoonid'] = item[0]
        typhoon_data['enname'] = item[1]
        typhoon_data['cnname'] = item[2]
        typhoon_data['seqnum'] = item[3]
        typhoon_data['seqnumstr'] = item[4]
        typhoon_data['nameby'] = item[6]
        typhoon_data['stat'] = item[7]
        typhoon_data['collecttime'] = datetime.now()
        typhoon_data['year'] = year
        year_data.append(typhoon_data)
    col.insert_many(year_data)
    print("{} typhoon data saved!".format(year))


def get_typhoon_info(typhoonid):
    '''
    输入台风id号，将具体信息存入数据库
    '''
    print('inserting typhoon {} data'.format(typhoonid))
    url = infoUrl.format(typhoonid)
    originData = session.get(url)
    parsed_data = data_parser(originData.content)
    typhoon_info = parsed_data['typhoon']
    typhoon_detail = typhoon_info[8]
    data_col = []

    for item in typhoon_detail:
        typhoon_data = {}
        typhoon_data['typhoonid'] = typhoon_info[0]
        typhoon_data['subid'] = item[0]
        typhoon_data['pasttime'] = item[1]
        date_formate = convert_timeformat(item[1])
        typhoon_data['pasttimeiso'] = date_formate[0] if date_formate else None
        typhoon_data['pasttimestr'] = date_formate[1] if date_formate else None

        typhoon_data['movedir'] = parse_direction(item[8])
        typhoon_data['position'] = {
            'type': "Point",
            'coordinates': [item[4] if item[4] < 180 else item[4] - 360, item[5]]
        }
        typhoon_data[
            'positionstr'] = '{}N/{}E'.format(item[5], item[4])
        typhoon_data[
            'topspeed'] = '{}m/s'.format(item[7]) if item[7] != 0 else 0
        typhoon_data['pressure'] = '{}百帕'.format(item[6]) if item[
            6] != 0 else 0
        typhoon_data[
            'movespeed'] = '{}公里/小时'.format(item[9]) if item[9] != 0 else 0

        typhoon_data['class'] = parse_class(item[3])

        typhoon_phrase = item[10]
        if typhoon_phrase:
            typhoon_phrase = map(parse_phrasedata, typhoon_phrase)

        typhoon_data['phrase'] = typhoon_phrase
        infocol.insert_one(typhoon_data)

    print('typhoon {} info saved!'.format(typhoonid))


def convert_timeformat(timestr):
    '''
    将字符串形式时间转为当地时间
    '''
    if timestr:
        year = int(''.join(timestr[0:4]))
        month = int(''.join(timestr[4:6]))
        day = int(''.join(timestr[6:8]))

        hour = int(''.join(timestr[8:10]))
        minute = int(''.join(timestr[10:12])) if len(timestr) > 10 else 0

        d = date(year, month, day)
        t = time(hour, minute)

        date_formate = datetime.combine(d, t)
        return date_formate, date_formate.strftime("%m-%d %H:%M")
    else:
        return None


def parse_class(typhoonclass):
    if typhoonclass not in typhoon_dict.keys():
        return typhoonclass
    return typhoon_dict[typhoonclass]


def parse_direction(dirstr):
    '''
    将NESW转换为对应的方向
    '''
    if dirstr == 'no':
        return None
    direction = []
    for s in dirstr:
        try:
            direction.append(direction_dict.setdefault(s, ''))
        except Exception as e:
            pass
    return ''.join(direction)


def parse_phrasedata(data):
    '''
    将风圈信息转换
    '''
    phrase = []
    phrase.append(Beaufort(data[0]))
    phrase.extend(data[1:5])
    return phrase


def data_parser(originData):
    '''
    将获取到的字符串转化为json形式
    '''
    if not originData:
        return
    starter = originData.index('{')
    json_data = originData[starter:-1]
    parsed_data = loads(json_data)
    return parsed_data


def Beaufort(kts):
    '''
    将kts的速度转换为风速等级
    '''
    if 'KTS' in kts:
        wind = kts[0:-3]
        windnum = int(wind)
        return initClass()[windnum]
    else:
        return None


def initClass():
    '''
    将kts为单位的速度转换为风级
    '''
    wind_class = []
    wind_class[0:17] = [0] * (17 - 0)
    wind_class[17:22] = [5] * (22 - 17)
    wind_class[22:28] = [6] * (28 - 22)
    wind_class[28:34] = [7] * (34 - 28)
    wind_class[34:41] = [8] * (41 - 34)
    wind_class[41:48] = [9] * (48 - 41)
    wind_class[48:56] = [10] * (56 - 48)
    wind_class[56:64] = [11] * (64 - 56)
    wind_class[64:100] = [12] * (100 - 64)
    return wind_class


if __name__ == '__main__':
    year_info = col.find({}, {'typhoonid': 1, '_id': 0})
    for typhoonid in year_info:
        # ids.append(typhoonid['typhoonid'])
        get_typhoon_info(typhoonid['typhoonid'])
