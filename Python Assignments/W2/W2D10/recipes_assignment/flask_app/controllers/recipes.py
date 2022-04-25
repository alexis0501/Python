from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,redirect,request,session,flash
from flask_app.models.recipe import Recipe
from flask_app import app

@app.route('/delete/<int:recipe_id>/<int:user_id>')
def delete_recipe(recipe_id,user_id):
    if user_id != session['user']:   #makes sure nobody else can delete urs
        flash("You can only delete your recipes")
        return redirect('/')
    Recipe.delete_recipe({'id': recipe_id})
    return redirect('/recipes') #after deleting redirect to home page

@app.route('/create', methods=['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        'user_id': session['user'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_thirty': request.form['under_thirty'],
    }
    Recipe.create_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/new')
def show_create_recipe():
    if 'user' not in session:
        flash("Log in to create recipe")
        return redirect('/')
    return render_template('add_recipe.html') #after creating redirect to create page


@app.route('/recipes/<int:recipe_id>/<int:user_id>')
def show_recipe(recipe_id,user_id):
    if 'user' not in session:
        flash("Log in to see recipe")
        return redirect('/')
    if session['user'] != user_id:
        flash("You cannot see other's recipes")
        return redirect('/recipes')

    return render_template('view_recipe.html',recipe=Recipe.get_recipe_by_id({'id':recipe_id}) )

@app.route('/edit/<int:recipe_id>', methods=['POST'])
def edit_recipe(recipe_id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/{recipe_id}/edit')

    data = {
        'id': recipe_id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_thirty': request.form['under_thirty'],
    }
    Recipe.edit_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/<int:recipe_id>/<int:user_id>/edit')
def show_edit_recipe(recipe_id,user_id):
    if 'user' not in session:
        flash("Log in to edit your recipe")
        return redirect('/')
    if session['user'] != user_id:
        flash("Can't edit someone else's recipe")
        return redirect('/recipes')
    return render_template('edit_recipe.html',recipe=Recipe.get_recipe_by_id({'id': recipe_id}))
