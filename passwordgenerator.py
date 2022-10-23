import sys
import wordlist
from termcolor import colored

try:
    sayı1 = sys.argv[1]
    sayı2 = sys.argv[2]
    kelime = sys.argv[3]
    dosyaİsmi = sys.argv[4]
    sayı1 = int(sayı1)
    sayı2 = int(sayı2)
    
    generator = wordlist.Generator(kelime)
    wordlistYaz = open(dosyaİsmi , "a", encoding="utf-8")
    
    index = 0
    for i in generator.generate(sayı1,sayı2):
        index += 1
        wordlistYaz.write(i)
        wordlistYaz.write("\n")
        print(colored(f"\r-*^*-> {i}", "green"), end="")
    print(colored(f"\nToplam {index} kombinasyon hesaplandı ve yazıldı...", "green"))
    wordlistYaz.close()
    
except KeyboardInterrupt:
    print(colored(f"\nElle durduruldu!", "blue"))
    print(colored(f"Toplam {index} kombinasyon hesaplandı ve yazıldı...", "blue"))
    exit(0)
    
except IndexError:
    print(colored("Program use: python wordlistgenerator.py <min> <max> <string> fileName.txt", "red"))
    exit(0)
    
except ValueError:
    print(colored("Program use: python wordlistgenerator.py <min> <max> <string> fileName.txt", "red"))
    exit(0)  