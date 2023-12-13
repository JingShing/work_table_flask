from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        selected_users = request.form['selectedUsers']
        frequency = request.form['frequency']
        
        reminder_date = request.form.get('reminder_date_once')
        reminder_time_once = request.form.get('reminder_time_once')
        reminder_time_weekly = request.form.get('reminder_time_weekly')
        days_selected = request.form.getlist('days[]')

        print(f"Task: {task}")
        print(f"Recipients: {selected_users}")
        print(f"Frequency: {frequency}")
        print(f"Reminder Date (Once): {reminder_date}")
        print(f"Reminder Time (Once): {reminder_time_once}")
        print(f"Reminder Time (Weekly): {reminder_time_weekly}")
        print(f"Days Selected: {', '.join(days_selected)}")
        
        # return 'Form submitted successfully!'
        # return f"Task: {task}<br>Frequency: {frequency}<br>Selected Users: {selected_users}"
        return f"Task: {task}<br>Frequency: {frequency}<br>Selected Users: {selected_users}<br>\
            Reminder Date: {reminder_date}<br>Reminder Time Once: {reminder_time_once}<br>\
            Reminder Time Weekly: {reminder_time_weekly}<br>Days Selected: {days_selected}"
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
