%import glob

%if date==None:
    %date='*'
    %end
%if IP==None:
    %IP='*'
    %end
%if username==None:
    %username='*'
    %end

<p style="background-color:#ff9900" align="left">
<img src="static/logo.png">
<form action="/search" method="GET">
Дата:<input type="text" size="10" maxlength="100" name="task1" value="{{date}}">
IP-адрес:<input type="text" size="10" maxlength="100" name="task2" value="{{IP}}">
Пользователь:<input type="text" size="10" maxlength="100" name="task3" value="{{username}}">
<input type="submit" name="save" value="Поиск"></p>
</form>


%if button == 'search':
    %for i in glob.glob("static/images/"+date+"_*_"+IP+"_*"+username+".jpg"):
    <a href="{{i}}"><img class="size-medium wp-image-1078 aligncenter" src="{{i}}" width="300" height="225"/></a>
    %end   

%end


