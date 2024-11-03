from gpiozero import LED
from time import sleep

# Define LEDs for Traffic Light A
red_A = LED(17)      # Red LED for Traffic Light A
amber_A = LED(27)    # Amber LED for Traffic Light A
green_A = LED(22)    # Green LED for Traffic Light A

# Define LEDs for Traffic Light B
red_B = LED(23)      # Red LED for Traffic Light B
amber_B = LED(24)    # Amber LED for Traffic Light B
green_B = LED(25)    # Green LED for Traffic Light B

def traffic_light_cycle():
    while True:
        # Traffic Light A Green, Light B Red
        red_B.on()          # Turn on the red light for Traffic Light B
        amber_B.off()       # Ensure amber light for Traffic Light B is off
        green_B.off()       # Ensure green light for Traffic Light B is off
        red_A.off()         # Turn off the red light for Traffic Light A
        amber_A.off()       # Ensure amber light for Traffic Light A is off
        green_A.on()        # Turn on the green light for Traffic Light A
        sleep(5)            # Keep the green light on for 5 seconds

        # Traffic Light A Amber
        green_A.off()       # Turn off the green light for Traffic Light A
        amber_A.on()        # Turn on the amber light for Traffic Light A
        sleep(2)            # Keep the amber light on for 2 seconds
        amber_A.off()       # Turn off the amber light for Traffic Light A

        # Traffic Light A Red, Light B Green
        red_A.on()          # Turn on the red light for Traffic Light A
        green_B.on()        # Turn on the green light for Traffic Light B
        red_B.off()         # Turn off the red light for Traffic Light B
        amber_B.off()       # Ensure amber light for Traffic Light B is off
        sleep(5)            # Keep the green light on for 5 seconds

        # Traffic Light B Amber
        green_B.off()       # Turn off the green light for Traffic Light B
        amber_B.on()        # Turn on the amber light for Traffic Light B
        sleep(2)            # Keep the amber light on for 2 seconds
        amber_B.off()       # Turn off the amber light for Traffic Light B

try:
    traffic_light_cycle()  # Start the traffic light cycle
except KeyboardInterrupt:
    # Turn off all LEDs when the program is stopped
    red_A.off()
    amber_A.off()
    green_A.off()
    red_B.off()
    amber_B.off()
    green_B.off()