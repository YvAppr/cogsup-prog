import expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY
control.set_develop_mode() #not displaying the boring stuff

def hermann_grid(square_size,innerline,rows,cols,square_color,bcg_color):

    """
    create and display hermann grid
    """
    # Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
    exp = design.Experiment(name = "Hermann Grid", background_colour=bcg_color)

    control.initialize(exp)
    width, height = exp.screen.size
    top_left_coordinates=(-(cols-1)*(square_size+innerline)//2,-(rows-1)*(square_size+innerline)//2)
    print(top_left_coordinates)
    stimuli_list=[]
    for r in range(rows):
        for c in range(cols):
            # we stock the stimuli inside a list 
            print(tuple(map(sum, zip(top_left_coordinates,(c*(square_size+innerline),r*(square_size+innerline))))))
            stimuli_list.append(stimuli.Rectangle(size=(square_size,square_size),colour=square_color,position=tuple(map(sum, zip(top_left_coordinates,(c*(square_size+innerline),r*(square_size+innerline)))))))

    # Start running the experiment
    control.start(subject_id=1)
    
    for i,sq in enumerate(stimuli_list):
        sq.present(clear=(i==0),update=False)
    
    exp.screen.update()

    # Leave it on-screen until a key is pressed
    exp.keyboard.wait()

    # End the current session and quit expyriment
    control.end()

hermann_grid(square_size=20,innerline=5,rows=10,cols=10,square_color=(0,0,0),bcg_color=(255,255,255))