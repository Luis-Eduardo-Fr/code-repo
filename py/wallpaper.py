import time
import subprocess
import random
b_time = 1200

# Iniciar o primeiro papel de parede
while True:
    # Cria uma lista de números de 1 a 26 
    numbers = list(range(1, 27))

    # Usamos o random para embaralhar essa lista
    random.shuffle(numbers)

    for a in numbers:
        if a == 7 and a == 9 and a == 15 and a == 23:
            continue
        way = "/home/lefds/Pictures/at{}.jpeg".format(a)
        
        # Iniciar o próximo papel de parede
        swaybg_process = subprocess.Popen(["swaybg", "--output=*", "--image", way, "-m", "fill"])
        
        # Esperar antes de passar para o próximo papel de parede
        time.sleep(b_time)

        # Finalizar o processo swaybg anterior
        swaybg_process.terminate()
 

