# import urllib2
from flask import Flask

# response = urllib2.urlopen("http://www.baidu.com")
#
# #获取请求状态码
# print response.getcode()
#
# content = response.read()

# request = urllib2.Request("http://www.baidu.com")
# #添加数据
# request.add_data('key',"value")
# #添加http header
# request.add_header('User-Agent','Mozilla/5.0')
#
# response = urllib2.urlopen(request)
#
# print(response)

def first_test(fun):
    def wper(*args,**w):
        print("first test")
        return fun(*args,**w)
    return wper

def after_test(fun):
    def wper(*args,**w):
        f = fun(*args,**w)
        print("after_test")
        return f
    return wper

@after_test
def hello():
    print("hello")

hello()
