import urllib.request
import cv2
import numpy as np
import os

# tast at hand:
# open link containing links to images from imagenet
# go to link and download the image
# resize the image using opencv
# save the image

def store_raw_image():
    neg_image_link='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03906997'
    #'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00450335'
    # http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03906997 
    #pens
    #contains images of people 
    neg_image_urls=urllib.request.urlopen(neg_image_link).read().decode()
    if not os.path.exists('Images_Pen/neg'):
        os.makedirs('Images_Pen/neg')
    
    pic_num=890;
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i,'Images_Pen/neg/{}.jpg'.format(pic_num))
            img=cv2.imread('Images_Pen/neg/{}.jpg'.format(pic_num),cv2.IMREAD_GRAYSCALE)
            resized_image= cv2.resize(img,(100,100))
            cv2.imwrite('Images_Pen/neg/{}.jpg'.format(pic_num),resized_image)
            pic_num+=1;

        except Exception as e:
            print(str(e))

def find_nonsense(): # removes images similar to images placed in nonsense folder
    for file_type in ['Images_Pen/neg']:
        for img in os.listdir(file_type):
            for nonsense in os.listdir('Images_Pen/Nonsense'):
                try:
                    image_path=str(file_type)+'/'+str(img)
                    # print(image_path)
                    useless=cv2.imread('Images_Pen/Nonsense'+'/'+str(nonsense))
                    # print(useless.shape)
                    check=cv2.imread(image_path)
                    # print(check.shape)
                    if useless.shape==check.shape and not(np.bitwise_xor(useless,check).any()):
                        print("Ugly image")
                        print(image_path)
                        os.remove(image_path)

                except Exception as e:
                    print(str(e))


def pos_n_neg():
    for file_type in ['Images_Pen/neg']:
        for img in os.listdir(file_type):
            if file_type=='Images_Pen/neg':
                line='./'+file_type+'/'+img+'\n\n'
                with open('Images_Pen/bg.txt','a') as f: #all files containing negative images
                    f.write(line)
            # elif file_type=='Images_Pen/pos':
            #     line=file_type+'/'+img+' 1 0 0 50 50\n' #expecting image to be present in 50*50 box

            #     with open('Images_Pen/info.txt','a') as f:
            #         f.write(line)

pos_n_neg()
