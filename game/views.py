from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import *

# Create your views here.

def home(request):
    import requests
    gameyear = request.GET.get("gameyear")
    print("Addffdrk",gameyear,type(gameyear))
    if gameyear != None:
        print('kbj')
        r = requests.get('https://www.gameinformer.com/' + str(gameyear))
        soup = BeautifulSoup(r.content, 'html.parser')
        elements = soup.find_all(class_='calendar_entry')
        dictList = {}
        for i in elements:
            if i.find('a').get('hreflang') == 'en':
                gameText = i.find('a').get_text()
                gameUrl = "https://www.gameinformer.com"+i.find('a').get('href')
                gameReleaseDate = i.find('time').get_text()+" "+gameyear
                try:
                    data = gi_videogame(gamename=gameText,releaseURL=gameUrl,releaseDate=gameReleaseDate)
                    data.save()
                except:
                    data = gi_videogame.objects.get(gamename=gameText,releaseURL=gameUrl,releaseDate=gameReleaseDate)

                r = requests.get(gameUrl)
                soup = BeautifulSoup(r.content, 'html.parser')
                elements = soup.find_all(class_='blurred-header-content')
                for ii in elements:
                    print(ii.find('img').get('src'))
                    for kk in ii.find_all(class_='field-content'):
                        for iii in kk.find_all(class_='field__wrapper'):
                            print(iii.find(class_='field__label').get_text())
                            print(iii.find(class_='field__items').get_text())
                            dictList[iii.find(class_='field__label').get_text().replace("\n","").replace(":","").strip()] = iii.find(class_='field__items').get_text().replace("\n","").replace(":","").strip()
                        # print("dictList",dictList)
                        if "https://" in ii.find('img').get('src'):
                            imgageUURL = ii.find('img').get('src')
                        else:
                            imgageUURL = "https://www.gameinformer.com" + ii.find('img').get('src')

                        rdata = gi_videogame_release(game_fk=data,platform=dictList['Platform'],no_of_player=dictList['Number of players'],developer=dictList['Developer'],publisher=dictList['Publisher'],genre=dictList['Genre'],release_date=dictList['Release Date'],industry_rating=dictList['Industry rating'],gameImage=imgageUURL)
                        rdata.save()
        return render(request,'home.html')
    else:
        print("lkhkjb")
        data = gi_videogame_release.objects.all()
        print("data",data)
        return render(request,'home.html',{'data':data})
    
                    
    


def datatransfer(request):
    return render(request,'dataShow.html')

