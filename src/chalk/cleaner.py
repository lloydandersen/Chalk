from checker import Checker
class Cleaner():
    def __init__(self, global_document_content: list, source_content: list, imports_content: list, problem_contents: list, check_object: Checker):
        self.global_document_content: list = global_document_content
        self.source_content: list = source_content
        self.imports_content: list = imports_content
        self.problem_contents: list = problem_contents
        self.check_object: Checker = check_object

        self.global_document_dict: dict = {}
        self.source_dict: dict = {}
        self.imports_dict: dict = {}
        self.problem_dict: dict = {} 
        self.author_list: list = []
        self.vars_dict: dict = {}
        self.media_dict: dict = {}


    def run(self) -> dict:
        self.global_clean()
        self.source_clean()
        self.imports_clean()
        self.problem_clean()

        return self.global_document_dict, self.source_dict, self.imports_dict, self.problem_dict, self.author_list, self.vars_dict, self.media_dict
    


    def global_clean(self):
        # print(self.global_document_content)
        global_clean_list = []

        for i in self.global_document_content:
            tup = i.partition(" = ")
            self.check_object.global_check(tup)
            global_clean_list.append(tup)

        
        # remove chalk block
        global_clean_list = global_clean_list[1:]

        
        for i in global_clean_list:
            if i[0] == "author":
                self.author_list.append(i[2])
            else:
                self.global_document_dict[i[0]] = i[2]

    
    
    def source_clean(self):
        source_clean_list: list = []
        for i in self.source_content:
            tup = i.partition(" = ")
            self.check_object.source_check(tup)
            source_clean_list.append(tup)


    def imports_clean(self):
        imports_clean_list: list = []
        for i in self.imports_content:
            tup = i.partition(" = ")
            self.check_object.imports_check(tup)
            imports_clean_list.append(tup)

        imports_clean_list = imports_clean_list[1:]

        for i in imports_clean_list:
            self.imports_dict[i[0]] = i[2]
        


    def problem_clean(self):
        problem_clean_list: list = []
        var_clean_list: list = []
        for i in self.problem_contents:
            tup = i.partition(" = ")
            self.check_object.problem_check(tup)
            problem_clean_list.append(tup)

        problem_clean_list = problem_clean_list[1:]
        problem_clean_list = problem_clean_list[:len(problem_clean_list)-1]

        vars_start_index = 0
        problem_start_index = 0
        media_start_index = 0

        problem_header_section_list: list = []
        vars_section_list: list = []
        problem_section_list: list = []
        media_section_list: list = []
        
        

        for i in problem_clean_list:
            if i[0] == "[VARS]":
                vars_start_index = problem_clean_list.index(i)

            elif i[0] == "[PROBLEM]":
                problem_start_index = problem_clean_list.index(i)

            elif i[0] == "[MEDIA]":
                media_start_index = problem_clean_list.index(i)

        problem_header_section_list = problem_clean_list[0:vars_start_index]
        vars_section_list = problem_clean_list[vars_start_index+1:problem_start_index]
        problem_section_list = problem_clean_list[problem_start_index+1:media_start_index]
        media_section_list = problem_clean_list[media_start_index+1:]



       

        for i in problem_header_section_list:
            self.check_object.problem_header_section_checker(i[0])
            self.problem_dict[i[0]] = i[2]


        for i in vars_section_list:
            self.check_object.vars_Section_checker(i[0])
            self.vars_dict[i[0]] = i[2]


        for i in problem_section_list:
            self.check_object.problem_section_checker(i[0])
            self.problem_dict[i[0]] = i[2]


        for i in media_section_list:
            self.check_object.media_section_checker(i[0])
            self.media_dict[i[0]] = i[2]


        

        

        



        

        

