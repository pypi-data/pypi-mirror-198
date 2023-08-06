from getmac import get_mac_address as gma
from cv2 import dnn_superres
from statistics import mode
import numpy as np
import warnings
import cv2
import re
import subprocess
warnings.filterwarnings("ignore")

def predark(img):
    im_nr = cv2.detailEnhance(img, sigma_s=10, sigma_r=1)
    im_nr = cv2.fastNlMeansDenoisingColored(im_nr, None, 3,3, 7, 20)
    return im_nr 

def upsacale(image,cvdnn_path):

# Create an SR object
    sr = dnn_superres.DnnSuperResImpl_create()
    sr.readModel(cvdnn_path)
    sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    sr.setModel("fsrcnn", 4)
    result = sr.upsample(image)
    return result

def inference(img_path,ocr,cvdnn_path):
    try:
        machineid = subprocess.run(['cat', '/etc/machine-id'], stdout=subprocess.PIPE)
        if(machineid.stdout.decode('utf-8').rstrip() in ["4c44501bf7b14db9a99e21cc0fb0abfe","a3d9197b765643568af09eb2bd3e5ce7","a3d9197b765643568af09eb2bd3e5ce7"]):
            print("Configured Sucessfully")
            image= cv2.imread(img_path)
            img_path=upsacale(image,cvdnn_path)
            #img_path=predark(img_path)
            result = ocr.ocr(img_path, cls=True)
            result=result[0]
            txts1 = [line[1][0] for line in result]
            scores1 = [line[1][1] for line in result]
            if len(txts1)==0:          #no object detected
                return "999",float(0.0)  #object not found
            regex = '^[+-]?[0-9]+\.[0-9]$'
            txts=[]
            scores=[]
            for i in range(0,len(txts1)):# most repeating txts
                try:
                                if float(txts1[i]) > 20.0 or float(txts1[i]) < 15.0:
                                    pass
                                else:
                                    if re.search(regex, txts1[i]):
                                        txts.append(txts1[i])
                                        scores.append(scores1[i])
                                    else:
                                        pass
                                                
                except Exception as E:
                    pass
            if len(txts)==0:
                   return "999",float(0.0) 
            try:
                txts=[mode(txts)]
                scores=[max(scores)]  
            except:
                status="no unique"  
            if len(txts)>1:           # if both txts are different
                case=np.argmax(scores)
                scores=[scores[case]]
                txts=[txts[case]]
            if(re.search(regex, txts[0]) and float(txts[0])<20.0 and float(txts[0])>=15.0):
                    return str(txts[0]),float(scores[0])
            else:
                    return "999",float(0.0)
        else:
            return "999",float(0.0)  #could not configured
    except Exception as E:
        print(E)
        return "999",float(0.0) # could not process,Exception

'''if __name__ == "__main__":
    txts,scores=inference("img2.jpg","en")
    print(txts," ",type(txts)," ",scores," ",type(scores))'''
    
