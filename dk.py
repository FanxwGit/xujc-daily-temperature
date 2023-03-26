# -*- coding:utf-8 -*-
import requests as _
import json
import time
headers = {
    'Content-Type': 'application/json',
}
data = {
    "formData": [
        {
            "name": "select_1631714040062",
            "title": "完成情况",
            "value": {
                "stringValue": "已打卡"
            },
            "hide": False,
            "readonly": False
        },
        {
            "name": "select_1631790340241",
            "title": "今日体温",
            "value": {
                "stringValue": "37.3以下"
            },
            "hide": False,
            "readonly": False
        },
        {
            "name": "select_1641522783266",
            "title": "今日是否有中高风险【所在城市】旅居史",
            "value": {
                "stringValue": "否"
            },
            "hide": False,
            "readonly": False
        },
        {
            "name": "label_1641522839410",
            "title": "中高风险地区查询",
            "value": {},
            "hide": False,
            "readonly": True
        },
        {
            "name": "select_1641522890815",
            "title": "今日是否有中高风险地区旅居史",
            "value": {
                "stringValue": None
            },
            "hide": True,
            "readonly": False
        },
        {
            "name": "input_1641522901563",
            "title": "中高风险地区旅居史详细地址",
            "value": {
                "stringValue": None
            },
            "hide": True,
            "readonly": False
        },
        {
            "name": "select_1641523063583",
            "title": "今日个人疫情管控情况",
            "value": {
                "stringValue": "无"
            },
            "hide": False,
            "readonly": False
        },
        {
            "name": "select_1641523103608",
            "title": "今日是否有境外旅居史",
            "value": {
                "stringValue": "无"
            },
            "hide": False,
            "readonly": False
        },
        {
            "name": "select_1588863625331",
            "title": "今日本人及共同居住人员是否与中高风险地区或境外回国人员接触？",
            "value": {
                "stringValue": "否"
            },
            "hide": False,
            "readonly": False
        },
        {
            "name": "select_1582538846920",
            "title": "今日是否出现发热、咳嗽、胸闷、呼吸困难等症状？",
            "value": {
                "stringValue": "否"
            },
            "hide": False,
            "readonly": False
        },
        {
            "name": "select_1582538939790",
            "title": "本人是否承诺以上所填报的全部内容均属实、准确，不存在任何隐瞒和不实的情况，更无遗漏之处。",
            "value": {
                "stringValue": "是"
            },
            "hide": False,
            "readonly": False
        },
        {
            "name": "select_1653460359484",
            "title": "上课方式",
            "value": {
                "stringValue": "线下"
            },
            "hide": False,
            "readonly": False
        }
    ],
    "playerId": "owner"
}
cookies = [
    {
        'name': 'fxw',
        'SAAS_U': '18ff43401d362687ffcec266c6b38ce0b54c5a353ff5ef3875f961fa809d923b'
    },
    {
        'name': 'cyh',
        'SAAS_U': '92798af3444a55f203ce743a56cbcc0249ef5b9753d1fbfc66258227a970af5f'
    },
    {
        'name': 'xd',
        'SAAS_U': '6661594b68a28f8bbd0b7dd0c1f79fa6b269bc81eb25233962c7fac8573a7c5f'
    },
    {
        'name': 'xzc',
        'SAAS_U': 'ab95f24934f8ec8db49aacf849d5ad7b6c2a370aebdcd731c425b009edd80ec5'
    },
    {
        'name': 'zzx',
        'SAAS_U': '687031294e636cf1cc457844026cab453932df3589b2605c6b4f181d482a37ec'
    },
    {
        'name': 'zcm',
        'SAAS_U': 'c147200293fe606906f8f32c8aa89f002a306df487fa8fe313d24bf19f122223'
    },
]
data_js = json.dumps(data, ensure_ascii=False).encode('utf-8')
while True:
    for item in cookies:
        try:
            getIdJson = _.get('http://ijg.xujc.com/api/app/229/business/now?getFirst=true',
                              cookies={'SAAS_U': item["SAAS_U"]}, headers=headers).text
            id = json.loads(getIdJson)['data'][0]['business']['id']
            getKeyJson = _.get(
                "http://ijg.xujc.com/api/formEngine/business/%s/myFormInstance" % (id), cookies={'SAAS_U': item["SAAS_U"]}).text
            key = json.loads(getKeyJson)['data']['id']
            url = 'http://ijg.xujc.com/api/formEngine/formInstance/' + key
            res = _.post(url, headers=headers, cookies={
                'SAAS_U': item['SAAS_U']}, data=data_js)
            print(res.text, res)
        except Exception as e:
            print(item['name'], "error")
    time.sleep(4*60*60)  # 休息4个小时

# url 1660
