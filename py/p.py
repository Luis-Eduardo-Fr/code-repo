import platform
import time

if platform.system() == 'Linux':
    print("Parece que está utilizando Linux, você é chad!")
elif platform.system() == 'Windows':
    print("Parece que você está utilizando Windows, você você é sub-chad!")
else:
    print("Seu sistema não é suportado.")

print("Carregando", end = '')
for _ in range(3):
    time.sleep(0.5)
    print('.', end = '', flush = True)
    time.sleep(0.5)
print("Found!")
