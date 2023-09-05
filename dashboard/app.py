from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin to which the KY-026 sensor is connected
flame_sensor_pin = 17

# Set up the GPIO pin as an input
GPIO.setup(flame_sensor_pin, GPIO.IN)

@app.route('/')
def dashboard():
    flame_status = GPIO.input(flame_sensor_pin)
    if flame_status:
        flame_status_text = "Flame Detected"
        flame_status_class = "flame-detected"
    else:
        flame_status_text = "No Flame Detected"
        flame_status_class = "no-flame-detected"
    
    return render_template('dashboard.html', flame_status_text=flame_status_text, flame_status_class=flame_status_class)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
