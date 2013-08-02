import re
import os

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

root = tk.Tk()
root.withdraw()

file_path = tk.askopenfilename(filetypes=[('text files', '.txt'),('all files', '.*')])

file = open(file_path)
outfile = open(str(os.getcwd())+'/CPDout.txt','w')

if file:
    print( "File ", file, " opened succesfully")
else:
    print ("File could not be opened!")
    exit(0)
    
root = tk.Tk()
root.withdraw()

URL_list=[]
count=0

while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        if "a href" and "jpg" in line:
            m=re.search('href(.+?)class',line)
            if m:
                result=m.group(1)
                result2=result[2:-3]
                print (result2)
                outfile.write(str(result2)+'\n')


outfile.close()
    
