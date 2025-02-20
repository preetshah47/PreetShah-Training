from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'e35618e745304bc5e36f2ae2ef6f91ce'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        role = request.form['role']
        new_user = User(username=username, email=email, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('User Registered Successfully', 'success')
        return redirect(url_for('dashboard'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['role'] = user.role
            session['username'] = user.username
            flash(f'Welcome {user.username}!', 'success')
            return redirect(url_for('view_users'))
        else:
            flash("Invalid Username or Password!", 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('dashboard'))


@app.route('/admin/users/', methods=['GET', 'POST'])
def view_users():
    if 'user_id' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))

    role = session['role']

    if request.method == 'POST':
        if role in ['Admin', 'Manager']:
            username = request.form['username']
            email = request.form['email']
            password = generate_password_hash(request.form['password'])
            new_role = request.form['role']

            new_user = User(username=username, email=email, password=password, role=new_role)
            db.session.add(new_user)
            db.session.commit()
            flash('User Created Successfully!', 'success')
            return redirect(url_for('view_users'))

    users = User.query.all()
    return render_template('users.html', users=users, role=role)


@app.route('/admin/users/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if 'user_id' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))

    user = User.query.get(user_id)
    if not user:
        flash('User not found!', 'danger')
        return redirect(url_for('view_users'))

    if session['role'] not in ['Admin', 'Manager']:
        flash('Access Denied!', 'danger')
        return redirect(url_for('view_users'))

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.role = request.form['role']
        db.session.commit()
        flash('User Updated Successfully!', 'success')
        return redirect(url_for('view_users'))

    return render_template('update_user.html', user=user)


@app.route('/admin/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if 'user_id' not in session or session['role'] != 'Admin':
        flash('Access Denied!', 'danger')
        return redirect(url_for('view_users'))

    user = User.query.get(user_id)
    if not user:
        flash('User not found!', 'danger')
        return redirect(url_for('view_users'))

    if user.role == 'Admin':
        flash('Cannot delete another Admin!', 'danger')
        return redirect(url_for('view_users'))

    db.session.delete(user)
    db.session.commit()
    flash('User Deleted Successfully!', 'success')
    return redirect(url_for('view_users'))


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, port=4444)
