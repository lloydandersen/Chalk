class Starter():
    def __init__(self, file_handle):
        self.file_handle: object = file_handle
        self.file_contents: list = []
        


    def load_file(self) -> list:
        handle = open(f'{self.file_handle}', "r")
        self.file_contents = handle.readlines()
        
        return self.file_contents



