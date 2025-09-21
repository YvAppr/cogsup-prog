
"""Open two_squares.py. Write a script that displays two squares side by 
side, the left one red, the right one green. Leave the fixation cross out.
The two squares should be separated by 200 pixels but centered as a whole.
 Present them on-screen until a key is pressed."""


# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.defaults.initialise_delay = 0 # No countdown
control.defaults.window_mode = True # Not full-screen
control.defaults.fast_quit = True # No goodbye message

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)


# Create a 50px-lenght Square
square1 = stimuli.Rectangle(size=(50,50), colour='red', position=(-100,0))
square2 = stimuli.Rectangle(size=(50,50), colour='green',position=(100,0))
# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross

square1.present(clear=True, update=False)
square2.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()