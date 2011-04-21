#-*-coding:utf-8-*-
from bottle import route, run, debug, template, request, static_file, error,redirect
import time


@route('/')
def index():
    redirect("/search?task1="+time.strftime("%Y-%m-%d")+"&task2=*&task3=*&save=Поиск")

@route('/search', method='GET')
def search():
    
    output = template('mytemplate',button="search",date=request.GET.get('task1'),IP=request.GET.get('task2'),username=request.GET.get('task3'))
    if request.GET.get('save','').strip():
        return output
        
    
@route('/static/:filename')
def server_static(filename):
    return static_file(filename, root='static/')

@route('/static/images/:filename')
def server_static(filename):
    return static_file(filename, root='static/images/')

 
 
@error(404)
def Error404(code):
    return "<h1>Страница 404</h1>" 


debug(True)
run(host='192.168.1.128', port=8080,reloader=True)
