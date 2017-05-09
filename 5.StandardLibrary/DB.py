#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='2238447',db='formater',port=3306)
    cur=conn.cursor()

    # cur.execute('select * from album_xiami where album_id = 1')
    # data = cur.fetchall()

    # if not len(data):
    #     print 'No data'

    # for album in data:
    #     print album
        
    # sql = "INSERT INTO `album_xiami` (`album_id`, `album_name`, `cover`, `cover_color`, `cover_width`, `cover_height`, `artist_id`, `artist_name`, `artist_name2`) VALUES (%s, '2', '3', '4', '5', '6', '7', '8', '9');"

    # sql = "INSERT INTO `album_xiami` (`album_id`, `album_name`, `cover`, `cover_color`, `cover_width`, `cover_height`, `artist_id`, `artist_name`, `artist_name2`) VALUES (%d,%s,%s,%s,%s,%s,%s,%s,%s)"

    # value = [56, '1', '1', '1', '1', '1', '1', '1', '1']

    # print sql
    # print value

    # data = cur.execute(sql, value)
    # print data

    # sql = "INSERT INTO `formater`.`my` (`id`, `name`) VALUES (%s, %s);"
    # cur.execute(sql, ('6','1'));

    # sql = "INSERT INTO `formater`.`album_xiami` (`album_id`, `album_name`, `cover`, `cover_color`, `cover_width`, `cover_height`, `artist_id`, `artist_name`, `artist_name2`) VALUES (%s, '1', '1', '1', '1', '1', '1', '1', '1');"    
    # cur.execute(sql, ('50'))

    # sql = "INSERT INTO `formater`.`album_xiami` (`album_id`, `album_name`, `cover`, `cover_color`, `cover_width`, `cover_height`, `artist_id`, `artist_name`, `artist_name2`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    # cur.execute(sql, ('54', '1', '1', '1', '1', '1', '1', '1', '1'))

    # conn.commit()

    cur.execute('SELECT * from `album_xiami` WHERE `album_id` = %s', ('100',))
    data = cur.fetchall()
    print data
    
    cur.close()
    conn.close()

except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
