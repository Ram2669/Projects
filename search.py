import re
import logging as log

log.basicConfig(level=log.DEBUG,filename="error.log")
class Search:
    def __init__(self,filename):
        try:
            
            with open(filename,"r") as f1:
                    self.line = f1.readlines()
        except FileNotFoundError:
            log.error(f"File : {filename} not found")
            raise Exception(f"file : {filename} not found")

    def clean(self):
        self.line = [re.sub(r'\W\s','',ele) for ele in self.line]
    def getLines(self,word):
            res = [word]
            for indx in range(len(self.line)):
                if re.search(rf'\b{word}\b',self.line[indx],re.IGNORECASE):
                    res.append((indx+1,self.line[indx].strip()))
            if len(res) == 1:
                log.error(f"Word : {word} not found")
                res.append((0,f"{word} not found in the file"))
                return res
            else:
                log.info("Word found in the file")
                return res
             
            

