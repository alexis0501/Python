from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'a key'
            
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('index2.html')

@app.route('/process', methods=["POST"])
def process(): 
    if request.form['language']=="0":
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/success")

if __name__=="__main__":   
    app.run(debug=True) 
    


