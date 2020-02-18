CREATE TABLE `github_ncov_url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` smallint(5) unsigned DEFAULT NULL,
  `sources` varchar(20) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;


insert into github_ncov_url
(date,sources,title,url)
value(2020,'github_Academic-nCoV','Academic-nCoV，为你追踪 2019-nCoV 最新海外信息','https://github.com/Academic-nCoV/2019-nCoV/wiki');


CREATE TABLE `Academic-nCoV_2019-nCoV_wiki` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
