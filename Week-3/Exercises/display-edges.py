import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode() #not displaying the boring stuff


# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "display edges")

control.initialize(exp)

width, height = exp.screen.size
length=width*0.0

left_top=stimuli.Rectangle(size=(length,length),colour='red', line_width=1, position=((-width//2)+length//2,(height//2)-length//2))
right_top=stimuli.Rectangle(size=(length,length),colour='red', line_width=1, position=(width//2-length//2,height//2-length//2))
left_bottom=stimuli.Rectangle(size=(length,length),colour='red', line_width=1, position=(-width//2+length//2,-height//2+length//2))
right_bottom=stimuli.Rectangle(size=(length,length),colour='red', line_width=1, position=(width//2-length//2,-height//2+length//2 ))
# Start running the experiment
control.start(subject_id=1)

left_top.present(clear=True, update=False)
right_top.present(clear=False, update=False)
left_bottom.present(clear=False, update=False)
right_bottom.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()