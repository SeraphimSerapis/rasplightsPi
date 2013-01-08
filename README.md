
rasplightsPi
=====

This is a tiny demo project in Python which leverages the package [RPi.GPIO](http://pypi.python.org/pypi/RPi.GPIO) to toggle three LEDs via GPIO.

How it works
----
1. the package needs to be imported:

		import RPi.GPIO as GPIO
		
2. set which pin numbers you want to use (optional)

		GPIO.setmode(GPIO.BOARD)
		
3. set a pin as output channel

		GPIO.setup(11, GPIO.OUT)
		
4. turn the led on

		GPIO.output(11, True)
	
5. turn the led off

		GPIO.output(11, FALSE)
		
____
The demo offers some functions to do this in a more comfortable way.

- **setup(port)** - sets the port to be an output channel
- **on(port)** - power the port
- **off(port)** - turn it off
- **init(ports)** - does the setup for a provided array of ports
- **blink(port)** - turns it on, waits a second, turns it off
- **lightshow(ports)** - just some more blinking awesomeness ;)


Author
-----
Tim Messerschmidt - PayPal Developer Evangelist - [tmesserschmidt@paypal.com](mailto:tmesserschmidt@paypal.com)