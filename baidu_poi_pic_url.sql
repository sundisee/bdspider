/*
 Navicat Premium Data Transfer

 Source Server         : mafengwo
 Source Server Type    : MySQL
 Source Server Version : 50163
 Source Host           : localhost
 Source Database       : mafengwo

 Target Server Type    : MySQL
 Target Server Version : 50163
 File Encoding         : utf-8

 Date: 12/26/2013 20:16:55 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `baidu_poi_pic_url`
-- ----------------------------
DROP TABLE IF EXISTS `baidu_poi_pic_url`;
CREATE TABLE `baidu_poi_pic_url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `baidu_poi_id` int(11) NOT NULL,
  `poi_pic_url` text,
  PRIMARY KEY (`id`),
  KEY `baidu_poi_id` (`baidu_poi_id`)
) ENGINE=MyISAM AUTO_INCREMENT=108 DEFAULT CHARSET=utf8;

