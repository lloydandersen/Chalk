"""The parser parses up your chalk file."""
class Parser():
    """The PARSER class"""
    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.handle: list = []
        self.problems: list = []
        self.import_list: list = []
        

        with open(self.file_name, "r", encoding="utf-8") as file:
            self.handle = file.readlines()
            self.clean_up()
            self.header_check()

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
        
        import_index = self.handle.index("[IMPORT]")
        print(import_index)

        first_problem_index = self.handle.index("[BEGIN]")
        print(first_problem_index)

        import_slice = self.handle[import_index:first_problem_index]
        print(import_slice)


x = Parser("tests\\chalk\\chalk_sample_1.chalk")

#print(x.handle)
