#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tornado import web
from model.blog import *


class BaseHandler(web.RequestHandler):
    pass


class IndexHandler(BaseHandler):
    def get(self):
        return self.render('index.html')


class ListArticleHandler(BaseHandler):
    def get(self, page=1):
        page = correct_page(page)
        rst = get_article_list(page)
        if rst['err'] != 0:
            return self.render('404.html')
        return self.render('listArticle.html',
                           articles=rst['articles'],
                           cur_page=rst['cur_page'],
                           all_page=rst['all_page'])


class ShowArticleHandler(BaseHandler):
    def get(self, article_id):
        article = get_article(article_id)
        if not article:
            return self.redirect('/')
        return self.render('article.html', article=article)


class CommentHandler(BaseHandler):
    def post(self):
        article_id = self.get_argument('article_id', None)
        user_name = self.get_argument('user_name', None)
        user_email = self.get_argument('user_email', None)
        web_site = self.get_argument('website', None)
        article_id = self.get_argument('article_id', None)
        comment = self.get_argument('comment', None)
        to_cid = self.get_argument('to_cid', None)
        if user_name is None or user_email is None or comment is None:
            return self.write({'err': -1, 'err_msg': '您需要填写昵称、邮箱和评论'})
        rst =  add_comment(article_id, user_email, web_site, article_id, comment, to_cid)
        return rst


class ShowProjectHandler(BaseHandler):
    def get(self):
        return self.render('project.html')


class ShowAboutMeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('aboutMe.html')


class TimeLineHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('timeLine.html')

    def post(self, *args, **kwargs):
        pass

handlers = [
    (r'/', IndexHandler),
    (r'/articles', ListArticleHandler),
    (r'/article/(\d+)/', ShowArticleHandler),
    (r'/comment', CommentHandler),
    (r'/project', ShowProjectHandler),
    (r'/aboutme', ShowAboutMeHandler),
    (r'/timeline', TimeLineHandler)
]