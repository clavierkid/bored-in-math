#!/usr/local/bin/python3
import numpy as np
import numpy.linalg
import math
alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

mode = input("Encode or decode? (e/d)")
if mode.lower() == "e":
  decode = False
elif mode.lower() == "d":
  decode = True
else:
  print("you done messed up")
  exit()

#Other sizes would also be nice
print("[a b c\nd e f\ng h i]")
encodeInput = input("Please insert your 3x3 encoding matrix in form (a b c; d e f; g h i):")
encodeMatrix = np.matrix(encodeInput)
decodeMatrix = numpy.linalg.inv(encodeMatrix)
print("inverse matrix:\n",decodeMatrix)

if decode == False:
  dMessage = input("Enter your plaintext message (letters and spaces only): ")
elif decode == True:
  dMessage = input("Enter your encoded text: ")
dMessage = dMessage.lower()
encoded = []
for i in range(len(dMessage)):
  encoded.append(alphabet.index(dMessage[i]))

length = len(dMessage)-1
if length%3 == 1:
  encoded.append(0)
elif length%3 == 2:
  encoded.append(0)
  encoded.append(0)

encoded[0] = [encoded[0],encoded[3]]
encoded[1] = [encoded[1],encoded[4]]
encoded[2] = [encoded[2],encoded[5]] 
shortLength = int(len(encoded)/3)
steps = 0
for i in range(1,shortLength-1):
  steps = steps + 1
  encoded[0].append(encoded[3*i+3])
  encoded[1].append(encoded[3*i+4])
  encoded[2].append(encoded[3*i+5])
del(encoded[3:])

encoded = np.matrix(encoded)
if decode == True:
  final = decodeMatrix * encoded
elif decode == False:
  final = encodeMatrix * encoded
final = final%27

print("Your original matrix:\n",encoded)
if decode == True:
  print("Your decoded matrix:\n",final)
elif decode == False:
  print("Your encoded matrix:\n", final)

message = []
final = final.tolist()

for j in range(len(final[0])):
  for i in range(len(final)):
    print(i,j,final[i][j],message,"\n")
    final[i][j] = round(final[i][j])
    message.append(alphabet[final[i][j]])

if decode == True:
  print("Your final decoded message is:","".join(message))
elif decode == False:
  print("Your final encoded message is:","".join(message))
