#!/usr/bin/env python
# -*- coding:utf-8 -*-


from handlers import blog, admin, chat


handlers = []
ui_modules = []
sub_handlers = []

handlers.extend(blog.handlers)
handlers.extend(admin.handlers)