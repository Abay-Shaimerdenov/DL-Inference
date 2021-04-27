import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
from scipy import ndimage
from xml.etree import ElementTree

def extract_features(filename):
    '''Here, we extract the seven selected features from the input image'''
    
    img = cv2.imread(filename, 3)
                   
    #Extracting the bounding box of the main object for area by perim and aspect ratio
    #newly added - was not present in last year's file, were the area by perima and aspect ratio of the whole image was taken
    xml_directory = "images/val/xml"

    file_path = xml_directory + '\\' + filename[18:41] + '.xml'
    tree = ElementTree.parse(file_path)
    root = tree.getroot()
    x_min = int(root.find("object/bndbox/xmin").text)
    x_max = int(root.find("object/bndbox/xmax").text)
    y_min = int(root.find("object/bndbox/ymin").text)
    y_max = int(root.find("object/bndbox/ymax").text)
    
    width = x_max - x_min
    height = y_max - y_min
    
    aspect_ratio = width / height                     # aspect ratio  
    
    area_by_perim = (height * width) / ((height + width) * 2)             # area by perimeter
    
    '''Average perceived brightness'''
    B = np.mean(img[:, :, 0])
    G = np.mean(img[:, :, 1])
    R = np.mean(img[:, :, 2])
    average_perceived_brightness = (math.sqrt(0.241*(R**2) + 0.691*(G**2) + 0.068*(B**2)))

    
    '''Edges - simplecv method - newly added'''
    #http://bennycheung.github.io/recognizing-snacks-using-simplecv
    '''
    img_2 = cv2.imread(filename, 3)
    if (img_2.shape[0] > img_2.shape[1]):
        p = img_2.shape[0]
    else:
        p = img_2.shape[1]
    minLine = 0.01*p
    gap = 0.1*p
    threshold = 10

    gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 100)
    lines = cv2.HoughLinesP(edges,rho=1,theta=np.pi/180, threshold=threshold, minLineLength = minLine, maxLineGap = gap)


    def lengthl(x1, y1, x2, y2):                          #function to calculate the length of the line
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    fs = []
    if lines is None:
        edge_length1 = 0
    else:
        for l in lines:
            for x1,y1,x2,y2 in l:
                fs.append(lengthl(x1,y1,x2,y2))
        ls = [i/p for i in fs] #normalize to image length
        lhist = np.histogram(ls, bins = 7, range=(0,1))
        edge_length1 = lhist[0].tolist()[0] + lhist[0].tolist()[1] + lhist[0].tolist()[2]'''

    
    '''Edges - opencv method'''
    edges = cv2.Canny(img, 100, 200)
    threshold = 100
    labeled, nr_objects = ndimage.label(edges > threshold)
    unique, lengths = np.unique(labeled, return_counts=True)
    y_e, x_e, g = plt.hist(lengths[1:], bins = 7)
    edge_length1 = y_e[0]

    
    '''Hue - simplecv method - newly added'''
    '''
    img_2 = cv2.imread(filename, 3)
    hls = cv2.cvtColor(img_2, cv2.COLOR_BGR2HLS )

    hue, lig, sat = cv2.split(hls)

    hue = hue.flatten()
    hist = np.histogram(hue, bins = 7, normed=True, range=(0,255))
    hue1 = hist[0].tolist()[0]
    '''


    '''Hue - opencv method'''
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    hue, sat, val = cv2.split(hsv)
    hue = hue.flatten()
    y_h, x_h, bars = plt.hist(hue, bins = 7)
    hue1 = y_h[0]


    '''Contrast'''
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    contrast = imgGrey.std()                              
    
    '''KP surf'''
    img = cv2.imread(filename)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    surf = cv2.xfeatures2d.SURF_create(hessianThreshold = 700) 
    keypoints = surf.detect(img_gray, None)
    kp_surf = len(keypoints)

    return [kp_surf, average_perceived_brightness, contrast, area_by_perim, aspect_ratio, edge_length1, hue1, [x_min, x_max, y_min, y_max]]
