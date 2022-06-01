"""
count = 0
#n = st.number_input("Enter the number of squats",min_value=0,max_value=100)
st.title("Exercise recommender and Personal Trainer")
st.subheader("Refer to the Video for the proper motions")
pTime = 0
path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'squats3.mp4'
placeholder = st.empty()


placeholder.video(path)
st.sidebar.title("Exercise Recommender and Personal Trainer")
n = st.sidebar.number_input("Enter the number of squats",min_value=0,max_value=100)
if st.sidebar.button("Start"):
    placeholder.empty()
cap = cv2.VideoCapture(0)
detector = pm.poseDetector()

    #up3 y500
    # down 1000
    # up15 1100
    #  down 1100
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

  
count = 0
f=0
time.sleep(5)
while True and count < n:
    success, img = cap.read()
    SIDE_WINDOW.image(img, channels='BGR')
    img = detector.findPose(img)
    lmlist = detector.getPosition(img,draw=False)
        
        # if u want all dots then put draw= true and comment out the cv2.circle part in the if part below
        
    if len(lmlist)!=0:
        #cv2.circle(img,(lmlist[25][1],lmlist[25][2]),10,(0,0,255),cv2.FILLED)
        #cv2.circle(img,(lmlist[23][1],lmlist[23][2]),10,(0,0,255),cv2.FILLED) 
            #print(lmlist[23])
        y1 = lmlist[25][2]
        y2 = lmlist[23][2]
            
        length = y2-y1
        if length>=0 and f==0:
            f=1
        elif length<-50 and f==1:
            f=0
            count=count+1
        #print(length)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        #cv2.putText(img,"Total Number of Squats  "+str(int(count)),(70,50),cv2.FONT_HERSHEY_DUPLEX,1,
                    #(60,100,255),3)
        #cv2.putText(img,"Calories Burnt  "+str(int(count)*0.32),(70,150),cv2.FONT_HERSHEY_DUPLEX,1,
          #  (60,100,255),3)
            #img = cv2.resize(img, (900,900))                    # Resize image
        FRAME_WINDOW.image(img, channels='BGR')

        calories = 0.32*count
        cnt = str(count)
        status_text.text("Total Number of Squats %s" %cnt)
        #cv2.destroyWindow(windowname)
#st.write("You have done", count, "squats")
"""