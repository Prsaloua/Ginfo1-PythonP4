# Ginfo1-PythonP4
## Python Class Project Number 4
### VERSION OF SAMIA TOURRIZ

- [x] Code of  **Progress Bar**
- [x] Code of **Searching in PDF and progreess bar together**
- [ ] Code of **searching in pdf** 


:battery: :battery: :battery:
__HERE PROGRESS BAR CODE__
:battery: :battery: :battery:
```python
from tqdm import tqdm
from time import sleep

for i in tqdm(range(0,100),desc="Loading : "):
    sleep(0.1)

for i in tqdm(range(0,100),desc="Loading : ",ascii="123456789♦"):
    sleep(0.1)
```

SOLUTION searched with @techmouhib 

:closed_book: :battery: :page_with_curl:
__HERE pdf search code & Progress BAR__
:closed_book::battery: :page_with_curl:

```python
from tqdm import tqdm
from time import sleep
import PyPDF2
import re

def progress(bar):
    for i in tqdm(bar, desc = "loading : ",ascii="123456789$"):
        sleep(.6)

print("\n")
print("[IMPORTANT] Place your pfd file in the same folder where the program is !!!! ")
print("\n")
Fname = input("Enter your file name in this format [file-name.pdf], \nOr use the default PDF named [cours.pdf] : ")

q = 'q'
for i in tqdm(range(0,100), desc = "loading : ",ascii="123456789$"):
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
                progress(pfile)

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

#### Hope you enjoy our journey with that project
