import cv2
import os

# this first part is just learning some python shit. 
# it'll have basically no purpose the moment that 
print("Please select the image you want:")
imgLi = os.listdir('images/')
# so you can't declare? only assign... a bit annoying
fileNamesD = {
    0 : "placeholder"
}
count = 0
for i in imgLi:
    count += 1
    fileNamesD.update({count : f"{i}"})

for j in fileNamesD:
    print(f"{j} : {fileNamesD[j]}") if j > 0 else None
    
def selection():
    valid = False
    while not valid:
        nInp = input("Enter the number of which you'd like to select: ")
        try:
            nInp_int = int(nInp)
            if nInp_int in fileNamesD:
                valid = True
                return nInp_int
            else:
                print("Not in the list!")
        except ValueError:
            print("Not valid")

num = selection()

pathA = f'images/{fileNamesD[num]}'
image = cv2.imread(pathA) 

h, w = image.shape[:2]

print(f"Height = {h}, Width = {w}")
# print(cv2.imread(pathA, 0))
# this is gonna be noted because it isn't particularly effective for massive imagery. plus idk what the purpose of the 0 is here, and vsc isn't helping, lowkey.