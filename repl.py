class Repl:
    
    chars = 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    prompt = '<repl>'
    
    def __init__(self):
        #self.commands = []
        self.text = str()
        self.stop = False

    def Read(self):
        """
        Read function
        """
        self.text = input(self.prompt)
        #print(self.text)
        if self.text == '':
            return 'empty', ''
        for i in range(len(self.text)):
            if self.text[i] not in self.chars:
                cmd, arg = self.text[:i], self.text[i:].split()
                break
            elif i == len(self.text)-1:
                cmd, arg = self.text, None
        #self.commands.append((cmd,arg))
        return cmd, arg

    def Eval_empty(self, *arg):
    	pass

    #def Print(self, out):
    #    print(out)

    def Eval_exit(self, *arg):
        self.stop = True

    def Eval_help(self, arg):
        out = "git gud"
        print(out)

    def Eval_foo(self, arg):
        print("bar" + " arg= ")
        if arg:
            arg = ''.join(arg)
        print(arg)

def run(prompt):
    while prompt.stop == False:
        command, arg = prompt.Read()
        getattr(prompt, 'Eval_' + command)(arg)

if __name__ == "__main__":
    prompt = Repl()
    run(prompt)