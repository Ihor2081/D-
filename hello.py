from flask import Flask, redirect, url_for
app = Flask(__name__)

# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#    return 'Blog Number %d' % postID
#
# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#    return 'Revision Number %f' % revNo

# @app.route('/admin')
# def hello_admin():
#    return 'Hello Admin'
#
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest
#
# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))
#
# if __name__ == '__main__':
#    app.run(debug=True)

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

# @app.route('/success/<name>')
# def success(name):
#    return 'вітаємо %s' % name
#
# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))

@app.route('/')
def index():
   return render_template(hello.html)

if __name__ == '__main__':
   app.run(debug = True)