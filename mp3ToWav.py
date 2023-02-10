import sys
from os import path
from pydub import AudioSegment

#Convert whole folders of mp3 files into wav 

def main():
    input_file = argv[1]
    output_file = argv[2]

    if not exists(input_file):
        print("Error: No input folder")
        exit()
    if not exists(output_file):
        output_file = "Output"

    