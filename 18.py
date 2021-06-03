import string
word = ["hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"]

chan = {}

cInWords = {}

for letter in string.ascii_lowercase:
    chan[letter] = cInWords[letter] = 0

ovLen = 0
for word in words:
    ovLen += len(word)
    for char in word:
        cInWords[char] += 1

for char in cInWords:
    chan[char] = cInWords[char] / ovLen

word = input()

pChan = chan[word[0]]
if pChan == 0:
    print('First character is unknown')
    exit()

pr_chan = pChan

for i in range(1, len(word)):

    if chan[word[i]] == 0.0:

        if prev_chance == 0.0:

            print("Error: char on ",i," position is unknown!")
            exit()

        else:
            pChan *= pr_chan
    
    else:
        pChan *= chan[word[i]]
        pr_chan = prChan

print(pChan)