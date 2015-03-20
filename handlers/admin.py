#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tornado import web
from control.admin import *
from config import sitename


class Admin:
    # use password hash instead
    password1 = "123456789"
    password2 = "987654321"
    email = "moument@gmail.com"
    auth_info = {}


class BaseHandler(web.RequestHandler):
    def prepare(self):
        token = self.get_secure_cookie(sitename)
        if token in Admin.auth_info:
            self.user = Admin.auth_info[token]['user']
            return
        self.redirect('/login')


class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/login.html')

    def post(self, *args, **kwargs):
        password1 = self.get_argument('password1', None)
        password2 = self.get_argument('password2', None)
        if password1 != Admin.password1 or password2 != Admin.password2:
            return self.redirect('admin/login.html')
        self.set_secure_cookie(sitename)
        token = self.get_secure_cookie(sitename)
        Admin.auth_info[token] = {'user': 'admin'}
        return self.render('admin/manage.html')


class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        token = self.get_secure_cookie(sitename)
        del Admin.auth_info[token]
        return self.redirect('/')


class ManageHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('amdmin/manage.html')


class ManageArticlesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/manageArticles.html')


class DeleteArticleHandler(BaseHandler):
    def post(self, *args, **kwargs):
        pass


class NewArticleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/newArticle.html')

    def post(self, *args, **kwargs):
        pass


class EditArticleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/editArticle.html')

    def post(self, *args, **kwargs):
        pass


class DeleteCommentHandler(BaseHandler):
    def post(self, *args, **kwargs):
        pass


class ManageTimeLine(BaseHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/manageTimeLine.html')


class DeleteTimeLine(BaseHandler):
    def post(self, *args, **kwargs):
        pass


handlers=[
    (r'/amdin/login', LoginHandler),
    (r'/admin/logout', LogoutHandler),
    (r'/admin/manage', ManageHandler),
    (r'/admin/articles', ManageArticlesHandler),
    (r'/admin/article/new', NewArticleHandler),
    (r'/admin/article/delete', DeleteArticleHandler),
    (r'/admin/comment/delete', DeleteCommentHandler),
    (r'/admin/timeline', ManageTimeLine),
    (r'/amdin/timeline/delete', ManageTimeLine)
]