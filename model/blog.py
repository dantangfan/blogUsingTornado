#!/usr/bin/env python
# -*- coding:utf-8 -*-


import datetime
from db.dbmanager import db
from config import page_count


def correct_page(page):
    try:
        page = int(page)
        if page < 1:
            return 0
        else:
            return page - 1
        return page
    except Exception, e:
        print e
        return 0


def get_article_list(page):
    try:
        sql = "select id, title, publish_time, summary from article order by id desc limit %s, %s"
        cur_page = page+1
        all_page = db.get('select count(*) from article')/page_count
        articles = db.query(sql, page, page_count)
    except Exception, e:
        print e
        return {'err': -1, 'err_msg': '系统错误'}
    return {'err': 0,
            'cur_page': cur_page,
            'all_page': all_page,
            'articles': articles,
            }


def get_article(article_id):
    try:
        article_id = int(article_id)
        if article_id < 1:
            return None
        sql = "select id, title, publish_time, content from article where article_id = %s"
        article = db.get(sql, article_id)
        return article
    except Exception, e:
        print e
        return None


def add_comment(article_id=None, user_name=None, user_email=None, website=None, comment=None, to_cid=None):
    sql = 'insert into comment(article_id, user_name, user_email, website, create_at, content, to_comment_id)' \
          'values(%s, %s, %s, %s, %s, %s, %s)'
    create_at = datetime.datetime.now()
    try:
        article_id = int(article_id)
        if article_id < 1:
            return {'err': -1, 'err_msg': '不存在的文章'}
        if to_cid:
            to_cid = int(to_cid)
            if to_cid < 1:
                return {'err': -1, 'err_msg': '不存在的评论'}
        tempsql = 'select count(*) from article'
        count = db.get(tempsql)
        if article_id > count:
            return {'err': -1, 'err_msg': '不存在的文章'}
        tempsql = "select 1 from comment where article_id = %s and id = %s"
        count = db.get(tempsql, article_id, to_cid)
        if not count:
            return {'err': -1, 'err_msg': '不存在的评论'}
        db.execute(sql, (article_id, user_name, user_email, website, create_at, comment, to_cid))
    except Exception, e:
        print e
        return {'err': -1, 'err_msg': '系统错误，请稍后再试'}
    return {'err': 0}
