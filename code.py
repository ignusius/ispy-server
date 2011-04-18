#-*-coding:utf-8-*-
import web
import glob
import os
from web import form

render = web.template.render('templates/', globals={'glob':glob})
form = form.Form(form.Textbox("Дата"),form.Textbox("IP-адрес"),form.Textbox("Пользователь"),form.Button("Поехали!"))
                                                              
urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())

class index:
    def GET(self, name):
        return render.index(name,form)
         
if __name__ == "__main__":
    app.run()

    
