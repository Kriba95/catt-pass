import tkinter as tk
import subprocess


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)


        self.prompt = tk.Label(self, text="Enter YouTube URL:", anchor="w")
        self.prompter = tk.Label(self, text="Skip video Chromecast", anchor="w")
        self.promptere = tk.Label(self, text="cmd Command", anchor="w")

        self.entry = tk.Entry(self)
        self.entryr = tk.Entry(self)

        self.submit = tk.Button(self, text="Search Video", command=self.cast)
        self.skipper = tk.Button(self, text="Skip video", command=self.skip)
        self.submitcmd = tk.Button(self, text="CMD command", command=self.cmd)
        self.output = tk.Label(self, text=" ")
        # lay the widgets out on the screen.
        self.prompt.grid(row=1,column=1) 
        self.entry.grid(row=2,column=1) 
        self.submit.grid(row=3,column=1) 
        self.output.grid(row=4,column=1) 

        self.prompter.grid(row=8,column=1) 
        self.skipper.grid(row=9,column=1) 
        
        self.promptere.grid(row=10,column=1) 
        self.entryr.grid(row=11,column=1)
        self.submitcmd.grid(row=12,column=1)  

    def cast(self):
        
        data = self.entry.get()

        cmd = "catt cast " + data
        print(cmd)
# returns output as byte string
        returned_output = subprocess.check_output(cmd)
        print(returned_output)

    def skip(self):
        data = self.entry.get()
        cmd = "catt skip"
        returned_output = subprocess.check_output(cmd)
        print(returned_output)
    
    def cmd(self):
        data = self.entryr.get()
        print(data)

        returned_output = subprocess.check_output(data)
        print(returned_output)



if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
