# data classes only

# define the model ErrorPattern

class ErrorPattern:
    def __init__(self, name, keywords, solution):
        self.name = name
        self.keywords = keywords
        self.solution = solution
    def matches(self, text):
        return all(keyword in text for keyword in self.keywords)
    
