from google.cloud import vision
import os
from selenium import webdriver
from time import sleep

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

imgFile = '/Users/vdo/Documents/Jeffrey/CMU/Courses/2021T2/49783/assignments/A4/screen.png';
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/Users/vdo/Documents/Jeffrey/CMU/Courses/2021T2/49783/ultimate-retina-317302-4a5e9f81d23b.json';
expectedFaceCount = int(input("Enter expected count of attendees: "));

browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver/geckodriver")
browser.get("https://www.zoom.us/");
input("Press RETURN when everyone has arrived.");
countUses = 0;
try:
    while browser:
        
        #photograph the class
        browser.get_screenshot_as_file("screen.png");
        
        #use Google's face counter
        faceCount = count_faces(imgFile);
        countUses += 1;
        
        #if some are off-screen
        if faceCount < expectedFaceCount: #alert the teacher
            if expectedFaceCount - faceCount == 1:
                os.system('say "Alert! One attendee is missing!"');
            else:
                os.system('say "Alert! ' + str(expectedFaceCount - faceCount) + ' attendees are missing!"');
        
        #wait a few seconds before checking again
        sleep(10);
except Exception as e:
    print('Google Vision Calls: ' + str(countUses));
