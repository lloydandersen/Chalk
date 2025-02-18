"""The imported class prepares for problem libraries."""
class Imported():
    def __init__(self, imported_slice: list) -> list:
        self.imported_slice: list = imported_slice
        self.imported_list: list = []
        self.alias_list: list = []
        self.library_list: list = []
        self.supported_list: list = ["standard", "math"]


        self.parse()
        self.populate_imports()
        self.clean_lists()
        
        
    def parse(self):
        """This turns the slice into the imports list."""
        self.imported_slice.remove("[IMPORT]")
        # print(self.imported_slice)
        for i in self.imported_slice:
            self.imported_list.append(i.partition("="))

        # print(self.imported_list)

    def populate_imports(self):
        for i in self.imported_list:
            alias = i[0]
            name = i[2]
            self.alias_list.append(alias)
            self.library_list.append(name)

        


    def clean_lists(self):
        for i in self.library_list:
            i.lstrip()
            print(i)
           




        print(self.library_list)
        print(self.alias_list)

        
            
if __name__ == "__main__":
    Imported(['[IMPORT]', 'std = "standard"', 'math = "math"'])

