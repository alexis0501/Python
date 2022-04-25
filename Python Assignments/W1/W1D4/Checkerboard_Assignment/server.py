from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')
def check():
    return render_template('index.html')

@app.route('/4')
def checker():
    return render_template('index2.html')

@app.route('/<int:num1>/<int:num2>')
def checkers(num1, num2):
    return render_template('index3.html', col = num1, row = num2)

if __name__=="__main__":     
    app.run(debug=True) 


