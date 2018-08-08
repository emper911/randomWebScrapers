import requests
import textwrap
from bs4 import BeautifulSoup
from lxml import html
from time import sleep
import smtplib
 


def main():
    same = 0
    err = True
    while True:
        url = "https://www.apple.com/us-hed/shop/browse/home/specialdeals/mac/macbook_pro/15"
        while err:
            try:
                page = requests.get(url)
            except requests.exceptions.RequestException as e:
                print(e)
                continue
            err = False
            
        soup = BeautifulSoup(page.content, 'html.parser')
        find2015 = soup.find_all('td', class_= "specs")
        for i in range(len(find2015)):
            [x.extract() for x in find2015[i]('h3')]
            [x.extract() for x in find2015[i]('p')]

        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        year = "2000"
        count = 0
        find2015_str = [str(x) for x in find2015]
        for i in range(len(find2015_str)):
            for mon in months:
                index = find2015_str[i].find(mon)
                if index != -1:
                    index2 = find2015_str[i].find("<br/>")
                    releaseDate = find2015_str[i][index:index2]
                    year = "".join([x for x in releaseDate if x.isnumeric()])
                    if year == "2015":
                        count += 1
        
        if count == same:
            print("No change yet. Still: {0}".format(count))
            continue
        elif count > same:
            same = count
            print("found {0}!".format(count))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("rtaro.suzuki@gmail.com", "Majikarpent710!")
        
            msg = "There are {0} from 2015 BUY COMPUTER!".format(count)
            server.sendmail("rtaro.suzuki@gmail.com", "emper96@gmail.com", msg)
            server.quit()
        else:
            same = count
            print("nothing yet. Count: {0}".format(count))
        
        sleep(600)
    

        

main()

