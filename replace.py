import cv2
# from moviepy.editor import *
# import os

f = open("./config.txt",mode='r')

src1 = f.readline()
src2 = f.readline()

outfile = f.readline()

R = int(f.readline())
G = int(f.readline())
B = int(f.readline())

src1.replace('\n','').replace('\r','')
src2.replace('\n','').replace('\r','')
# outfile.replace('\n','').replace('\r','')

f.close()


print("origin video: " + src1)
print("AI video: " + src2)
print("result path:" + outfile)


# save audio
# video = VideoFileClip(src1).subclip(0,1)
# audio = video.audio
# audio.write_audiofile("./temp.mp3")

# open video
v1 = cv2.VideoCapture(src1)
v2 = cv2.VideoCapture(src2)

width = v1.get(cv2.CAP_PROP_FRAME_WIDTH)
height = v1.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = v1.get(5)
print("w="+str(int(width))+"h="+str(int(height))+"FPS="+str(fps))


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(outfile, fourcc, fps, (int(width),int(height)))

cnt = 0


# merge video
while v1.isOpened():
    
    r1, f1 = v1.read()
    r2, f2 = v2.read()

    if(r1 == 0):
        print("origin video out.")
        break
    elif(r2 == 0):
        print("AI video out.")
        break

    cnt = cnt +1

    f2 = cv2.resize(f2,(int(width),int(height)), interpolation=cv2.INTER_CUBIC)
    
    outframe = f1


    for i in range(int(height)):
        for j in range(int(width)):
            if(f1[i,j,1] == R and f1[i,j,2] == G and f1[i,j,2] == B):
                outframe[i,j] = f2[i,j]
    
    cv2.imwrite("D:\gen1\origin/test.jpg",outframe)
    out.write(f1)

    if(int(cnt%3) == 0):
        print(str(cnt/30)+"s")


v1.release()
v2.release()
out.release()


# merge audio
# video = VideoFileClip(outfile)
# audio = AudioFileClip("./temp.mp3")      # 讀取音樂

# output = video.set_audio(audio)          # 合併影片與聲音
# output.write_videofile(outfile, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

# os.remove("./temp.mp3")