import allInOne
import borderUtil
import nameUtil
print("Input the latitude and longitude of the point")
lat=45.660392#float(input("lat: "))45.660392
long=25.615819#float(input("long: "))25.615819

#allInOne.generate((lat,long))
#borderUtil.add_border("HartaGenerata.png",'HartaMarita.png', fill = '#F2F2F2', bottom = 1600)
nameUtil.addText(srcImg='D:\pyCharmProjects\mapProject\HartaMarita.png',textAdd="\t Brasov,Romania  ")
nameUtil.addText(srcImg='D:\pyCharmProjects\mapProject\HartaScrisa.png', textAdd="\n\tPatricia and Alex")
nameUtil.addText(srcImg='D:\pyCharmProjects\mapProject\HartaScrisa.png', textAdd=" \n\n\t\tOur First Kiss  ") #you can use newline and tabs
#TODO: idk if doable: Add point to map//edit: maybe doable with PIL and a marker png--meh
#TODO: make this an app so i don`t have to open pycharm -- still got to do it

#cityGen si waterGen e cod nemodificat
#oras si ape e cod modificat si facut fara hardcoded variables
#consider using graph_from_address conisering that u would use that on insta too
