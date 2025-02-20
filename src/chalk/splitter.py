from checker import Checker
class Splitter():
    def __init__(self, file_contents:list, check_object: Checker):
        self.file_contents: list = file_contents
        self.global_document_content: list = []
        self.source_content: list = []
        self.imports_content: list = []
        self.problem_contents: list = []
        self.check_object: Checker = check_object
        

    def run(self):
        self.clean_up()
        self.split()
        return self.file_contents, self.global_document_content, self.source_content, self.imports_content, self.problem_contents


    def split(self):
        header_content = []
        slice_end = self.file_contents.index('[BEGIN]')
        header_content = self.file_contents[0:slice_end]
        self.problem_contents = self.file_contents[slice_end:]

        source_index = header_content.index('[SOURCE]')
        imports_index = header_content.index('[IMPORT]')
        
        self.global_document_content = header_content[0:source_index]
        self.source_content = header_content[source_index:imports_index]
        self.imports_content = header_content[imports_index:]

        

    def clean_up(self):
        """basic cleanup"""
        self.file_contents = list(filter(lambda x: x != "\n", self.file_contents))
        self.file_contents = list(map(lambda x: x.strip(), self.file_contents))
        self.check_object.precheck(self.file_contents)
        
        




if __name__ == '__main__':
    pass
