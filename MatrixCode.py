import numpy as np

alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#Other sizes would also be nice
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

# print("Before:",encoded)
encoded[0] = [encoded[0],encoded[3]]
encoded[1] = [encoded[1],encoded[4]]
encoded[2] = [encoded[2],encoded[5]] 
shortLength = int(len(encoded)/3)
steps = 0
# print("\n\nMiddle:",encoded)
for i in range(1,shortLength-1):
  steps = steps + 1
  encoded[0].append(encoded[3*i+3])
  encoded[1].append(encoded[3*i+4])
  encoded[2].append(encoded[3*i+5])
del(encoded[3:])

# print("\n\nAfter:",encoded)
encoded = np.matrix(encoded)
final = encodeMatrix * encoded
final = final%27

print("Your original matrix:\n",encoded)
print("Your encoded matrix:\n",final)

message = []
final = final.tolist()

for j in range(len(final[0])):
  for i in range(len(final)):
    message.append(alphabet[final[i][j]])

print("Your final encoded message is:","".join(message))
