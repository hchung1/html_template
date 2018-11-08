import os
from PIL import Image
def edit_image(path, lists,width,height):
  home=os.getcwd()
  os.chdir(home+path)
  for ims in lists:
    im=Image.open(ims)
    maxsize = (width, height)
    tn_image = im.resize(maxsize, Image.ANTIALIAS)  
    tn_image.save(ims)
  os.chdir(home)
def file_text(files):
  f= open(files,"r")
  text = f.read().replace('\n','')
  f.close()
  text = text.split("==")
  for i in range(len(text)):
    text[i] = text[i].split('&&')
  return text
def file_write(path,lists):
  text = file_text("text_file"+path+".txt")
  f=open(path[1:]+".html","w")
  for i in range(len(text)):
    try:
      f.write("<img src=\""+path[1:]+ "/"+lists[i]+"\" style=\"width:100%\"></img>\n")
    except:
      pass
    for j in range(len(text[i])):
      f.write("<p>"+text[i][j]+"</p>")
  f.close()
def write_members():
  f=open("text_file/members.csv","r")
  data=f.read().split('\n')
  f.close()
  for i in range(len(data)):
    data[i]=data[i].split(",")
  data.remove([''])
  sets=len(data)//6
  remain=len(data)%6
  t=0
  f=open("member_image.html","w")
  for i in range(sets):
    f.write("<div class=\"row main_content bodies\">")
    for i in range(6):
      f.write("<div class=\"col-2\" align=\"center\"><img src=\"member_image/"+data[t][4]+"\" style=\"width:100%\"></img><p>"+data[t][0]+"</p><p>Position: "+data[t][3]+"</p><p>Phone: "+data[t][1]+"</p><p>Email: "+data[t][2]+"</p></div>")
      t+=1
    f.write("</div><br>")

  f.write("<div class=\"row main_content bodies\">")

  for i in range(remain):
    f.write("<div class=\"col-2\" align=\"center\"><img src=\"member_image/"+data[t][4]+"\" style=\"width:100%\"></img><p>"+data[t][0]+"</p><p>Position: "+data[t][3]+"</p><p>Phone: "+data[t][1]+"</p><p>Email: "+data[t][2]+"</p></div>")
    t+=1
  f.write("</div>")
  f.close()    
def project_writer():
  lists=file_text("text_file/project.txt")
  times=len(lists)//7
  print times
  f = open("project_image.html","w")
  for i in range(times):
    f.write("<div class=\"row main_content bodies\"></div>")
    f.write("<img src=\"project_image/"+''.join(lists[i*7+0])+"\" style=\"width:100%\"></img>")
    f.write("<h3>"+''.join(lists[i*7+1])+"</h3>")
    f.write("<p>"+''.join(lists[i*7+2])+"</p>")
    f.write("<p>"+''.join(lists[i*7+3])+"</p>")
    f.write("<p>"+''.join(lists[i*7+4])+"</p>")
    f.write("<p>"+''.join(lists[i*7+5])+"</p>")
    f.write("<p>"+''.join(lists[i*7+6])+"</p>")
    f.write("</div>")
  f.close()
def check_path(path,width,height,i):
  listing={0:file_write,1:file_write}
  home=os.getcwd()
  lists = os.listdir(home+path)
  #edit_image(path,lists,width,height)
  if (i==0):
    listing[i](path, lists)
#check_path("/home_image",1000,1000,0)
#check_path("/about_image",1000,1000,0)
#check_path("/member_image",250,250,1)
check_path("/trip_image",1000,1000,0)
#write_members()
project_writer()
