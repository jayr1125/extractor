#import the libraries
import os
import shutil
from zipfile import ZipFile

def file_extractor(filepath):
    """
    Creates a folder with name similar to the zip file to be extracted.
    Extracts the zip file the folder created.
    """
    #create a list of filenames in the filepath
    sources = os.listdir(filepath)
    #removes the .zip extension from filenames
    destinations = []
    for source in sources:
        destinations.append(source.replace('.zip',''))
    #create a folder for every filename
    for destination in destinations:
        path = filepath + '\\' + destination
        os.mkdir(path)
    
    #create a dictionary of sources and destinations
    pts = dict(zip(sources,destinations))
    for i,j in pts.items():
        src = filepath + '\\' + i
        dst = filepath + '\\' + j
        #move the sources to the destinations
        shutil.move(src,dst)
        #change to destination directory
        os.chdir(dst)
        #open file as zip object
        with ZipFile(i, 'r') as zipObj:
            zipObj.extractall()
            zipObj.close()
        #delete the zip file after extraction
        os.remove(i)
        os.chdir(r'C:\Users\Desktop')
        
file_extractor(input("Input Filepath: "))
