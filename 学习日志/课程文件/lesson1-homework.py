# lesson1-homework.py - 第一课课后练习

from bottle import route, run, request, response

# 动手题 1: 处理 GET 和 POST 请求
# 任务：创建一个 /login 路由
# - GET 请求返回一个登录表单
# - POST 请求返回 "Login Successful"


# 动手题 2: 使用 request 对象
# 任务：创建一个 /search 路由
# - 从 URL 查询参数中获取 keyword
# - 返回 "You searched for: [keyword]"


# 动手题 3: 使用 response 对象
# 任务：创建一个 /set-cookie 路由
# - 设置一个名为 'my_cookie'，值为 'hello_bottle' 的 cookie



# 思考题 1: 性能的艺术
# 问题：为什么 Bottle 要将静态路由和动态路由分开处理？这对性能有什么影响？
# 请将你的答案写在这里作为注释：
#
# 答：
#


if __name__ == '__main__':
    # 使用 if __name__ == '__main__': 是一个好习惯
    # 这样在其他文件导入此文件时，不会直接运行服务器
    run(host='localhost', port=8081, debug=True, reloader=True)
