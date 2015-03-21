#!/usr/bin/env python
# -*- coding:utf-8 -*-

from db.dbmanager import db
import datetime
from config import page_count


def delete_article(article_id):
    try:
        article_id = int(article_id)
        sql = "delete from article where id = %s"
        cursor = db._cursor()
        cursor.execute("BEGIN")
        cursor.execute(sql, (article_id))
        sql = "delete from comment where article_id = %s"
        cursor.execute(sql, (article_id))
        cursor.execute("COMMIT")
    except Exception, e:
        print e
        return {'err': -1, 'err_msg': 'server error'}
    return {'err': 0}


def new_article(title, summary, content):
    if title is None or summary is None or content is None:
        return {'err': -1, 'err_msg': '标题、概要、内容都不能为空'}
    try:
        time = datetime.datetime.now()
        sql = "insert into article(title, publish_time, summary, content) values(%s, %s, %s, %s)"
        db.execute(sql, (title, time, summary, content))
        return {'err': 0}
    except Exception, e:
        print e
        return {'err': -1, 'err_msg': 'sever error'}


def delete_comment(cid):
    try:
        cid = int(cid)
        sql = "delete from comment where id = %s"
        db.execute(sql, (cid))
        return {'err': 0}
    except Exception, e:
        print e
        return {'err': -1, 'err_msg': 'server error'}