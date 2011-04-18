#-*-coding:utf-8-*-
import web
import glob
import os
from time import strftime 
from web import form

render = web.template.render('templates/', globals={'glob':glob})
form = form.Form(form.Textbox("date",description="Дата",type="text",value=strftime("%Y-%m-%d")),form.Textbox("IP",description="IP-адрес",value="*"),form.Textbox("username",description="Пользователь",value="*"),form.Textbox("list",description="Кол-во",value="50"),form.Button("Поиск"))

                                                              
urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())

class index:
    def GET(self, name):
        return render.index(name,form)
         
   
	
if __name__ == "__main__":
    app.run()

    
