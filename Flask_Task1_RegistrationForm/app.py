from flask import Flask, render_template, url_for, redirect, flash
from forms import Registration_Form, Login_Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5df76650449189ecfd05ef8bf6f4b49'

data_file = "userdata.txt"

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration_Form()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        with open(data_file,'a') as file:
            file.write(f"{username},{password}\n")
            
        flash(f"Account successfully created for {username}", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user_exist = False
        try:
            with open(data_file, 'r') as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(',')
                    if stored_username == username and stored_password == password:
                        user_exist = True
                        break
        except FileNotFoundError:
            flash("No users registered yet!", 'danger')
            return redirect(url_for('login'))
            
        if user_exist:
            flash("Logged In Successfully", 'success')
            return redirect(url_for('homepage'))
        else:
            flash("Invalid username or password", 'danger')
            
    return render_template('login.html', title='Login', form=form)
    

if __name__ == "__main__":
    app.run(debug=True, port=8000)