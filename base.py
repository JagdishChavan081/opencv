import cv2

#how to read,write, show images in open cv2

img=cv2.imread('data/lena.jpg',-1)

cv2.imshow('image',img)
k=cv2.waitKey(0)


if k == 27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    #write an image in the form a file
    cv2.imwrite('copy_image/lena_copy.png',img)
    cv2.destroyAllWindows()

