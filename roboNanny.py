from google.cloud import vision
import os

#def detect_faces(path):
#    """Detects faces in an image."""
#    import io;
#    client = vision.ImageAnnotatorClient();
#
#    with io.open(path, 'rb') as image_file:
#        content = image_file.read();
#
#    image = vision.Image(content=content);
#
#    response = client.face_detection(image=image);
#    faces = response.face_annotations;
#
#    # Names of likelihood from google.cloud.vision.enums
#    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')
#    print('Faces:')
#
#    for face in faces:
#        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
#        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
#        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
#
#        vertices = (['({},{})'.format(vertex.x, vertex.y)
#                    for vertex in face.bounding_poly.vertices])
#
#        print('face bounds: {}'.format(','.join(vertices)))
#
#    if response.error.message:
#        raise Exception(
#            '{}\nFor more info on error messages, check: '
#            'https://cloud.google.com/apis/design/errors'.format(
#                response.error.message))

def count_faces(path):
    """Detects faces in an image."""
    import io;
    client = vision.ImageAnnotatorClient();
    
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read();
        
    image = vision.Image(content=content);
    response = client.face_detection(image=image);
    faces = response.face_annotations;
    
    return len(faces);

expectedFaceCount = int(input("Enter expected count of attendees: "));

##use Google's face counter (working):
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/Users/vdo/Documents/Jeffrey/CMU/Courses/2021T2/49783/assignments/A4/ultimate-retina-317302-4a5e9f81d23b.json';
##print("Google's count of faces:", count_faces('/Users/vdo/Documents/Jeffrey/CMU/Courses/2021T2/49783/assignments/A4/screenManual.jpg'));
#imgFile = '/Users/vdo/Documents/Jeffrey/CMU/Courses/2021T2/49783/assignments/A4/screenManual.png';
#faceCount = count_faces(imgFile);
#if faceCount < expectedFaceCount:
#    if expectedFaceCount - faceCount == 1:
#        os.system('say "Alert! One attendee is missing!"');
#    else:
#        os.system('say "Alert! ' + str(expectedFaceCount - faceCount) + ' attendees are missing!"');
    
##bring meeting window to foreground (not working; very tricky in MacOS):
#objName = {"title": "Zoom Meeting", "type": "NSWindow"};
##waitFor("object.exists(\"%s\")" % objName, 20000);
#nsw = findObject(objName);
#nsw.makeKeyAndOrderFront_(nsw);

#take a screenshot:
##attempt 1:
#import pyautogui;
#screenshot = pyautogui.screenshot();
#screenshot.save("screen.png");

##attempt 2:
#from PIL import ImageGrab
#image = ImageGrab.grab(bbox=(0,0,700,800))
#image.save('screen2.png')

##attempt 3:
#import pyautogui;
#import imutils;
#import cv2;
#import numpy as np;
#screenshot = pyautogui.screenshot();
#image = pyautogui.screenshot();
##screenshot.save("screen.png");
##image = ImageGrab.grab(bbox=(0,0,700,800));
#image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR);
#cv2.imwrite("in_memory_to_disk.png", image);
#cv2.imshow("Screenshot", imutils.resize(image, width=600));
#cv2.waitKey(0);

#attempt 4 (works!):
from selenium import webdriver
from time import sleep
browser = webdriver.Firefox()
browser.get("https://www.ecosia.org/");
sleep(1)
browser.get_screenshot_as_file("screen4.png")
browser.quit()
