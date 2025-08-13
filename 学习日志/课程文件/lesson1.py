# lesson1.py - Bottle 核心功能学习

from bottle import route, run, request, response

# 实践 1: Hello World
@route('/')
def index():
    return '<h1>Hello, World!</h1>'

# 实践 2: 动态路由
@route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

# 运行服务器
# host='localhost' 表示只有本机可以访问
# port=8080 是监听的端口号
# debug=True 可以在代码修改后自动重载服务器，并提供更详细的错误页面
run(host='localhost', port=8080, debug=True)
