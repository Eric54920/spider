import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
fp = open('spider/test/yjzj.csv', 'w', encoding='utf-8')
head = "businessLicenseNumber,businessPerson,certStr,epsAddress,epsName,epsProductAddress,isimport,legalPerson,productSn,qfManagerName,qualityPerson,rcManagerDepartName,rcManagerUser,xkCompleteDate,xkDate,xkDateStr,xkName,xkType"
fp.write(head+'\n')

url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
for page in range(2):
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
    }
    res = requests.post(url=url, headers=headers, data=data).json()
    for i in res['list']:
        enter_id = i['ID']
        print(enter_id)
        detail_url = f'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById&id={enter_id}'
        detail_res = requests.get(url=detail_url, headers=headers).json()

        businessLicenseNumber = detail_res['businessLicenseNumber']
        businessPerson = detail_res['businessPerson']
        certStr = detail_res['certStr']
        epsAddress = detail_res['epsAddress']
        epsName = detail_res['epsName']
        epsProductAddress = detail_res['epsProductAddress']
        isimport = detail_res['isimport']
        legalPerson = detail_res['legalPerson']
        productSn = detail_res['productSn']
        qfManagerName = detail_res['qfManagerName']
        qualityPerson = detail_res['qualityPerson']
        rcManagerDepartName = detail_res['rcManagerDepartName']
        rcManagerUser = detail_res['rcManagerUser']
        xkCompleteDate = detail_res['xkCompleteDate']
        xkDate = detail_res['xkDate']
        xkDateStr = detail_res['xkDateStr']
        xkName = detail_res['xkName']
        xkType = detail_res['xkType']

        line = f"{businessLicenseNumber},{businessPerson},{certStr},{epsAddress},{epsName},{epsProductAddress},{isimport},{legalPerson},{productSn},{qfManagerName},{qualityPerson},{rcManagerDepartName},{rcManagerUser},{xkCompleteDate},{xkDate},{xkDateStr},{xkName},{xkType}"
        fp.write(line+'\n')


