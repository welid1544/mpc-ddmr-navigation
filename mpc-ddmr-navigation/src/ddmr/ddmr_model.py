class DDMRModel:
    def __init__(self):
        self.state = None
        self.reference = None

    def set_reference(self, reference):
        self.reference = reference

    def update_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state