import cv2
from person_tracker import person_tracking as tk



def main():
    cap = cv2.VideoCapture(0)
    tk.main(cap)
    

main()