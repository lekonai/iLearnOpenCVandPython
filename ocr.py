# i had made such a mess of the original code that im not sure i want to continue
# but i enjoyed what i did and i learnt a lot, so i think ive suitable knowledge to just jump into it. this will start soon
import os
import cv2

imgLi = os.listdir('static/images/text/')

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
path = f'static/images/text/{fileNamesD[num]}'
# this is code copied from my other script file
# this is at the moment a tutorial. script wise this is a very very simple implementation it seems as the library does practically everything for you lol
# i love this damn library

curImage = cv2.imread(path)

textDetectorDB50 = cv2.dnn_TextDetectionModel_DB('static/DB50.onnx') # why is opencv's docs so bad?
# .setBinaryThreshold
# .setPolygonThreshold
# .setInputParams 

# setInputParams(scale, inputSize, mean, swapRB) – Preprocessing parameters:
#     scale – Scaling factor for image normalization (e.g., 1.0).
#     inputSize – Input size expected by the model (e.g., (320, 320)).
#     mean – Mean values for normalization (e.g., (123.68, 116.78, 103.94)).
#     swapRB – Boolean flag for swapping red and blue channels (usually True for OpenCV).

# boxes, confidences = textDetectorDB50.detect(image) is some sorta detection

testimage = curImage.copy()

conf = 0.8 # confidence
nmst = 0.4 # idk what this is?
bint = 0.3 # binary threshold
polyt = 0.5 # polygon threshold
mean = (122.67891434, 116.66876762, 104.00698793) # im not sure what this is meant to be ?? lol
h, w = curImage.shape[:2]
print(f"{h}, {w}")
textDetectorDB50.setBinaryThreshold(bint).setPolygonThreshold(polyt)
textDetectorDB50.setInputParams(1.0/255, (h, w), mean, True)

boxes, _ = textDetectorDB50.detect(testimage)

cv2.imshow("original", curImage)
cv2.imshow("annotated", testimage)
cv2.waitKey(0)
cv2.destroyAllWindows