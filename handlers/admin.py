#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tornado import web
from model.admin import *
from config import sitename


class Admin:
    # use password hash instead
    password1 = "123"
    password2 = "321"
    email = "moument@gmail.com"
    auth_info = {}


class BaseHandler(web.RequestHandler):
    def prepare(self):
        try:
            token = self.get_secure_cookie(sitename)
            if token in Admin.auth_info:
                self.user = Admin.auth_info[token]['user']
                return
            self.redirect('/admin/login')
        except Exception, e:
            print e
            self.redirect('/admin/login')


class LoginHandler(web.RequestHandler):
    def get(self):
        return self.render('admin/login.html')

    def post(self, *args, **kwargs):
        password1 = self.get_argument('password1', None)
        password2 = self.get_argument('password2', None)
        print password1,password2
        if password1 != Admin.password1 or password2 != Admin.password2:
            return self.redirect('/admin/login')
        self.set_secure_cookie(sitename, password1)
        token = self.get_secure_cookie(sitename)
        Admin.auth_info[token] = {'user': 'admin'}
        return self.redirect('/admin/manage')


class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        token = self.get_secure_cookie(sitename)
        del Admin.auth_info[token]
        return self.redirect('/')


class ManageHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/manage.html')


class ManageArticlesHandler(BaseHandler):
    def get(self, page=1):
        rst = manage_article(page)
        if rst['err']:
            #return self.render('404.html')
            return self.write('<h1>404<h1>')
        return self.render('admin/manageArticle.html', articles=rst['articles'])


class DeleteArticleHandler(BaseHandler):
    def post(self, *args, **kwargs):
        article_id = self.get_argument('article_id', None)
        return delete_article(article_id)


class NewArticleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/newArticle.html')

    def post(self, *args, **kwargs):
        title = self.get_argument('title', None)
        summary = self.get_argument('summary', None)
        content = self.get_argument('content', None)
        return new_article(title, summary, content)


class EditArticleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/editArticle.html')

    def post(self, *args, **kwargs):
        pass


class DeleteCommentHandler(BaseHandler):
    def post(self, *args, **kwargs):
        cid = self.get_argument('cid', None)
        return delete_comment(cid)


class ManageTimeLine(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/manageTimeline.html')


class DeleteTimeLine(BaseHandler):
    def post(self, *args, **kwargs):
        pass


handlers=[
    (r'/admin/login', LoginHandler),
    (r'/admin/logout', LogoutHandler),
    (r'/admin/manage', ManageHandler),
    (r'/admin/articles', ManageArticlesHandler),
    (r'/admin/article/new', NewArticleHandler),
    (r'/admin/article/delete', DeleteArticleHandler),
    (r'/admin/comment/delete', DeleteCommentHandler),
    (r'/admin/timeline', ManageTimeLine),
    (r'/admin/timeline/delete', ManageTimeLine)
]