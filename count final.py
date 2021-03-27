import cv2
cap=cv2.VideoCapture('C:/Users/gegvf/Downloads/20201230123300.mp4')
car_cascade=cv2.CascadeClassifier('C:/Users/gegvf/Desktop/New folder/Car-Detection-Basic-Open-CV-master/carx.xml')

count=0


while(True):
    ret,frame=cap.read()
    
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    height,width,_=frame.shape
    frame[0:50,0:width]=(255,255,255)
    cv2.putText(frame,'count=',(40,40), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)


    #print(height,width)
    
    cars=car_cascade.detectMultiScale(grey,1.1,1)
    
    cv2.line(frame,(0,height-600),(width,height-600),(255,255,0),5)
   
  
    for(x,y,w,h) in cars:
        
        car_cnt=int(y + h/2)
        cnt_line=height-400
        
        if(car_cnt<cnt_line+10 and car_cnt>cnt_line-10):
           
            count=count+1
            
            print(count)
        
        
        
        cv2.rectangle(frame,(x,y),(x+w-8,y+h-8),(244,244,0),3)
        cv2.putText(frame,'car',(x,y-10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
        cv2.putText(frame,str(count),(300,45), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
    


    cv2.imshow('frame',frame)
    
    
    key=cv2.waitKey(30)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()