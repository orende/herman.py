# -*- coding: UTF-8 -*-
import hashlib

string = 'Fin dag idag, inte sant?'
a = sorted(list(string.upper().replace(' ','',2).replace('?','').replace('',',')))
newString = ''.join(reversed(a))
print hashlib.sha1(newString).hexdigest()

# Gör om strängen till gemener, plocka ut alla unika bokstäver (ta bort andra tecken), sortera dem i bokstavsordning, skapa en sha1-hash av resultatet
# Det finns ett antal buggar i koden...
# Svaret bör bli: 30865f4524d36c7c848a2f81263a834c3e560bcc
