import numpy as np
from PIL import Image

#open file
file = open("test3_points.txt","r")
file_2 = open("test4_points.txt","r")

data_1 = [] #new empty matrix for data-1
for line in file:
    line = line.rsplit() 
    data_1.append(line)     
    data_1.append(line)
    ##we read line by line, ignoring the gaps in txt

data_2 = [] #new empty matrix for data-2
for line in file_2:
    line = line.rsplit()
    data_2.append(line)     
    data_2.append(line)
    ##We read line by line, ignoring the gaps in txt

f = "D:\\HACETTEPE\\fotogrametri\\fotograf3.jpeg"
img = Image.open(f)

width,height = img.size
pixels = []

for i in range(width):
    for j in range(height):
        pixels.append([i,j])
        pixels.append([i,j])
#print(pixels)
pixelnumber = np.array(pixels)
print("Pixel Coordinates Of Our Photo")
print(pixels)
        
def inserting(n):
    co_mat = np.zeros(shape=[2*n, 6]) ##creating a matrix filled with zeros for coefficient matrix
    obs_mat = np.zeros(shape=[2*n,1]) ##creating a matrix filled with zeros for observation matrix
    try:
        for i in range(2*n):
            for j in range(6):
                
                if i %2 == 0:    
                    co_mat[i,0]=1
                    co_mat[i,[1,2]]= data_1[i]
                    co_mat[i+1,3]=1
                    co_mat[i+1,[4,5]]= data_1[i]

                    obs_mat[i] = data_2[i][0]
                    obs_mat[i+1] = data_2[i][1]

                elif i%2!=0:
                    co_mat[i+1,0]=1
                    co_mat[i+1,[1,2]]= data_1[i+2]
                    co_mat[i+2,3]=1
                    co_mat[i+2,[4,5]]= data_1[i+2]

                    obs_mat[i+1] = data_2[i+2][0]
                    obs_mat[i+2] = data_2[i+2][1]              
    except:
        IndexError
    normal_eq = np.dot(co_mat.T,co_mat)
    b = np.dot(co_mat.T,obs_mat)

    unk_par = np.dot(np.linalg.inv(normal_eq),b)
    print("**COEFFICIENTS MATRİX**")
    print(co_mat) #coefficient matrix
    print("***OBSERVATİON MATRİX***")
    print(obs_mat) #observation matrix
    print("****UNKNOWN PARAMETER****")
    print(unk_par) #unknown parameters matrix
    #aa=np.linalg.lstsq(co_mat,obs_mat)[0] #I used to try
    #print(aa)
    f = open("unknown_parameters.txt", "w")
    f.write(unk_par)
    f.close 

    def affine(k):
        co_mat2 = np.zeros(shape=[2*k, 6]) ##creating a matrix filled with zeros for coefficient matrix
        try:
            for i in range(2*k):
                for j in range(6):
                
                    if i %2 == 0:    
                        co_mat2[i,0]=1
                        co_mat2[i,[1,2]]= pixelnumber[i]
                        co_mat2[i+1,3]=1
                        co_mat2[i+1,[4,5]]= pixelnumber[i]

                    elif i%2!= 0:
                        co_mat2[i+1,0]=1
                        co_mat2[i+1,[1,2]]= pixelnumber[i+2]
                        co_mat2[i+2,3]=1
                        co_mat2[i+2,[4,5]]= pixelnumber[i+2]
        except:
            IndexError              
        print("Coefficient Matrix For All Pixels")
        print(co_mat2)       
        newpixel = np.dot(co_mat2,unk_par)
        newpixel=newpixel.reshape((1920000,2)).astype(int)
        print("New Pixels")
        print(newpixel)

        img = Image.open(f)
        width1,height1 = img.size
        pixels2 = []

        for x in range(width1):
            for y in range(height1):
                pixels2.append([x,y])
        pixels2 = np.array(pixels2)
        print(pixels2)

        for b in range (k):
            pixels2[b,[0,1]] = newpixel[b,[0,1]] 
        print("Transformation Pixels")
        print(pixels2)


    affine(1920000)

inserting(4)
