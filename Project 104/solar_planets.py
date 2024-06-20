import cv2

#read image
img = cv2.imread('solar-system.jpg')

#Adding text for planets
#Sun
cv2.putText(img,
            "Sun",
            (100,90),
            cv2.FONT_HERSHEY_COMPLEX,
            1.5,
            (0,0,255)
            )

#Mercury
cv2.putText(img,
            "Mercury",
            (110,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

#Venus
cv2.putText(img,
            "Venus",
            (190,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

#Earth
cv2.putText(img,
            "Earth",
            (280,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

#Mars
cv2.putText(img,
            "Mars",
            (380,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

#Jupiter
cv2.putText(img,
            "Jupiter",
            (480,80),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

#Saturn
cv2.putText(img,
            "Saturn",
            (780,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

#Uranus
cv2.putText(img,
            "Uranus",
            (965,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

#Neptune
cv2.putText(img,
            "Neptune",
            (1110,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

#Display Image
cv2.imshow('Solar PLanets',img)

cv2.waitKey(0)

#Saving Final Image
cv2.imwrite('solar_system_with_name.jpg',img)