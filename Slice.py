import cv2 as cv 
#from google.colab.patches import cv2_imshow # for image display

vidcap = cv.VideoCapture('/Users/benz/Downloads/Video Slicing/IMG_6572.MOV')
success,image = vidcap.read()
count = 0
pic = 1
while success:
    if count%10 == 0:
      cv.imwrite("/Users/benz/Downloads/Video Slicing/Output Picture/มืด_เปิดไฟ/%d.jpg" % pic, image) 
      print('Read a new frame :', str(success) + ' : at','frame ' + str(count)+ ' | pic : '+str(pic))
      count += 1
      pic += 1
      success,image = vidcap.read()
    else:
      count += 1
      success,image = vidcap.read()

print("success")

vidcap.release()