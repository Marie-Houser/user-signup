from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env= jinja2.Environment(loader = jinja2.FileSystemLoader (template_dir), autoescape=True)

app=Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user-signup.html')

@app.route("/welcome")
def welcome():
   return render_template('welcome.html', username=username)


#checking validation for user-signup
@app.route('/', methods=['POST'])
def validate_signup( ):

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form["verify_password"]
    email=request.form["email"]
    
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    
    #testing username
    if len(username)<3:
        username_error = 'Please choose a username longer than 3 characters.'
        
    elif len(username)>20:
        username_error = 'Please choose a username shorter than 20 characters.'
        
    else:
        for char in username:
            if char ==' ':
                username_error = 'Your username is not allowed to have a space.  Please choose a different username.'

    #testing password
    for char in password:
            if char ==' ':
                password_error = 'Your password is not allowed to have a space.  Please choose a different password.'

    if len(password)<3:
        password_error = 'Please choose a password longer than 3 characters.'
        password=''
        verify_password=''
        
    if len(password)>20:
        password_error = 'Please choose a password shorter than 20 characters.'
        password=''
        verify_password=''

    if password != verify_password:
        verify_password_error = "Passwords do not match.  Please retype."
        password=''
        verify_password=''
        
           

    #testing email: between 3-20, one @, one ., no spaces
    if email !='':
        for char in email:
            if char ==' ':
                email_error = 'Your email is not allowed to have a space.  Please choose a different email.' 

        if len(email)<3:
            email_error = 'Please choose an email longer than 3 characters.'
        
        if len(email)>20:
            email_error = 'Please choose an email shorter than 20 characters.'
       
         
        if email_error == '':
            period_count = 0
            for char in email:
                if char == '.':
                    period_count +=1
                else:
                    period_count = period_count
                if period_count != 1:
                    email_error = "Your email must have a single period.  Please try again."
                else:
                    email_error = ''

        if email_error == '':
            at_count = 0
            for char in email:
                if char == '@':
                    at_count +=1
                else:
                    at_count = at_count
                if at_count != 1:
                    email_error = "Your email must have a single '@'.  Please try again."
                else:
                    email_error = ''

    if not username_error and not password_error and not verify_password_error and not email_error:
        
        return render_template('welcome.html', username=username)

    else:
        return render_template('user-signup.html', 
        username_error=username_error, 
        password_error=password_error, 
        verify_password_error=verify_password_error, 
        email_error=email_error,
        username=username,
        password=password,
        email=email,
        verify_password=verify_password)
        
    

app.run()