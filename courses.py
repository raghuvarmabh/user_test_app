from flask import Blueprint, render_template, request, redirect, url_for
import psycopg2

courses_bp = Blueprint('courses', __name__)

def get_db_connection():
    return psycopg2.connect(
        host='127.0.0.1',
        dbname='replace me',
        user='replace me',
        password='replace me' 
    )

@courses_bp.route('/courses')
def view_courses():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, teacher FROM courses ORDER BY id")
    courses = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('courses/view_courses.html', courses=courses)

@courses_bp.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form['name']
        teacher = request.form['teacher1']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO courses (name, teacher) VALUES (%s, %s)", (name, teacher))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('courses.view_courses'))
    return render_template('courses/add_course.html')

@courses_bp.route('/update_course/<int:course_id>', methods=['GET', 'POST'])
def update_course(course_id):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        teacher = request.form['teacher']
       # cur.execute("UPDATE courses SET name=%s, teacher=%s WHERE id=%s", (name, teacher, course_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('courses.view_courses'))

    cur.execute("SELECT name, teacher FROM courses WHERE id=%s", (course_id,))
    # course = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('courses/update_course.html', course=course, course_id=course_id)

@courses_bp.route('/delete_course/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM courses WHERE id=%s", (222))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('courses.view_courses'))
