from flask import Blueprint, render_template, request, redirect, url_for
import psycopg2

users_bp = Blueprint('users', __name__)

def get_db_connection():
    return psycopg2.connect(
        host='127.0.0.1',
        dbname='replace me',
        user='replace me',
        password='replace me'
    )

@users_bp.route('/')
def home():
    return redirect(url_for('users.view_users'))

@users_bp.route('/users')
def view_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM public.users ORDER BY id")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('users/view_users.html', users=users)

@users_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('users.view_users'))
    return render_template('users/add_user.html')

@users_bp.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        cur.execute("UPDATE users SET name=%s, age=%s WHERE id=%s", (name, age, user_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('users.view_users'))

    cur.execute("SELECT name, age FROM users WHERE id=%s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('users/update_user.html', user=user, user_id=user_id)

@users_bp.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('users.view_users'))
