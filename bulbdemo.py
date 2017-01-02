import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   18 : {'name' : 'BULB 1', 'state' : GPIO.LOW},
   23 : {'name' : 'BULB 2', 'state' : GPIO.LOW},
   24 : {'name' : 'BULB 3', 'state' : GPIO.LOW},
   25 : {'name' : 'BULB 4', 'state' : GPIO.LOW},
   12 : {'name' : 'BULB 5', 'state' : GPIO.LOW},
   16 : {'name' : 'BULB 6', 'state' : GPIO.LOW},
   20 : {'name' : 'BULB 7', 'state' : GPIO.LOW},
   21 : {'name' : 'BULB 8', 'state' : GPIO.LOW},
   5 : {'name' : 'BULB 9', 'state' : GPIO.LOW},
   17 : {'name' : 'BULB 10', 'state' : GPIO.LOW},
   27 : {'name' : 'BULB 11', 'state' : GPIO.LOW},
   22 : {'name' : 'BULB 12', 'state' : GPIO.LOW},
}

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."


   if action == "g1on":
      # Set the pin high:
      GPIO.output(18, GPIO.HIGH)
      GPIO.output(23, GPIO.HIGH)
      message = "Turned " + "GROUP" + " on."
   if action == "g1off":
      # Set the pin high:
      GPIO.output(18, GPIO.LOW)
      GPIO.output(23, GPIO.LOW)
      # Save the status message to be passed into the template:
      message = "Turned " + "GROUP" + " off."

   if action == "g2on":
      # Set the pin high:
      GPIO.output(25, GPIO.HIGH)
      GPIO.output(12, GPIO.HIGH)
      GPIO.output(16, GPIO.HIGH)

      # Save the status message to be passed into the template:
      message = "Turned " + "GROUP" + " on."
   if action == "g2off":
      GPIO.output(25, GPIO.LOW)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(16, GPIO.LOW)

      message = "Turned " + "GROUP" + " off."

   if action == "g3on":
      # Set the pin high:
      GPIO.output(18, GPIO.HIGH)
      GPIO.output(23, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + "GROUP" + " on."

   if action == "g3off":
      GPIO.output(18, GPIO.LOW)
      GPIO.output(23, GPIO.LOW)

      # Save the status message to be passed into the template
      message = "Turned " + "GROUP" + " off."

   if action == "g4on":
      # Set the pin high:
      GPIO.output(18, GPIO.HIGH)
      GPIO.output(24, GPIO.HIGH)
      GPIO.output(12, GPIO.HIGH)
      GPIO.output(20, GPIO.HIGH)

      # Save the status message to be passed into the template:
      message = "Turned " + "GROUP" + " on."

   if action == "g4off":
      GPIO.output(18, GPIO.LOW)
      GPIO.output(24, GPIO.LOW)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(20, GPIO.LOW)
      message = "Turned " + "GROUP" + " off."

   if action == "g5on":
      # Set the pin high:
      # Set the pin high:
      GPIO.output(23, GPIO.HIGH)
      GPIO.output(25, GPIO.HIGH)
      GPIO.output(16, GPIO.HIGH)
      GPIO.output(21, GPIO.HIGH)

      message = "Turned " + "GROUP" + " on."

   if action == "g5off":
      GPIO.output(23, GPIO.LOW)
      GPIO.output(25, GPIO.LOW)
      GPIO.output(16, GPIO.LOW)
      GPIO.output(21, GPIO.LOW)

      message = "Turned " + "GROUP" + " off."

   if action == "g6on":
      # Set the pin high:
      GPIO.output(5, GPIO.HIGH)
      GPIO.output(17, GPIO.HIGH)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.HIGH)

# Save the status message to be passed into the template:
      message = "Turned " + "GROUP" + " on."

   if action == "g6off":
      GPIO.output(5, GPIO.LOW)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.LOW)
      GPIO.output(22, GPIO.LOW)
      message = "Turned " + "GROUP" + " off."

   if action == "gallon":
      # Set the pin high:
      GPIO.output(18, GPIO.HIGH)
      GPIO.output(23, GPIO.HIGH)
      GPIO.output(24, GPIO.HIGH)
      GPIO.output(25, GPIO.HIGH)
      GPIO.output(12, GPIO.HIGH)
      GPIO.output(16, GPIO.HIGH)
      GPIO.output(20, GPIO.HIGH)
      GPIO.output(21, GPIO.HIGH)
      GPIO.output(5, GPIO.HIGH)
      GPIO.output(17, GPIO.HIGH)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.HIGH)
# Save the status message to be passed into the template:
      message = "Turned " + "GROUP" + " on."

   if action == "galloff":
      GPIO.output(18, GPIO.LOW)
      GPIO.output(23, GPIO.LOW)
      GPIO.output(24, GPIO.LOW)
      GPIO.output(25, GPIO.LOW)
      GPIO.output(12, GPIO.LOW)
      GPIO.output(16, GPIO.LOW)
      GPIO.output(20, GPIO.LOW)
      GPIO.output(21, GPIO.LOW)
      GPIO.output(5, GPIO.LOW)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.LOW)
      GPIO.output(22, GPIO.LOW)
      message = "Turned " + "GROUP" + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'message' : message,
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
