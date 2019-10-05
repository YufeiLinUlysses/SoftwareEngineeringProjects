from flask import Flask, session, redirect, url_for, escape, request,render_template
import datetime
#import Classses

app = Flask(__name__)


"""
Something to look at for server side 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = new User()
        if(user.login(request.form['email'], request.form['password'])):
            time = datetime.datetime.now()
            return redirect(url_for('index'))
        else:
            #returns to login page with error message
    return render_template("index.html")


@app.route('/logout', methods=['GET'])
def logout():
    user = pickle.load(session['user'])
    user.logout()
    return redirect(url_for('login'))"""

"""
    Unlike a Cookie, Session data is stored on server. 
    Session is the time interval when a client logs into a server and logs out of it. 
    The data, which is needed to be held across this session, is stored in a temporary directory on the server.
    A session with each client is assigned a Session ID. 
    The Session data is stored on top of cookies and the server signs them cryptographically. 
    For this encryption, a Flask application needs a defined SECRET_KEY.
"""
# secret key: for e.g.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
time = 0

@app.route('/')
def index():
    if 'username' in session:
        #return 'You are still logged in as %s' % escape(session['username'])
        return render_template("main.html", data = session['username'])
    return render_template("index.html")#'You need to go to login html to log in (not in session!)'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['email']
        session['pwd'] = request.form['password']
        # user in session than go to index html
        return redirect(url_for('index'))
    # by default it returns to login in page
    return render_template("index.html")


@app.route('/logout', methods = ['GET'])
def logout():
    # removing username from the session:
    session.pop('username', None)
    # we redirect to login page after we logout or we'd redirect to index file!
    return redirect(url_for('login'))

@app.route('/work', methods = ['POST'])
def work():
    if 'username' in session:
        #return 'You are still logged in as %s' % escape(session['username'])
        return render_template("work.html", data=session['username'])
    return render_template("index.html")

@app.route('/docs', methods=['POST'])
def docs():
    if 'username' in session:
        #return 'You are still logged in as %s' % escape(session['username'])
        return render_template("document.html", data=session['username'])
    return render_template("index.html")

@app.route('/createDocs', methods=["POST"])
def createDocs():
    if 'username' in session:
        #return 'You are still logged in as %s' % escape(session['username'])
        return render_template("create_document.html", data=session['username'])
    return render_template("index.html")

@app.route('/library', methods=["POST"])
def library():
    if 'username' in session:
        #return 'You are still logged in as %s' % escape(session['username'])
        return render_template("library.html", data=session['username'])
    return render_template("index.html")

@app.route('/profile', methods=['POST'])
def profile():
    if 'username' in session:
        #return 'You are still logged in as %s' % escape(session['username'])
        return render_template("user_profile.html")
    return render_template("user_profile.html")

@app.route('/contacts', methods=['POST'])
def contacts():
    if 'username' in session:
        #return 'You are still logged in as %s' % escape(session['username'])
        return render_template("contacts.html", data=session['username'])
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
