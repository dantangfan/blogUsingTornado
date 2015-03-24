#!/usr/bin/env python
# -*- coding:utf-8 -*-


import datetime
from db.dbmanager import db
from config import page_count
from utils.clean_xss import parsehtml


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
        all_page = db.get('select count(*) as count from article')
        all_page = all_page['count']/(page+1)
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
        sql = "select id, title, html, publish_time, content from article where id = %s"
        article = db.get(sql, article_id)
        return article
    except Exception, e:
        print e
        return None

def get_comment(article_id):
    sql = "select id, user_name, create_at, content, to_comment_id as cid, to_comment_username as cname" \
          " from comment where article_id = %s"
    comments = db.query(sql, article_id)
    return comments


def add_comment(article_id=None, user_name=None, user_email=None, website=None, comment=None, to_cid=None, to_cname=None):
    sql = 'insert into comment(article_id, user_name, user_email, website, create_at, content, to_comment_id, to_comment_username)' \
          'values(%s, %s, %s, %s, %s, %s, %s, %s)'
    create_at = datetime.datetime.now()
    try:
        article_id = int(article_id)
        if article_id < 1:
            return {'err': -1, 'err_msg': '不存在的文章'}
        if to_cid:
            print to_cid
            to_cid = int(to_cid)
            if to_cid < 1:
                return {'err': -1, 'err_msg': '不存在的评论'}
        if to_cid=='':
            to_cid = None
        user_name = parsehtml(user_name)
        comment = parsehtml(comment)
        db.execute(sql, article_id, user_name, user_email, website, create_at, comment, to_cid, to_cname)
    except Exception, e:
        print e
        return {'err': -1, 'err_msg': '系统错误，请稍后再试'}
    return {'err': 0}
