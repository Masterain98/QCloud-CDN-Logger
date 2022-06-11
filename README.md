# QCloud-CDN-Logger
Python program to migrate Tencent Cloud CDN log to local MySQL database

将腾讯云 CDN 日志自动迁移到本地 MySQL 服务器的 Python 程序

## 使用方法

### 填写配置文件

- 打开 `config.json` 文件，将你的腾讯云配置文件填入
  - `SecretId` 和 `SecretKey` 为你的腾讯云用户的密钥
  - `domain` 为一个包含帐号下 CDN 域名的列表
  - `db_config` 为数据配置信息
    - `dbAddress` 为数据库主机地址
    - `dbPort` 为 MySQL 端口
    - `dbName` 为数据库名
    - `dbUser` 为数据库用户名
    - `dbPassword` 为数据库用户密码

示例配置：

```json
{
  "SecretId": "BNJDFhgonishgnionio3875nvolBOGSM",
  "SecretKey": "h8FGOoOHGOEOCVBFhgon81bgo1vozK",
  "domain": ["www.google.com", "www.baidu.com", "www.bing.com"],
  "db_config": {
    "dbAddress":"172.17.0.1",
    "dbPort": 3306,
    "dbName": "qcloud-log",
    "dbUser": "qcloud-log",
    "dbPassword": "qcloud_log"
  }
}
```

### 运行程序

- 在目标数据库中导入 `qcloud-log.sql` 文件
- 测试时直接运行 `main.py` 即可
- 主程序已经 Docker 化，你可以直接使用 Repo 中的 `Dockerfile`
  - Linux 下可以执行 ` sh build-docker.sh` 完成 Docker 容器部署

## 数据库结构

![](https://github.com/Masterain98/QCloud-CDN-Logger/blob/main/db-structure-screenshot.png?raw=true)

