import cv2

img = cv2.imread("solar-system.jpg") 
cv2.putText(img, "Sol", (100,80),
 cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255) )

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Mercúrio",
            (100,40),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Vênus",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Terra",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Marte",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )
cv2.putText(img,
            "Júpiter",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Saturno",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Urano ",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Netuno",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.imshow("Resultado",img) 
cv2.waitKey(0) 
cv2.imwrite("Solar_systemwithname.jpg",img)