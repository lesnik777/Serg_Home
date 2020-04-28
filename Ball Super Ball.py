class Ball(object):
    def __init__(self,s='regular'):       
        self.ball_type = s

ball1 = Ball()
ball2 = Ball("super")
#ball_type = Ball("Super")
print(ball1.ball_type) 
print(ball2.ball_type)