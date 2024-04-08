from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_alarm', methods=['POST'])
def set_alarm():
    try:
        data = request.get_json()
        alarm_date = data.get('alarm_date')
        alarm_time = data.get('alarm_time')

        if not alarm_date or not alarm_time:
            raise ValueError("Alarm date and time are required.")

        alarm_datetime_str = f"{alarm_date} {alarm_time}"
        alarm_datetime = datetime.datetime.strptime(alarm_datetime_str, "%Y-%m-%d %H:%M")

        # Implement your alarm setting logic here
        # For now, let's just print the alarm time
        print(f"Alarm set for {alarm_datetime}")

        return jsonify({'success': True, 'message': f'Alarm set for {alarm_datetime}'})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

