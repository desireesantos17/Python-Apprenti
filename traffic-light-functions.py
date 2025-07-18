# Define indivdual traffic light functions 
def red_light():
    print("Stop! The light is red.")

def yellow_light():
    print("Caution! The light is yellow.")

def green_light():
    print("Go! The light is green.")

# Function to control the traffic light based on the given state
def traffic_light(state):
    if state == "red":
        red_light()

    elif state == "yellow":
        yellow_light()

    elif state == "green":
        green_light()
        
    else:
        print("Error:Invalid traffic light state!")

# Test cases
traffic_light("red")
traffic_light("yellow")
traffic_light("green")

# Add your own functions to handle other traffic light states
def flashing_red_light():
    print("Flashing red! Stop and proceed with caution.")

