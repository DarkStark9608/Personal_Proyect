import time 
from tqdm import tqdm

print("Iniciando barra de progreso")

for i in tqdm(range(1000)):
    time.sleep(0.01)