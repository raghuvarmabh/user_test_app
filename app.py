from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host='127.0.0.1',
        dbname='replace me',
        user='replace me',
        password='replace me'
    )

@app.route('/')
def home():
    return redirect(url_for('view_users'))

@app.route('/users')
def view_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM public.users ORDER BY id")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('view_users.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
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
        return redirect(url_for('view_users'))
    return render_template('add_user.html')

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('view_users'))

    cur.execute("SELECT name, age FROM users WHERE id=%s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('update_user.html', user=user, user_id=user_id)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('view_users'))

if __name__ == '__main__':
    app.run(debug=True)
