-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2022 at 09:51 AM
-- Server version: 10.6.8-MariaDB-log
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `QCloudCDNLogger`
--

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `ID` int(11) NOT NULL,
  `Request_Time` datetime DEFAULT NULL COMMENT '请求时间',
  `IP` varchar(255) DEFAULT NULL COMMENT '客户端 IP',
  `Domain` varchar(255) DEFAULT NULL COMMENT '域名',
  `Path` varchar(255) DEFAULT NULL COMMENT '请求路径',
  `Request_Size` int(11) DEFAULT NULL COMMENT '本次访问字节数大小（包含文件本身大小及请求 header 头部大小）',
  `Province_ID` int(11) DEFAULT NULL COMMENT '境内日志代表省份编号，境外日志代表地区编号（映射表见下文）',
  `ISP_ID` int(11) DEFAULT NULL COMMENT '境内日志代表运营商编号，境外日志统一为 -1（映射表见下文）',
  `HTTP_Response` varchar(255) DEFAULT NULL COMMENT 'HTTP 状态码',
  `Referer` varchar(255) DEFAULT NULL COMMENT 'Referer 信息',
  `Response_Time` int(11) DEFAULT NULL COMMENT '响应时间（毫秒），指节点从收到请求后响应所有回包再到客户端所花费的时间',
  `User_Agent` varchar(255) DEFAULT NULL COMMENT 'User-Agent 信息',
  `Range_Parameter` varchar(255) DEFAULT NULL COMMENT 'Range 参数',
  `HTTP_Method` varchar(255) DEFAULT NULL COMMENT 'HTTP Method',
  `HTTP_Protocols` varchar(255) DEFAULT NULL COMMENT 'HTTP 协议标识',
  `Cache_Status` varchar(255) DEFAULT NULL COMMENT '缓存 HIT/MISS，在 CDN 边缘节点命中、父节点命中均标记为 HIT',
  `CDN_Port` varchar(255) DEFAULT NULL COMMENT '客户端与 CDN 节点建立连接的端口，若无则为 -'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `log`
--

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
