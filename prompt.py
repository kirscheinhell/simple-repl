import repl

class prompt(repl.Repl):

    def __init__(self):
        super(prompt,self).__init__()
    
    def Eval_test(self, *arg):
        print("Test passed")
    
    def Eval_editor(self, arg):
        import editor
        editor.main(arg[0])

command = prompt()
repl.run(command)