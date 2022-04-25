from flask_app import app
from flask import render_template, flash, redirect, request, session 
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/recipes') #made change write notes,was success -> recipes
    return render_template('main_page.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/') #this will stay the same

@app.route('/register', methods=['POST'])
def register():
    if not User.register_validation(request.form):
        return redirect('/')
    snek = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': snek,
    }
    flash("You have been successfully logged in!")
    user = User.save(data)
    session['user'] = user
    return redirect('/recipes')  #the register stays the same except the redirect in this line bc after registering it validates and takes u to next page

@app.route('/recipes') #this changes to whatever the line is above
def recipes(): # change to what
    if 'user' not in session:
        return redirect('/')
    return render_template('recipes.html', recipes=Recipe.get_all_user_recipes(), user = User.get_user_by_id({'id':session['user']}))

@app.route('/login', methods=['POST'])
def login():
    user = User.get_user_by_email({'email': request.form['email']})
    if not User.login_validation(user, request.form['password']):
        return redirect('/')

    session['user'] = user.id

    return redirect('/recipes')