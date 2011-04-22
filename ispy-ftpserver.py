from pyftpdlib import ftpserver
authorizer = ftpserver.DummyAuthorizer()
authorizer.add_user("user", "12345", "/home/komar/Image", perm="elrafmw")
handler = ftpserver.FTPHandler
handler.authorizer = authorizer
address = ("192.168.1.128", 2222)
ftpd = ftpserver.FTPServer(address, handler)
ftpd.serve_forever()

