import numpy as np
alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
encodeInput = input("Please insert your 3x3 encoding matrix in form (a b c; d e f; g h i):")
encodeMatrix = np.matrix(encodeInput)
dMessage = input("Enter your message (letters and spaces only): ")
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
shortLength = len(encoded)/3+1
# Only supports 12 characters right now, fix in the future
encoded[0] = [encoded[0],encoded[3],encoded[6],encoded[9]]
encoded[1] = [encoded[1],encoded[4],encoded[7],encoded[10]]
encoded[2] = [encoded[2],encoded[5],encoded[8],encoded[11]]
del(encoded[3:])
encoded = np.matrix(encoded)
final = encodeMatrix * encoded
final = final%27
#final = []
# for i in range(len(encoded)):
  # final[i] = encodeMatrix[i]*encoded[i][i]
  # print(final)
# Modulus 27 so you'll get a real letter
# for i in range(len(final)):
  # final[i]=int(final[i])%27
# for i in range(int(shortLength)):
  # encoded.insert(4*i,";")
# encoded.pop(0)
# encoded.pop(len(encoded)-1)
print("Your original matrix:\n",encoded)
print("Your encoded matrix:\n",final)
message = []
final = final.tolist()
#This part also needs more flexibility
for i in range(len(final)):
  message.append(alphabet[final[i][0]])
for i in range(len(final)):
  message.append(alphabet[final[i][1]])
for i in range(len(final)):
  message.append(alphabet[final[i][2]])
for i in range(len(final)):
  message.append(alphabet[final[i][2]])
print("Your final encoded message is:","".join(message))
