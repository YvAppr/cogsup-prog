import expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY
control.set_develop_mode() #not displaying the boring stuff

def kanizsa_rectangle(rectangle_ratio=1, rectangle_scale=0.3, circle_scale=0.05):
    """
    create and display kanizsa rectangle given rectangle ratio, and rectangle, circle scale
    """
    # Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
    exp = design.Experiment(name = "display edges", background_colour=C_GREY)

    control.initialize(exp)
    width, height = exp.screen.size
    rectangle_width=width*rectangle_scale
    rectangle_heigth=rectangle_width/rectangle_ratio
    circle_radius=width*circle_scale
    

    left_top=stimuli.Circle(radius=circle_radius,colour='black', position=(-rectangle_width//2,rectangle_heigth//2))
    right_top=stimuli.Circle(radius=circle_radius,colour='black', position=(rectangle_width//2,rectangle_heigth//2))
    left_bottom=stimuli.Circle(radius=circle_radius,colour='white',position=(-rectangle_width//2,-rectangle_heigth//2))
    right_bottom=stimuli.Circle(radius=circle_radius,colour='white', position=(rectangle_width/2,-rectangle_heigth//2))
    square=stimuli.Rectangle(size=(rectangle_width,rectangle_heigth),colour=C_GREY,position=(0,0))
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

kanizsa_rectangle(rectangle_ratio=2)