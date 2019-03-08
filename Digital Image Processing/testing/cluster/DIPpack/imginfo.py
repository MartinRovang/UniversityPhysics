import exifread
from pprint import pprint

def getinfo(Image):
    """Image --> path to image"""
    im = open(Image, 'rb')
    tags = exifread.process_file(im)
    pprint(tags)