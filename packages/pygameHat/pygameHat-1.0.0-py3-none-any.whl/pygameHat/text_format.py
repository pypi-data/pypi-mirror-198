class TextFormat:
    def __init__(self):
        self.text = ""
    
    def clear(self):
        self.text = ""
    def delete_from_end(self):
        if len(self.text) > 0:
            self.text = self.text[:-2]