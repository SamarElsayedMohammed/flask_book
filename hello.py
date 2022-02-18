from flask import Flask,template_rendered
# from flask.ext.script import Manager


test = Flask(__name__)
# manager = Manager(test)
# ...
# if __name__ == '__main__':
#     manager.run()


from flask import make_response
from flask import redirect


from flask import abort
# @test.route('/user/<id>')
# def get_user(id):
#     # user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, %s</h1>' % user.name

@test.route('/')
# def index():
#     return redirect('http://www.example.com')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

# @test.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400
    # user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser is %s</p>' % user_agent
    # return '<h1>hello world</h1>'

@test.route('/user/<name>')
def name(name):
    # return '<h1>hello ,%s!</h1>'%name
    # return 'hello %s'%name
    return '<h1> hello {{ name }}</h1>'

if __name__ == '__main__':
    test.run(debug=True)