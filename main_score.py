from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/scores')
def table_score():
    with open('scores.txt', 'r') as txt_import:
        if txt_import:
            return txt_import.readlines()
        else:
            return False


app.run(port=5000)

# אני מצליח לראות את הפלט של קובץ scores.txt
# אבל אני לא מבין איך אני מקשר אותו לקובץ HTML שיצרתי.

# גם אחרי שהוספתי את הקובץ main_score עם ה flask
# כשאני מפעיל את המשחק הוא לא עובד כי ה flask בעצם תופס את החלון

