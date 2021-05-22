from tqdm import tqdm
from time import sleep

for i in tqdm(range(0,100),desc="Loading : "):
    sleep(0.1)

for i in tqdm(range(0,100),desc="Loading : ",ascii="123456789$"):
    sleep(0.1)

