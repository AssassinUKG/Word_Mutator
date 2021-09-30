import itertools
import argparse

# Created by Ricahrd Jones
# 00:17 1st Oct 2021
# To create fast permutated words on a given word (with or without prefix and suffix)

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--word", help="The word to permutate", required=True)
parser.add_argument("-p", "--prefix", help="A Prefix for your word list. Eg: prefixword")
parser.add_argument("-s", "--suffix", help="A Suffix for your word list. Eg: wordsuffix")
args = parser.parse_args()


def permutations(word, prefix=None, suffix=None):
    retList = []
    letters = [i for i in word]
    for v in itertools.permutations(letters, len(letters)):     
        current_permutation = "".join(v)
        if (suffix and prefix):
            retList.append(f"{prefix}{current_permutation}{suffix}")
            continue
        elif (prefix):
            retList.append(f"{prefix}{current_permutation}")
        elif (suffix):
            retList.append(f"{current_permutation}{suffix}")
        else:
            retList.append(current_permutation)        
    return retList


def main():
  
    for word in permutations(args.word, args.prefix, args.suffix):
        print(word)

if __name__=="__main__":
    main()
