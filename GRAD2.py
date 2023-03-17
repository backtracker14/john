import wpf
import subprocess
import os

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'GRAD2.xaml')
        self.micOn = self.FindName("micOn")
        
        
    def btn1_Click(self, sender, e):
        subprocess.call(["python", "script1.py"])
        pass

    def btn2_Click(self, sender, e):
        subprocess.call(["python", "script2.py"])
        pass

if __name__ == '__main__':
    Application().Run(MyWindow())
