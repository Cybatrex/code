#!/usr/bin/env python
# coding: utf-8

import xmlrpclib
import xlrd

# url = 'http://localhost:8069'
# dbname = 'mgm_20_06'
# username = 'admin'
# pwd = 'a'

url = 'http://beta-dev1.hashmicro.com'
dbname = 'MGM'
username = 'admin'
pwd = 'Hash22733Micro#'

sock_common = xmlrpclib.ServerProxy (url + '/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = xmlrpclib.ServerProxy(url + '/xmlrpc/object')

# workbook = xlrd.open_workbook('ACCOUNTS.xlsx')
# worksheet = workbook.sheet_by_name('ACCOUNTS')

not_deleted_account = []
deleted_account = []
default_account = ['1-121001','2-110001', '2-122101', '2-122102', '1000000', '1100000', '1110000', '1111000', '1111100', '1111101', '1111102', '1111103', '1111104', '1111131', '1111132', '1111133', '1111134', '1111135', '1111136', '1111200', '1111201', '1111300', '1111301', '1111400', '1111401', '1112000', '1112100', '1112101', '1112102', '1112103', '1112104', '1112105', '1112106', '1112107', '1112108', '1112109', '1112110', '1112111', '1112200', '1112201', '1112202', '1112203', '1112204', '1112300', '1112301', '1112302', '1112303', '1112304', '1113000', '1113100', '1113101', '1114000', '1114100', '1114101', '1120000', '1121000', '1121100', '1121101', '1121102', '1121103', '1121104', '1121200', '1121201', '1121202', '1121203', '1121204', '1122000', '1122100', '1122101', '1122102', '1122103', '1122104', '1122200', '1122201', '1122202', '1122203', '1122204', '1123000', '1123100', '1123101', '1123102', '1122001', '1122105', '1122106', '1122107', '1122205', '1122206', '1122300', '1122301', '1122900', '1122901', '1130000', '1131000', '1131100', '1131101', '1131102', '1131103', '1131104', '1131105', '1131106', '1131107', '1131108', '1131109', '1131110', '1131111', '1131112', '1140000', '1141000', '1141100', '1141101', '1141102', '1141103', '1141104', '1142000', '1142100', '1142101', '1142102', '1142103', '1142104', '1142105', '1142106', '1142199', '1150000', '1151000', '1151100', '1151101', '1151102', '1151103', '1151104', '1152000', '1152100', '1152101', '1152102', '1152103', '1153000', '1153100', '1153101', '1153102', '1153103', '1153104', '1153105', '1153106', '1153107', '1153108', '1159000', '1159100', '1159101', '1200000', '1210000', '1211000', '1211100', '1211101', '1220000', '1221000', '1221100', '1221101', '1230000', '1231000', '1231100', '1230001', '1230002', '1300000', '1310000', '1311000', '1311100', '1311101', '1311102', '1311103', '1311104', '1311105', '1311106', '1311107', '1311108', '1311109', '1311110', '1311200', '1311201', '1311202', '1311203', '1311204', '1311205', '1311206', '1311207', '1311208', '1311209', '1311300', '1311301', '1311302', '1320000', '1321000', '1321100', '1321101', '1321200', '1321201', '2000000', '2100000', '2110000', '2111000', '2111100', '2111101', '2111102', '2111103', '2111104', '2112100', '2112101', '2112102', '2112103', '2112104', '2112000', '2112105', '2112106', '2112107', '2112108', '2112109', '2112200', '2112201', '2112202', '2112203', '2112204', '2113000', '2113100', '2113101', '2113102', '2113103', '2113104', '2113200', '2113201', '2130000', '2131000', '2131100', '2131101', '2131102', '2131103', '2131200', '2131201', '2140000', '2141000', '2141100', '2141101', '2141102', '2141200', '2141201', '2141202', '2142000', '2142100', '2142101', '2142200', '2142201', '2143000', '2143100', '2143101', '2143102', '2143103', '2143104', '2143105', '2143106', '2143107', '2143108', '2143109', '2144000', '2144100', '2144101', '2144102', '2144200', '2144201', '2144300', '2144301', '2144302', '2144303', '2200000', '2210000', '2211000', '2211100', '2211101', '2211200', '2211201', '2212000', '2212100', '2212101', '2212200', '2212201', '2212202', '2212203', '3000000', '3100000', '3110000', '3111000', '3111100', '3121101', '3121102', '3121103', '3121104', '3121105', '3120000', '3121000', '3121100', '3121106', '3121107', '3121199', '4000000', '4100000', '4110000', '4111000', '4111100', '4111101', '4111102', '4111103', '4111104', '4111105', '4120000', '4121000', '4121100', '4121101', '4121102', '4121103', '4121104', '4121105', '4130000', '4131000', '4131100', '4131101', '4140000', '4141000', '4141100', '4141101', '4180000', '4181000', '4181100', '4181101', '4190000', '4191000', '4191100', '4191101', '5000000', '5100000', '5110000', '5111000', '5111100', '5111101', '5111102', '5111103', '5111105', '5111106', '5111107', '5111108', '5111109', '5111110', '5111111', '5130000', '5131000', '5131100', '5131101', '5132000', '5132100', '5132101', '5133000', '5133100', '5133101', '5140000', '5141000', '5141100', '5141101', '5141102', '5141103', '5141104', '5141105', '5141106', '5141107', '5141108', '5141109', '5141110', '5141111', '5141112', '5141113', '5141114', '5141115', '5150000', '5151000', '5151100', '5151101', '5151102', '5151103', '5151104', '5151105', '5151106', '5151107', '5151108', '5151109', '5151110', '5151111', '5151112', '5151113', '5151114', '5151115', '5151116', '5151117', '5151118', '5160000', '5161000', '5161100', '5111501', '5111502', '5111503', '5111504', '5170000', '5171000', '5171100', '5171101', '5171102', '5171103', '5111700', '5111701', '5111702', '5111703', '5111704', '5111705', '5111706', '5111900', '5111901', '5111902', '5111903', '5111904', '6000000', '6100000', '6110000', '6111000', '6111100', '6111101', '6111102', '6111103', '6111104', '6111105', '6111106', '6111107', '6111108', '6111109', '6111110', '6111111', '6111112', '6111113', '6111114', '6111115', '6111116', '6111117', '6111118', '6112000', '6112100', '6112101', '6112102', '6112103', '6112104', '6112105', '6112106', '6120000', '6121000', '6121100', '6121101', '6121102', '6121103', '6121104', '6121105', '6121200', '6121201', '6121202', '6121203', '6121204', '6130000', '6131000', '6131100', '6113101', '6113102', '6113103', '6113104', '6131200', '6131201', '6131202', '6131203', '6131204', '6131205', '6131206', '6131207', '6131208', '6140000', '6141000', '6141100', '6114101', '6114102', '6114103', '6141200', '6141201', '6141202', '6141203', '6150000', '6151000', '6151100', '6151101', '6151102', '6151103', '6151104', '6151105', '6160000', '6161000', '6161100', '6161101', '6161102', '6161103', '6161200', '6161201', '6170000', '6171000', '6171100', '6171101', '6171102', '6171103', '6171104', '6171105', '6180000', '6181000', '6181100', '6181101', '6181102', '6181103', '6181104', '6181105', '6181106', '6181107', '6181108', '6190000', '6191000', '6191100', '6191101', '6191102', '6191103', '6191104', '6191105', '6191106', '8000000', '8100000', '8110000', '8111000', '8111100', '8111101', '8111102', '8111103', '8111200', '8111201', '8111202', '8112000', '8112100', '8112101', '8112102', '8112103', '8112104', '8112199', '8112200', '8112201', '8200000', '8210000', '8211000', '8211100', '8211101', '8211102', '8211103', '8211200', '8211201', '8211202', '8211203', '8211001', '8211104', '8211199', '999999', '300200', '300100', '220000', '212300', '212200', '212100', '211000', '210000', '201000', '200000', '112000', '111300', '111200', '111100', '111000', '103000', '102000', '101700', '101600', '101501', '101401', '101300', '101200', '101130', '101120', '101110', '101000', '100000']


acc_ids = sock.execute(dbname, uid, pwd, 'account.account', 'search', [('code', 'not in', default_account)])

for acc_id in acc_ids:
    try:
        print ">>>>>>>>>>>>> try delete acc_id",acc_id
        account_unlink = sock.execute(dbname, uid, pwd, 'account.account', 'unlink', acc_id)
        deleted_account.append(acc_id)
    except:
        print ">>>>>>>>>>>>> except acc_id", acc_id
        not_deleted_account.append(acc_id)

print ">>>>>>>>>> deleted_acc", deleted_account
print ">>>>>>>>>> not deleted_acc", not_deleted_account

