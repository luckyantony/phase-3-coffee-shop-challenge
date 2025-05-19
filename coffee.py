class coffee:
    
    def __init__(self, name):
        if isinstance(name, str) and len(name) >=3:
            self.name = name
        
        else:
            return ValueError("Name must be a string of atleast 3 characters.")