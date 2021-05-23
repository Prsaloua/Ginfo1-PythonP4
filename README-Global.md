# Ginfo1-PythonP4
## Python Class Project Number 4
### VERSION MOUHIB OTMAN
#### Hope you enjoy our journey with that project





:battery: ##Progress bar
```python

from tqdm import tqdm
from time import sleep

def progress(bar):
    for i in tqdm(bar, desc = "loading : ",ascii="123456789$"):
        sleep(.6)

```


▪️ ▫️ ◾ ◽ ◼️ ◻️  ##PDf Search
```python

import PyPDF2
import re


print("\n")
print("[IMPORTANT] Place your pfd file in the same folder where the program is !!!! ")
print("\n")
Fname = input("Enter your file name in this format [file-name.pdf], \nOr use the default PDF named [cours.pdf] : ")

q = 'q'

while q != 'n' and q != 'N':

    file = PyPDF2.PdfFileReader(Fname)
    pages = file.getNumPages()
    word = input("\nenter the word you are looking for : ")
    c = 0
    pageList = []
    for i in range(0, int(pages)):
        pfile = file.getPage(i)
        text = pfile.extractText()
        look = re.search(word, text)
        if look != None:
            print(f"\nWord Found in Page : {i+1} ")
            c += 1
            pageList.append(i)
            print("\n")
            //progress(pfile) //uncoment this only when you include the progress bar function in this code
            print("\n")
    if c >= 1 :
        for i in range (len(pageList)):
            pageList[i] = pageList[i]+1

        print(f"[SUMMARY] : Word Found in {len(pageList)} Pages")


        print("\n")
        print(f"[SUMMARY] : Page Numbers : {pageList}")
        print("\n")
        q = input("Want To Run Program Again ? [Y/N] : ")
    else:
        print("Word Not Found !!")
        print("[ERROR] : please try another Word")
        q = input("Want To Run Program Again ? [Y/N] : ")




print("END OF PROGRAM")
```


#### Hope that was helpfull


