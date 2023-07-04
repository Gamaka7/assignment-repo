from app import app
from flask import render_template, request, redirect
from models import providers_list
import random

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home Page")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register')
def register():
    return render_template('register.html', title="Register")

@app.route('/login')
def login():
    return render_template('login.html', title="Login")

@app.route('/forget-password')
def forget_password():
    return render_template('forget-password.html', title="Forget Password")

## APIs

#GET ALL
@app.route('/providers')
def providers():
    return render_template('providers/providers-list.html', title="Service Providers", providers=providers_list)

def build_provider_object(request,id):
        return  {
                "id": id,
                "firstname": request.form['firstname'],
                "lastname": request.form['lastname'],
                "position": request.form['position'],
                "company": request.form['company'],
                  } 

def getProviderIndex(id, providers_list):
    for i in range(0,len(providers_list)):
        if providers_list[i]['id'] == int(id):
            return i
    return None

#POST - ADD
@app.route('/providers/add-provider', methods = ["GET","POST"])
def add():
    if request.method == 'POST':
        id = random.randint(100000,999999)
        provider = build_provider_object(request,id)
        providers_list.append(provider)
        return redirect('/providers')

    return render_template('/providers/provider-add-form.html', title="Add Provider", providers=providers_list)


#EDIT - UPDATE
@app.route('/providers/edit/<id>', methods = ["GET","POST"])
def edit(id):
    provider = None
    index = getProviderIndex(id,providers_list)
    if request.method == 'POST':
        provider = build_provider_object(request,int(id))
        if index is not None:
            providers_list[index] = provider
        return redirect('/providers')

    if index is not None:
        provider = providers_list[index]

    return render_template('providers/provider-edit-form.html', title="Update Provider", provider=provider, id=id)


#DELETE
@app.route('/providers/delete/<id>')
def delete(id):
    index = getProviderIndex(id,providers_list)
    if index is not None:
        del providers_list[index]
    return redirect('/providers')