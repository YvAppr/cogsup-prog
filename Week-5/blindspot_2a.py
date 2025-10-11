from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN,K_UP,K_LEFT,K_RIGHT,K_SPACE, K_a, K_z


""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(["Subject_id","eye","radius", "x_cord","y_cord"])
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(side):
    if side=='R':
        d0=1
    elif side=='L':
        d0=-1
    else : 
        print("Please make sure to enter 'R' or 'L' as a parameter in run_trial()")
        return
    
    """Initialization"""
    text=stimuli.TextScreen(heading='Blind-spot finder', text_justification=0, text = 'The goal of this experiment is to find the blind spot : \n \n Regarding the condition Left "L" or Right "R" in run_trial, close the corresponding eye. \n\n Press the arrows to move the circle and "a" to get it smaller or z to get it bigger \n\nThe goal is to make the circle completly disapear from your sight')
    text.present(True, True)
    exp.clock.wait(5000)

    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300*d0, 0])
    fixation.preload()

    radius = 75
    circle = make_circle(radius)

    fixation.present(True, False)
    circle.present(False, True)

    """Controls"""
    while True:
        key,time_pressed=exp.keyboard.wait(keys=[K_DOWN,K_UP,K_LEFT,K_RIGHT, K_a,K_z,K_SPACE])
        radius= circle.radius 
        dx,dy=radius//3,radius//3 # space shift 
        if key==K_DOWN:
            circle.move((0,-dy))
        if key==K_UP:
            circle.move((0,dy))
        if key== K_RIGHT:
            circle.move((dx,0))
        if key==K_LEFT:
            circle.move((-dx,0))
        if key==K_a:
            radius+=-5 
            circle = make_circle(radius,circle.position)
        if key==K_z:
            radius+=5
            if radius>=0: 
                circle = make_circle(radius,circle.position)
            pass

        fixation.present(True, False)
        circle.present(False, True)

        if key==K_SPACE:
            exp.data.add([1,side,circle.radius,circle.position[0],circle.position[1]])
            break

control.start(subject_id=1)

run_trial('R')
    
control.end()