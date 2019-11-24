from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def instructors_info():

    db_path = "F:/desktop/lectures/SSW-810/assignments/SSW-810/810_startup.db"
    try:
        db = sqlite3.connect(db_path)
    except sqlite3.OperationalError:
        return f"Error: Unable to open database at {db_path}"
    else:
        query = """SELECT InstructorCWID, Name, Dept, Course, count(*)
                FROM instructors, grades
                WHERE InstructorCWID=CWID
                GROUP BY InstructorCWID, Course"""
        data = [{'cwid': cwid, 'name': name, 'dept': dept, 'course': course,
                'count': count} for cwid, name, dept,
                course, count in db.execute(query)]

        db.close()

        return render_template(
            'Instructor_table.html',
            title='Stevens Repository',
            page_title='Instructors Repository',
            table_title='Instructors student count',
            instructors=data
        )


app.run(debug=True)
