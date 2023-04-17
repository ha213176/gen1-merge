import cv2

f = open("./config.txt",mode='r')

src1 = f.readline()
src2 = f.readline()

outfile = f.readline()

R = f.readline()
G = f.readline()
B = f.readline()

f.close()


print("origin video: " + src1)
print("AI video: " + src2)
print("result path:" + outfile)

# open video
v1 = cv2.VideoCapture(src1)
v2 = cv2.VideoCapture(src2)

width = v1.get(cv2.CAP_PROP_FRAME_WIDTH)
height = v1.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = v1.get(5)
print("w="+str(int(width))+"h="+str(int(height))+"FPS="+str(fps))


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(outfile, fourcc, fps, (int(width),int(height)))

cnt = 0


# merge video
while v1.isOpened():
    
    r1, f1 = v1.read()
    r2, f2 = v2.read()

    if(r1 == 0):
        print("origin video error.")
        break
    elif(r2 == 0):
        print("AI video error.")
        break

    cnt = cnt +1

    f2 = cv2.resize(f2,(int(width),int(height)), interpolation=cv2.INTER_CUBIC)
    
    outframe = f1


    for i in range(int(height)):
        for j in range(int(width)):
            if(f1[i,j,1] > 252 or f1[i,j,2] > 252 or f1[i,j,2] > 252):
                outframe[i,j] = f2[i,j]
    
    out.write(outframe)

    if(int(cnt%3) == 0):
        print(str(cnt/30)+"s")


v1.release()
v2.release()
out.release()
