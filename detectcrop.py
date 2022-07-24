import cv2
i_no = str(2)

# image = cv2.imread('./doc-data/ocr_images/train/train' + i_no + '.bmp') 
# image = cv2.imread('./doc-data/ocr_images/eval/eval' + i_no + '.bmp') 
image = cv2.imread('./doc-data/ocr_images/test/testex' + i_no + '.bmp') 

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(image, 10, 250) 
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
idx = 0 
for c in cnts: 
	x,y,w,h = cv2.boundingRect(c) 
	if w>5 and h>50: 
		idx+=1 
		new_img=image[y:y+h,x:x+w] 
		# cv2.imwrite('./doc-data/ocr_images/train/' + i_no + '_train/' + str(idx) + '.png', new_img) 
		# cv2.imwrite('./doc-data/ocr_images/eval/' + i_no + '_eval/' + str(idx) + '.png', new_img) 
		cv2.imwrite('./doc-data/ocr_images/test/' + i_no + '_testex/' + str(idx) + '.png', new_img) 
