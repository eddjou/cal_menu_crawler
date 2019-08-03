import urllib.request as req
import re

def writemenu(htmlcode,key):
    reg = re.compile('</p><p> (.+?) <')
    if (re.search(key+"(.+?)Brunch(.+?)</div>", htmlcode)):
        brunchstr = re.search(key+"(.+?)Brunch(.+?)</div>", htmlcode).groups()[1]
        brunch = reg.findall(brunchstr)
        pageFile.write("\tBrunch:\r")
        for i in range(len(brunch)):
            if brunch[i]!="N/A":
                pageFile.write("\t\t" + brunch[i] + "\r")
    elif(re.search(key+"(.+?)Breakfast(.+?)</div>",htmlcode)):
        breakstr=re.search(key+"(.+?)Breakfast(.+?)</div>",htmlcode).groups()[1]
        breakf = reg.findall(breakstr)
        pageFile.write("\tBreakfast:\r")
        for i in range(len(breakf)):
            if breakf[i]!="N/A":
                pageFile.write("\t\t" + breakf[i] + "\r")
        if(re.search(key+"(.+?)Lunch(.+?)</div>",htmlcode)):
            lunchstr = re.search(key+"(.+?)Lunch(.+?)</div>", htmlcode).groups()[1]
            lunch = reg.findall(lunchstr)
            pageFile.write("\tLunch:\r")
            for i in range(len(lunch)):
                if lunch[i]!="N/A":
                    pageFile.write("\t\t" + lunch[i] + "\r")
    if(re.search(key+"(.+?)Dinner(.+?)</div>",htmlcode)):
        dinnerstr = re.search(key+"(.+?)Dinner(.+?)</div>", htmlcode).groups()[1]
        dinner=reg.findall(dinnerstr)
        pageFile.write("\tDinner:\r")
        for i in range(len(dinner)):
            if dinner[i]!="N/A":
                pageFile.write("\t\t" + dinner[i] + "\r")

page=req.urlopen('https://caldining.berkeley.edu/menu.php')
htmlcode=str(page.read())
print(htmlcode)
pageFile = open('menu.txt','w')
pageFile.write("Cafe3:\r")
writemenu(htmlcode,"Cafe_3")
pageFile.write("\rCrossroads:\r")
writemenu(htmlcode,"Crossroads")
pageFile.write("\rFoothill:\r")
writemenu(htmlcode,"Foothill")
pageFile.close()