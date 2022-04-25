from flask import Flask, render_template, redirect, session
app = Flask(__name__) 
app.secret_key = 'key_name'

@app.route('/') 
def clicker():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0
    return render_template("index.html")

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')
    
if __name__=="__main__":     
    app.run(debug=True) 


