
class Draw():
    def __init__(self, file_handle: str, *args):
        arguments = locals()['args']
        for i in arguments:
            print(i)





if __name__ == "__main__":
    x = Draw("chalk.draw", 5, "yes", "no")