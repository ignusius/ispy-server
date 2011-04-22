#-*-coding:utf-8-*-
from bottle import route, run, debug, template, request, static_file, error,redirect,PasteServer

import time

@route('/')
def index():
    redirect("/search?task1="+time.strftime("%Y-%m-%d")+"&task2=*&task3=*&save=Поиск")

@route('/search', method='GET')
def search():
    
    output = template('template/index',button="search",date=request.GET.get('task1')\
,IP=request.GET.get('task2'),username=request.GET.get('task3'))
    if request.GET.get('save','').strip():
        return output

@route('/admin', method='GET')
def admin():
    output = template('template/admin',button="search")
    return output

@route('/admin', method='POST')
def admin():
    output = template('template/admin',button="search")
    return "rrrr"

@route('/static/:filename')
def server_static(filename):
    return static_file(filename, root='static/')

@route('/static/images/:filename')
def server_static(filename):
    return static_file(filename, root='static/images/')

 
@error(404)
def Error404(code):
    return "<h1>Страница 404 :(</h1>" 

debug(True)
run(server=PasteServer(host='192.168.1.128'), reloader=True)

