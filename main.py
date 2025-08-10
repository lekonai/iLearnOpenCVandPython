import cv2
import os

# this first part is just learning some python shit. 
# it'll have basically no purpose the moment that 
# so you can't declare? only assign... a bit annoying

### initial directory read, will not be necessary after implementation / the addition of a web frontend ###
print("Please select the image you want:")
imgLi = os.listdir('images/')

fileNamesD = {
    0 : "placeholder"
}
count = 0
for i in imgLi:
    count += 1
    fileNamesD.update({count : f"{i}"})

for j in fileNamesD:
    print(f"{j} : {fileNamesD[j]}") if j > 0 else None
    

### important functions and subroutines ###
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

def messingAbout():
    # i need to make some space and put all the real shit in .. the actual flow control
    h, w = image.shape[:2]
    print(f"Height = {h}, Width = {w}")

    Blue, Green, Red = image[h - 20, w - 20]
    print(f"The colour values at the pixel [{h - 20}, {w - 20}], are\nR = {Red}\nG = {Green}\nB = {Blue}")
    cv2.imshow("Pixel!", image[h - 20, w - 20])
    cv2.waitKey(0)
    print("")
    roi = image[0 : int(h / 2), 0 : int(w / 2)] # im no sure which is height and width. im gonna assume its h and w, also because everything is alphabetical, and also because i had assigned h and w before in this same manner
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)

def mostHighColoured():
    # before i get to OCR, which i know will stump me, i want to make a quick and very very slow algorithm to find the highest R, G and B values
    # the purpose of this subroutine is to extract the pixels of highest RGB and then display them in context. this will be forming images and such
    print("Finding Highest RGB Values...")
    tHeight, tWidth = image.shape[:2]
    # i have no ideas of how to optimise this better at the moment, i guess this could be deployed differently depending on colour depth or what type of image it is
    # hstR, hstG, hstB = 0, 0, 0 # declaration / assignment of VALUES
    # hstRC, hstGC, hstBC = [0, 0], [0, 0], [0, 0] # declaration / assignment of COORDS
    # im going to see if i can refactor this into a dictionary. damn this is big though
    highestColours = {
        "HstR" : [-1, 0, 0],
        "HstG" : [-1, 0, 0], # highest value and then the coords
        "HstB" : [-1, 0, 0]
    }
    # hst = highest
    # cur = current (in examination)
    for hCur in range (0, tHeight): 
        for wCur in range (0, tWidth):
            bCur, gCur, rCur = image[hCur, wCur]
            # print(f"current pixel: {hCur}, {wCur}") # for debug purposes
            # okay so this ensures that everything's scoured through!
            if rCur > highestColours["HstR"][0]:
                print("A New Highest Red Found!")
                highestColours["HstR"][0] = rCur
                highestColours["HstR"][1] = hCur
                highestColours["HstR"][2] = wCur
            
            if gCur > highestColours["HstG"][0]:
                print("A New Highest Green Found!")
                highestColours["HstG"][0] = gCur
                highestColours["HstG"][1] = hCur
                highestColours["HstG"][2] = wCur

            if bCur > highestColours["HstB"][0]:
                print("A New Highest Blue Found!")
                highestColours["HstB"][0] = bCur
                highestColours["HstB"][1] = hCur
                highestColours["HstB"][2] = wCur
    # im not really sure how this works with BW imagery lol
    print(f"Highest Red Value is {highestColours["HstR"][0]}, which can be found at pixel: {highestColours["HstR"][1]}, {highestColours["HstR"][0]}\nHighest Green Value is {highestColours["HstG"][0]}, which can be found at pixel: {highestColours["HstG"][1]}, {highestColours["HstG"][2]}\nHighest Blue Value is {highestColours["HstB"][0]}, which can be found at: {highestColours["HstB"][1]}, {highestColours["HstB"][2]}")
            
            



### main main ###
num = selection()

pathA = f'images/{fileNamesD[num]}'
image = cv2.imread(pathA) 

decision = input("Would you like to see the image you selected? Y/N \n")
decision = True if decision.lower() == "y" else False
if decision == True:
    cv2.imshow("Selected image", image)
    cv2.waitKey(0)

# messingAbout()
mostHighColoured()


# print(cv2.imread(pathA, 0))
# this is gonna be noted because it isn't particularly effective for massive imagery. plus idk what the purpose of the 0 is here, and vsc isn't helping, lowkey.