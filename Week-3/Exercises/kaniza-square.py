import expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY
control.set_develop_mode() #not displaying the boring stuff


# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "display edges", background_colour=C_GREY)

control.initialize(exp)

width, height = exp.screen.size
circle_radius=width//20
square_length=width//4

left_top=stimuli.Circle(radius=circle_radius,colour='black', position=(-square_length//2,square_length//2))
right_top=stimuli.Circle(radius=circle_radius,colour='black', position=(square_length//2,square_length//2))
left_bottom=stimuli.Circle(radius=circle_radius,colour='white',position=(-square_length//2,-square_length//2))
right_bottom=stimuli.Circle(radius=circle_radius,colour='white', position=(square_length//2,-square_length//2))
square=stimuli.Rectangle(size=(width//4,width//4),colour=C_GREY,position=(0,0))
# Start running the experiment
control.start(subject_id=1)

left_top.present(clear=True, update=False)
right_top.present(clear=False, update=False)
left_bottom.present(clear=False, update=False)
right_bottom.present(clear=False, update=False)
square.present(clear=False,update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()