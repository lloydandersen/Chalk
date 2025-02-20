"""The Chalk module is the staging place for the entire Chalk build engine."""
from starter import Starter
from splitter import Splitter
from checker import Checker
from cleaner import Cleaner


class Chalk():
    """The core Chalk Object."""
    def __init__(self, file_handle):
        self.file_handle = file_handle
        self.file_contents: list = []
        self.global_document_content: list = []
        self.source_content: list = []
        self.imports_content: list = []
        self.problem_contents: list = []

        self.global_document_dict: dict = {}
        self.source_dict: dict = {}
        self.imports_dict: dict = {}
        self.problem_dict: dict = {}

        self.author_list: list = []
        self.vars_dict: dict = {}
        self.media_dict: dict = {}

        self.check_object: Checker = Checker(global_document_content=self.global_document_content,
                        source_content=self.source_content,
                        imports_content=self.imports_content,
                        problem_contents=self.problem_contents)

    def run(self):
        """The run method schedules the cleanup and parsing of Chalk file."""
        self.load()
        self.split()
        self.clean()

    def load(self):
        """This method loads a chalk file into memory."""
        handle = Starter(file_handle=self.file_handle)
        self.file_contents = handle.load_file()
        
    def split(self):
        """The split function cleans up and splits chalk data into more accessible chunks."""
        splitted_object = Splitter(file_contents=self.file_contents, check_object=self.check_object)
        splitted_content = splitted_object.run()

        self.file_contents = splitted_content[0]
        self.global_document_content = splitted_content[1]
        self.source_content = splitted_content[2]
        self.imports_content = splitted_content[3]
        self.problem_contents = splitted_content[4]

    def clean(self):
        """The clean method further takes the chalk data and creates python usable dictionaries and lists."""
        cleaner_object = Cleaner(global_document_content=self.global_document_content,
                        source_content=self.source_content,
                        imports_content=self.imports_content,
                        problem_contents=self.problem_contents, check_object=self.check_object)
        cleaner_content = cleaner_object.run()
        
        self.global_document_dict = cleaner_content[0]
        self.source_dict = cleaner_content[1]
        self.imports_dict = cleaner_content[2]
        self.problem_dict = cleaner_content[3]
        self.author_list = cleaner_content[4]
        self.vars_dict = cleaner_content[5]
        self.media_dict = cleaner_content[6]
        

if __name__ == '__main__':
    x  = Chalk('samples\\chalk.chalk')
    x.run()
    print(x.author_list)
    
    

    
