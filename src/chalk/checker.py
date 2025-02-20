"""The checker modules checks for syntax and semantic errors within the Chalk File."""
from exceptions import HeaderError, GlobalError, SourceError, ImportsError, ProblemError

class Checker():
    def __init__(self, global_document_content: list, source_content: list, imports_content: list, problem_contents: list):
        self.global_document_content: list = global_document_content
        self.source_content: list = source_content
        self.imports_content: list = imports_content
        self.problem_contents: list = problem_contents
        

        # counters
        self.global_name_counter: int = 0
        self.collection_counter: int = 0
        self.license_counter: int = 0
        self.creation_date_counter: int = 0

        self.id_counter: int = 0
        self.begin_counter: int = 0
        self.end_counter: int = 0

        self.problem_name_counter: int = 0
        self.desc_counter: int = 0
        self.hint_counter: int = 0
        self.sample_counter: int = 0
        self.question_counter: int = 0
        self.equation_counter: int = 0
        self.answer_counter: int = 0
        self.png_counter: int = 0
        self.jpeg_counter: int = 0
        self.svg_counter: int = 0
        self.draw_counter: int = 0


        


    def clean_check(self):
        pass


    def precheck(self, file_contents: list):
        """Basic file checking"""
        if '[CHALK]' not in file_contents:
            raise HeaderError("Need a Chalk header")
        
        chalk_count = file_contents.count('[CHALK]')
        
        if chalk_count > 1:
            raise HeaderError(f"You may have only one [CHALK] per Chalk file. You have {chalk_count} [CHALK] Blocks.")
        
        if file_contents[0] != '[CHALK]':
        
            if file_contents[0] == 'CHALK':
                raise HeaderError("You need brackets around CHALK.")
        
            if file_contents[0] == '[Chalk]':
                raise HeaderError("You need to capitalize all the letters in CHALK.")
        
            if file_contents[0] == '[chalk]':
                raise HeaderError("You need to capitalize all the letters in CHALK.")
            

    def global_check(self, tup: tuple):
        # Name Checker
        for i in tup:
            if i == 'name':
                self.global_name_counter += 1

            if self.global_name_counter > 1:
                raise GlobalError("You may only have one global name.")
            
            if i == 'collection':
                self.collection_counter += 1

            if self.collection_counter > 1:
                raise GlobalError("You may only have one collection label per chalk file.")
            
            if i == 'license':
                self.license_counter += 1

            if self.license_counter > 1:
                raise GlobalError("You may only have one License per Chalk file.")
            
            if i == 'creation_date':
                self.creation_date_counter += 1

            if self.creation_date_counter > 1:
                raise GlobalError("You may only have one Creation Date per Chalk file.")
            
    def source_check(self, tup: tuple):
        for i in tup:
            if i == 'yes':
                pass

    def imports_check(self, tup: tuple):
        pass

    def problem_check(self, tup: tuple):
        

        for i in tup:
            if i == "[BEGIN]":
                self.begin_counter += 1


            if i == "[END]":
                self.end_counter += 1
            
            

        

            
        if self.begin_counter > 1:
            raise ProblemError("You my only have one [BEGIN] block per Problem.")
        else:
            pass
        
        
        if self.end_counter > 1:
            raise ProblemError("You may only have one [END] block per Problem.")
        else:
            pass

    def problem_header_section_checker(self, key):
        if key == "name":
            self.problem_name_counter += 1

        if self.problem_name_counter > 1:
            raise ProblemError("You may only have one name per problem section.")
        
        if key == "desc":
            self.desc_counter += 1

        if self.desc_counter > 1:
            raise ProblemError("You may have only one description per problem.")
        
        if key == "hint":
            self.hint_counter += 1

        if self.hint_counter > 1:
            raise ProblemError("You may have only one hint per problem.")
        

    def vars_Section_checker(self, key):
        pass

    def problem_section_checker(self, key):
        if key == "sample":
            self.sample_counter += 1

        if self.sample_counter > 1:
            raise ProblemError("You may only have one sample per problem.")
        
        if key == "question":
            self.question_counter += 1

        if self.question_counter > 1:
            raise ProblemError("You may only have one question per problem.")
        
        if key == "equation":
            self.equation_counter += 1

        if self.equation_counter > 1:
            raise ProblemError("You may only have one equation per problem.")
        
        if key == "answer":
            self.answer_counter += 1
        
        if self.answer_counter > 1:
            raise ProblemError("You may only have one answer per problem.")

    def media_section_checker(self, key):
        if key == "png":
            self.png_counter += 1

        if self.png_counter > 1:
            raise ProblemError("You may only have one png per problem.")
        
        if key == "jpeg":
            self.jpeg_counter += 1
        
        if self.jpeg_counter > 1:
            raise ProblemError("You may only have one Jpeg per problem.")
        
        if key == "svg":
            self.svg_counter += 1

        if self.svg_counter > 1:
            raise ProblemError("You may only have one svg per problem.")
        
        if key == "draw":
            self.draw_counter += 1

        if self.draw_counter > 1:
            raise ProblemError("You may only have one draw function per problem.")
            
            

            
            

            
            
        
        
