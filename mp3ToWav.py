import sys
from os import path, walk 
from pydub import AudioSegment

#Convert whole folders of mp3 files into wav 

def main():
    input_folder = argv[1]
    output_folder = argv[2]

    if not exists(input_folder):
        print("Error: No input folder")
        exit()
    if not exists(output_folder):
        output_folder = "Output"
        os.makedirs(output_folder)

    count = 0
    files = []
    for (root, dirnames, filenames) in walk(input_folder):
        name = Path(root + dirnames)    
                    
        for filename in filenames:
            if filename.endswith('.mp3'):
                newFileName = filename.stem + '.wav'
                dest = root + output_folder + newFileName
                converted = AudioSegment.from_mp3(filename)
                converted.export(dest, format="wav")


    