import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="fuzzy_db"
)

mycursor = mydb.cursor()

# Table structure for table 'tb_emp'

mycursor.execute("DROP TABLE IF EXISTS `tb_emp`")

mycursor.execute("CREATE TABLE `tb_emp` (\
                  `id` int(10) NOT NULL auto_increment,\
                  `nama` varchar(50) default NULL,\
                  `usia` tinyint(2) default NULL,\
                  `masakerja` tinyint(2) default NULL,\
                  `gaji` int(10) default NULL,\
                  PRIMARY KEY (`id`)) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;")

mycursor.execute("INSERT INTO `tb_emp`(`id`,`nama`,`usia`,`masakerja`,`gaji`) \
                  VALUES (1,'Anik',30,6,750000),\
                  (2,'Yudi',48,17,1255000),\
                  (3,'Inawati',36,14,1500000),\
                  (4,'Rudi',37,4,1040000),\
                  (5,'Riska',42,12,950000),\
                  (6,'Aman',39,13,1600000),\
                  (7,'Dudi',37,5,1250000),\
                  (8,'Rini',32,1,550000),\
                  (9,'Ratih',35,3,735000),\
                  (10,'Panjul',25,2,860000)")

# Table structure for table 'tb_kelompok'

mycursor.execute("DROP TABLE IF EXISTS `tb_kelompok`")

mycursor.execute("CREATE TABLE `tb_kelompok` (\
                  `id` int(10) NOT NULL auto_increment,\
                  `nama_kelompok` varchar(25) default NULL,\
                  `field_akses` varchar(25) default NULL,\
                  PRIMARY KEY (`id`)) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;")

mycursor.execute("INSERT INTO `tb_kelompok`(`id`,`nama_kelompok`,`field_akses`) \
                  VALUES (1,'Umur','usia'),\
                  (2,'Masa Kerja','masakerja'),\
                  (3,'Gaji', 'gaji')")

# Table structure for table 'tb_kriteria'

mycursor.execute("DROP TABLE IF EXISTS `tb_kriteria`")

mycursor.execute("CREATE TABLE `tb_kriteria` (\
                  `id` int(10) NOT NULL auto_increment,\
                  `nama_kriteria` varchar(30) default NULL,\
                  `bawah` float(10,2) default NULL,\
                  `tengah` float(10,2) default NULL,\
                  `atas` float(10,2) default NULL,\
                  `kelompok` tinyint(2) default NULL,\
                  `keterangan` varchar(100) default NULL,\
                  PRIMARY KEY (`id`)) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;")

mycursor.execute("INSERT INTO `tb_kriteria`(`id`,`nama_kriteria`,`bawah`,`tengah`,`atas`,`kelompok`,`keterangan`) \
                  VALUES (1,'Muda',0.00,30.00,40.00,1,'Darah Muda'),\
                  (2,'Parobaya',35.00,45.00,50.00,1,NULL),\
                  (3,'Tua',40.00,50.00,99.00,1,NULL),\
                  (4,'Baru',0.00,5.00,15.00,2,NULL),\
                  (5,'Lama',10.00,25.00,99.00,2,NULL),\
                  (6,'Rendah',0.00,300000.00, 800000.00,3,NULL),\
                  (7,'Sedang',500000.00,1000000.00,1500000.00,3,NULL),\
                  (8,'Tinggi',1000000.00,2000000.00,100000000.00,3,NULL)")

mydb.commit()