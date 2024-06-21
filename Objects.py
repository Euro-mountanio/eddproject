class Objects:
    valid_states = ["False ", "True", "None "]
    
    def __init__(valid_state):   
        if valid_state in valid_states:
            Isliving = valid_state   
            Ismobility = valid_state   
            HasMass = valid_state 
            Hasvolume = valid_state 
        else:
            raise ValueError(" not valid entry")    

class rock(object):
    valid_states = ["False ", "True","None" ]
    def __init__( valid_state):
        super.__init__()
        if valid_state in valid_states:
            IsRegilar= valid_state
            HasColor = valid_state
        else:
            raise ValueError(" not valid entry")    

class mountain(rock):
    valid_state = ["True", "False", " None"]
    def __init__(self, valid_state):
        super().__init__()
        if valid_state in valid_state:
            self.IsMassive= valid_state
    def location(self):
        valid_state = ["False ", "True","None" ]
        super().__init__()
        if valid_state in valid_state:
            self.IsOnLand = valid_state    

class hill(mountain):
    valid_state = ["True", "False", " None"]
    def __init__(self, valid_state):
        super().__init__()
        if valid_state in valid_state:
            self.Issmaller = valid_state

