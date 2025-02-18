"""The parser parses up your chalk file."""
from chalk import imported 

class Parser():
    """The PARSER class"""
    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.handle: list = []
        self.problems: list = []
        self.imported_list: list = []
        self.imported_slice: list = []
        

        with open(self.file_name, "r", encoding="utf-8") as file:
            self.handle = file.readlines()
            self.clean_up()
            self.header_check()
            self.imported_parse()

    def clean_up(self) -> None:
        """The cleanup function"""   
        self.handle = list(filter(lambda x: x != "\n", self.handle))
        self.handle = list(map(lambda x: x.strip(), self.handle))

    def header_check(self) -> None:
        """The header check, checks the header for syntax/semantic errors."""
        chalk_counter = self.handle.count("[CHALK]")
        if chalk_counter == 1:
            pass
        elif chalk_counter > 1:
            raise Exception(f"""You must have only one [CHALK] header block, you have {chalk_counter}\n""")
        else:
            raise Exception("You need atleast one [CHALK] header block.")
        
        chalk_location = self.handle.index("[CHALK]")
        if chalk_location != 0:
            raise Exception("The [CHALK] header must be at the top of the file.")
        
    def imported_parse(self):
        try:
            import_index = self.handle.index("[IMPORT]")
            print(import_index)
        except:
            raise Exception("You need to use an [IMPORT] block for imports. It should come after [CHALK] and [SOURCE] blocks.")

        first_problem_index = self.handle.index("[BEGIN]")
        print(first_problem_index)

        self.imported_slice = self.handle[import_index:first_problem_index]
        


        imported.Imported(self.imported_slice)




if __name__ == "__main__":
    x = Parser("samples\\perfect_chalk.chalk")
    
    