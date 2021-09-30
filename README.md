# Word Mutator
A python app to generate permutation on words with a suffix and prefix if needed. 

## Description

This was made for an easy way to generate permutated words with or without a prefix or suffix. Great for making brute force lists! 

## Install

Copy the file locally (copy and paste) 

or

```
git clone https://github.com/AssassinUKG/Word_Mutator.git
cd word_Mutator
python3 wordPermutator.py -w word
```

## Usage

```
./wordPremutator.py -w test
```

Produces

```
test
tets
tset
<SNIP>
tste
tset
```

```
./wordPremutator.py -w 0123 -p WIFI1-
```

Produces

```
WIFI1-0123
WIFI1-0132
WIFI1-0312
<SNIP>
WIFI1-3201
WIFI1-3210
```

```
./wordPremutator.py -w 1234 -p WIFI1- -s -NONE
```

Produces

```
WIFI1-1234NONE
WIFI1-1243NONE
WIFI1-1324NONE
WIFI1-1342NONE
<SNIP>
WIFI1-3412NONE
WIFI1-3421NONE
WIFI1-4123NONE
WIFI1-4132NONE
WIFI1-4213NONE
WIFI1-4231NONE
WIFI1-4312NONE
WIFI1-4321NONE
```
