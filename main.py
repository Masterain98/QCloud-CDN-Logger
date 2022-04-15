import json
import gzip
import time

import requests
import os
from datetime import datetime, timezone, timedelta
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdn.v20180606 import cdn_client, models

from db_pool.mysqlhelper import MySqLHelper


# Load config file
with open("config.json", 'r') as config:
    config_dict = json.load(config)
SecretId = config_dict["SecretId"]
SecretKey = config_dict["SecretKey"]
Domain = config_dict["domain"]


def getLog(startTime, endTime, domain):
    try:
        cred = credential.Credential(SecretId, SecretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cdn.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cdn_client.CdnClient(cred, "", clientProfile)

        req = models.DescribeCdnDomainLogsRequest()
        params = {
            "Domain": domain,
            "StartTime": startTime,
            "EndTime": endTime,
            "Area": "mainland"
        }
        req.from_json_string(json.dumps(params))

        resp = client.DescribeCdnDomainLogs(req)
        print(resp.to_json_string())
        api_result = json.loads(resp.to_json_string())["DomainLogs"]

        # 遍历 API 返回结果
        for log in api_result:
            # 获取 gz 日志下载地址
            gz_log_download = requests.get(log["LogPath"])
            gz_log_name = "data/" + log["LogName"] + ".gz"
            # 下载 gz 日志包
            with open(gz_log_name, "wb") as file:
                file.write(gz_log_download.content)
            # 解压 gz 日志
            g_log = gzip.GzipFile(gz_log_name)
            open(gz_log_name.replace(".gz", ".log"), "wb+").write(g_log.read())
            g_log.close()
            # 删除 gz 包
            os.remove(gz_log_name)

            # 打开日志
            for line in open(gz_log_name.replace(".gz", ".log")):
                split1 = line.split('"')
                split2 = line.split(' ')

                Request_Time = split2[0]
                IP = split2[1]
                Domain = split2[2]
                Path = split2[3]
                Request_Size = split2[4]
                Province_ID = split2[5]
                ISP_ID = split2[6]
                HTTP_Response = split2[7]
                Referer = split2[8]
                Response_Time = split2[9]
                UA = split1[1]
                Range_Parameter = split1[3]
                HTTP_Method = split2[-4]
                HTTP_Protocols = split2[-3]
                Cache_Status = split2[-2]
                CDN_Port = split2[-1]

                SQL_statement = r"INSERT INTO log(Request_Time, IP, Domain, Path, Request_Size, Province_ID, ISP_ID," \
                                r"HTTP_Response, Referer, Response_Time, User_Agent, Range_Parameter, HTTP_Method," \
                                r"HTTP_Protocols, Cache_Status, CDN_Port) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s," \
                                r"%s, %s, %s, %s, %s, %s, %s)"
                data = db.insertone(SQL_statement,
                                    param=(Request_Time, IP, Domain, Path, Request_Size, Province_ID, ISP_ID, \
                                           HTTP_Response, Referer, Response_Time, UA, Range_Parameter, HTTP_Method, \
                                           HTTP_Protocols, Cache_Status, CDN_Port))
                if str(data) == "1":
                    print("写入数据成功")
                else:
                    print("写入数据失败 " + str(datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))))


    except TencentCloudSDKException as err:
        print(err)


if __name__ == "__main__":
    db = MySqLHelper()

    while True:
        currentTimestamp = int(time.time()) + 3600

        currentDateTime = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
        print(currentDateTime)
        start_time = currentDateTime.replace(minute=0, second=0, microsecond=0) + timedelta(hours=-3)
        end_time = currentDateTime.replace(minute=59, second=59, microsecond=0) + timedelta(hours=-3)
        start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
        end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
        # getLog("2022-03-17 00:00:00", "2022-04-16 17:59:59", Domain)
        getLog(start_time, end_time, Domain)

        print("休眠 " + str(currentTimestamp - int(time.time())) + " 秒")
        time.sleep(currentTimestamp - int(time.time()))


