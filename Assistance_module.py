import cv2
import mediapipe as mp 
import serial
import time
from pyfirmata2 import Arduino, util


#open the port to the first Arduino
Arduino_port = Arduino('/dev/cu.usbmodem11401')


#open the port to the second Arduino
Arduino_port2 = Arduino('/dev/cu.usbmodem11201')

key = util.Iterator(Arduino_port)
key.start()

#determining what is what for the fingers that are going to be raised
thumb = Arduino_port.get_pin('d:9:o')
index = Arduino_port.get_pin('d:10:o')
middle = Arduino_port.get_pin('d:11:o')
ring = Arduino_port.get_pin('d:12:o')
pinky = Arduino_port.get_pin('d:13:o')

#determining what is what for the middle function
index_middle = Arduino_port2.get_pin('d:12:o')
middle_middle = Arduino_port2.get_pin('d:11:o')
ring_middle = Arduino_port2.get_pin('d:10:o')
pinky_middle = Arduino_port2.get_pin('d:9:o')





class HandDetector:
    def __init__ (self, mode= False, hands_to_track=1, detection_confidence = 0.5, tracking_confidence = 0.5) -> None:
        
        self.mode = mode
        self.hands_to_track = hands_to_track
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence



        self.mp_hand = mp.solutions.hands
        self.hands = self.mp_hand.Hands( static_image_mode=self.mode, max_num_hands = self.hands_to_track, min_detection_confidence = self.detection_confidence,
                                        min_tracking_confidence = self.tracking_confidence
                                         )
        
        self.mp_drawing_utils = mp.solutions.drawing_utils 
        self.mp_drawing_styles = mp.solutions.drawing_styles

        self.tips_ids = [8, 12, 16, 20]
        self.thumb_id = [4]



    def find_hands(self, img, draw = True):
        self.result = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if self.result.multi_hand_landmarks:
            if draw:
                for hand_landmark in self.result.multi_hand_landmarks:
                    self.mp_drawing_utils.draw_landmarks(img, hand_landmark, self.mp_hand.HAND_CONNECTIONS)

        return img

        
    def find_positions(self, img, hand_index=0, draw = True ):
        self.land_mark_list = []

        if self.result.multi_hand_landmarks:
            intrest_hand = self.result.multi_hand_landmarks[hand_index]

            for id, landmark in enumerate(intrest_hand.landmark): 
                print(id, landmark)

                h, w, c = img.shape 
                cx, cy = int(landmark.x*w), int(landmark.y*h)

                self.land_mark_list.append([id, cx, cy])

                # to add the landmark id to the actual points on the finger
                #  cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 1)

                if draw:
                    cv2.circle(img, (cx, cy), 10, (250, 0, 0), cv2.FILLED)
            
            return self.land_mark_list
        
    def fingers_ups(self):

        if len(self.land_mark_list) != 0:
            finger_counter = []

            if self.land_mark_list[self.thumb_id[0]][1] > self.land_mark_list[self.thumb_id[0] - 1][1]:
                    finger_counter.append(1)

            else: 
                finger_counter.append(0)

            for tip_id in range (0, 4):

                if self.land_mark_list[self.tips_ids[tip_id]][2] < self.land_mark_list[self.tips_ids[tip_id] - 3][2]:
                        finger_counter.append(1)


                #if self.land_mark_list[self.tips_ids[tip_id]][2] < self.land_mark_list[self.tips_ids[tip_id] - 1][2]:
                    #finger_counter.append[5]
                    


                else:
                    finger_counter.append(0)

            
        # providing data for what to go up or down, Yipee

            if finger_counter == [0,0,0,0,0]:
                thumb.write(0)
                index.write(0) 
                index_middle.write(0)
                middle.write(0) 
                middle_middle.write(0)
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(0) 
                pinky_middle.write(0)

            if finger_counter == [0,0,0,0,1]:
                thumb.write(0)
                index.write(0) 
                index_middle.write(0)
                middle.write(0) 
                middle_middle.write(0)
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(1) 

            if finger_counter == [0,0,0,1,0]:
                thumb.write(0)
                index.write(0) 
                index_middle.write(0)
                middle.write(0) 
                middle_middle.write(0)
                ring.write(1) 
                pinky.write(0) 
                pinky_middle.write(0)

            if finger_counter == [0,0,0,1,1]:
                thumb.write(0)
                index.write(0) 
                index_middle.write(0)
                middle.write(0) 
                middle_middle.write(0)
                ring.write(1)
                pinky.write(1)

            if finger_counter == [0,0,1,0,0]:
                thumb.write(0)
                index.write(0) 
                index_middle.write(0)
                middle.write(1) 
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(0)
                pinky_middle.write(0)
            
            if finger_counter == [0,0,1,0,1]:
                thumb.write(0)
                index.write(0) 
                index_middle.write(0)
                middle.write(1)
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(1)

            
            if finger_counter == [0,0,1,1,0]:
                thumb.write(0)
                index.write(0) 
                index_middle.write(0)
                middle.write(1)
                ring.write(1)
                pinky.write(0)
                pinky_middle.write(0)

            
            if finger_counter == [0,0,1,1,1]:
                thumb.write(0)
                index.write(0) 
                index_middle.write(0)
                middle.write(1)
                ring.write(1)
                pinky.write(1)

            
            if finger_counter == [0,1,0,0,0]:
                thumb.write(0)
                index.write(1)
                middle.write(0) 
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [0,1,0,0,1]:
                thumb.write(0)
                index.write(1)
                middle.write(0) 
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(1)

            if finger_counter == [0,1,0,1,0]:
                thumb.write(0)
                index.write(1)
                middle.write(0) 
                middle_middle.write(0)
                ring.write(1)
                pinky.write(0)
                pinky_middle.write(0)
            
            if finger_counter == [0,1,1,0,0]:
                thumb.write(0)
                index.write(1)
                middle.write(1) 
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [0,1,1,0,1]:
                thumb.write(0)
                index.write(1)
                middle.write(1)
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(1)

            if finger_counter == [0,1,1,1,0]:
                thumb.write(0)
                index.write(1)
                middle.write(1)
                ring.write(1)
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [0,1,1,1,1]:
                thumb.write(0)
                index.write(1)
                middle.write(1) 
                ring.write(1) 
                pinky.write(1)

            if finger_counter == [1,0,0,0,0]:
                thumb.write(1)
                index.write(0) 
                index_middle.write(0)
                middle.write(0) 
                middle_middle.write(0)
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [1,0,0,0,1]:
                thumb.write(1)
                index.write(0) 
                index_middle.write(0)
                middle.write(0) 
                middle_middle.write(0)
                ring.write(0)
                ring_middle.write(0) 
                pinky.write(1)
                            
            if finger_counter == [1,0,0,1,0]:
                thumb.write(1)
                index.write(0) 
                middle.write(0)
                middle_middle.write(0) 
                ring.write(1) 
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [1,0,0,1,1]:
                thumb.write(1)
                index.write(0) 
                index_middle.write(0)
                middle.write(0) 
                middle_middle.write(0)
                ring.write(1)
                pinky.write(1)

            if finger_counter == [1,0,1,0,0]:
                thumb.write(1)
                index.write(0)
                index_middle.write(0) 
                middle.write(1)
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [1,0,1,0,1]:
                thumb.write(1)
                index.write(0) 
                index_middle.write(0)
                middle.write(1)
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(1)

            if finger_counter == [1,0,1,1,0]:
                thumb.write(1)
                index.write(0) 
                index_middle.write(0)
                middle.write(1)
                ring.write(1) 
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [1,0,1,1,1]:
                thumb.write(1)
                index.write(0) 
                index_middle.write(0)
                middle.write(1)
                ring.write(1)
                pinky.write(1)


            if finger_counter == [1,1,0,0,0]:
                thumb.write(1)
                index.write(1)
                middle.write(0) 
                middle_middle.write(0)
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [1,1,0,0,1]:
                thumb.write(1)
                index.write(1)
                middle.write(0)
                middle_middle.write(0) 
                ring.write(0)
                ring_middle.write(0) 
                pinky.write(1)

            if finger_counter == [1,1,0,1,0]:
                thumb.write(1)
                index.write(1)
                middle.write(0)
                middle_middle.write(0) 
                ring.write(1)
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [1,1,1,0,0]:
                thumb.write(1)
                index.write(1)
                middle.write(1)
                ring.write(0) 
                ring_middle.write(0)
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [1,1,1,0,1]:
                thumb.write(1)
                index.write(1) 
                middle.write(1)
                ring.write(0)
                ring_middle.write(0) 
                pinky.write(1)

            if finger_counter == [1,1,1,1,0]:
                thumb.write(1)
                index.write(1)
                middle.write(1)
                ring.write(1)
                pinky.write(0)
                pinky_middle.write(0)

            if finger_counter == [1,1,1,1,1]:
                thumb.write(1)
                index.write(1)
                middle.write(1)
                ring.write(1)
                pinky.write(1)
                

            return finger_counter
        
        
    def fingers_middle(self):
        
        minimum_y = int(500)
        maximum_y = int(700)
        fingertip_indicies = [8, 12, 16, 20]


        if len(self.land_mark_list) != 0:
            finger_middled = []

            for tip_id in fingertip_indicies:
                    y_value = self.land_mark_list[tip_id][2]

                    if minimum_y <= y_value <= maximum_y:
                        finger_middled.append(1)
                        print("up we go")
            
                    else:
                        finger_middled.append(0)
                        print("down we go")

             # providing data on what to do if it the finger is middle, Yipee

            if finger_middled == [0,0,0,0]:
                index_middle.write(0) 
                middle_middle.write(0) 
                ring_middle.write(0) 
                pinky_middle.write(0) 

            if finger_middled == [0,0,0,1]:
                index_middle.write(0) 
                middle_middle.write(0) 
                ring_middle.write(0) 
                pinky_middle.write(1) 
                pinky.write(0)

            if finger_middled == [0,0,1,0]:
                index_middle.write(0) 
                middle_middle.write(0) 
                ring_middle.write(1) 
                ring.write(0)
                pinky_middle.write(0) 

            if finger_middled == [0,0,1,1]:
                index_middle.write(0) 
                middle_middle.write(0) 
                ring_middle.write(1) 
                ring.write(0)
                pinky_middle.write(1)
                pinky.write(0)

            if finger_middled == [0,1,0,0]:
                index_middle.write(0) 
                middle_middle.write(1) 
                middle.write(0)
                ring_middle.write(0) 
                pinky_middle.write(0)
            
            if finger_middled== [0,1,0,1]:
                index_middle.write(0) 
                middle_middle.write(1) 
                middle.write(0)
                ring_middle.write(0) 
                pinky_middle.write(1)
                pinky.write(0)

            
            if finger_middled == [0,1,1,0]:
                index_middle.write(0) 
                middle_middle.write(1) 
                middle.write(0)
                ring_middle.write(1) 
                ring.write(0)
                pinky_middle.write(0)

            
            if finger_middled == [0,1,1,1]:
                index_middle.write(0) 
                middle_middle.write(1) 
                middle.write(0)
                ring_middle.write(1) 
                ring.write(0)
                pinky_middle.write(1)
                pinky.write(0)

            
            if finger_middled == [1,0,0,0]:
                index_middle.write(1) 
                index.write(0)
                middle_middle.write(0) 
                ring_middle.write(0) 
                pinky_middle.write(0)

            if finger_middled == [1,0,0,1]:
                index_middle.write(1) 
                index.write(0)
                middle_middle.write(0) 
                ring_middle.write(0) 
                pinky_middle.write(1)
                pinky.write(0)

            if finger_middled == [1,0,1,0]:
                index_middle.write(1) 
                index.write(0)
                middle_middle.write(0) 
                ring_middle.write(1) 
                ring.write(0)
                pinky_middle.write(0)
            
            if finger_middled == [1,1,0,0]:
                index_middle.write(1) 
                index.write(0)
                middle_middle.write(1) 
                middle.write(0)
                ring_middle.write(0) 
                pinky_middle.write(0)

            if finger_middled == [1,1,0,1]:
                index_middle.write(1) 
                index.write(0)
                middle_middle.write(1) 
                middle.write(0)
                ring_middle.write(0) 
                pinky_middle.write(1)
                pinky.write(0)

            if finger_middled == [1,1,1,0]:
                index_middle.write(1) 
                index.write(0)
                middle_middle.write(1) 
                middle.write(0)
                ring_middle.write(1) 
                ring.write(0)
                pinky_middle.write(0)

            if finger_middled == [1,1,1,1]:
                index_middle.write(1) 
                index.write(0)
                middle_middle.write(1) 
                middle.write(0)
                ring_middle.write(1) 
                ring.write(0)
                pinky_middle.write(1)
                pinky.write(0)

            return(finger_middled)



