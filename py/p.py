import platform

if platform.system() == 'Linux':
    print("Parece que está utilizando Linux, você é chad!")
elif platform.system() == 'Windows':
    print("Parece que você está utilizando Windows, você você é sub-chad!")
else:
    print("Seu sistema não é suportado.")
