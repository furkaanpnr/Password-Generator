import sys
import wordlist
from termcolor import colored

try:
    number1 = sys.argv[1]
    number2 = sys.argv[2]
    letters = sys.argv[3]
    fileName = sys.argv[4]
    number1 = int(number1)
    number2 = int(number2)
    
    generator = wordlist.Generator(letters)
    wordlistWrite = open(fileName , "a", encoding="utf-8")
    
    index = 0
    for i in generator.generate(number1,number2):
        index += 1
        wordlistWrite.write(i)
        wordlistWrite.write("\n")
        print(colored(f"\r-*^*-> {i}", "green"), end="")
    print(colored(f"\nA total of {index} combinations were calculated and written...", "green"))
    wordlistWrite.close()
    
except KeyboardInterrupt:
    print(colored(f"\nManually Stopped!", "blue"))
    print(colored(f"A total of {index} combinations were calculated and written...", "blue"))
    exit(0)
    
except IndexError:
    print(colored("Program usage: python wordlistgenerator.py <min> <max> <string> fileName.txt", "red"))
    exit(0)
    
except ValueError:
    print(colored("Program usage: python wordlistgenerator.py <min> <max> <string> fileName.txt", "red"))
    exit(0)  