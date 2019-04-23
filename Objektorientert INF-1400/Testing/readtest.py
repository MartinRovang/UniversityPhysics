
import csv


class Reader:
    def __init__(self):
        self.filereader = csv.writer(open("lol.txt", 'a'))
    
    def put_in(self, stringed):
        # stringed on the form larve-hest-mann
        self.filereader.writerow([stringed])
        print('Wrote to file %s'%stringed.split('-'))



