from bs4 import BeautifulSoup
import requests


def Bot(): 
    target = "Sekiro™: Shadows Die Twice - GOTY Edition"

    #Extract info 
    src = requests.get('https://store.steampowered.com/search/?term='+target).text
    soup = BeautifulSoup(src, 'lxml')

    #Look for The target game
    for game in soup.find_all('a', class_='search_result_row ds_collapse_flag'):
        if target in str(game.find('span', class_='title')):
            #print(game)
            break

    #Look for a discount
    discount_per_tag = game.find('div', class_='search_discount') 
    normal_price_tag = game.find('div', class_='discounted') 

    try: 
        discount_per = discount_per_tag.find('span').text
        normal_price = normal_price_tag.find('span').text
        discount_price = str(normal_price_tag)[133:143]
    
        m = target+';'+discount_per+';'+normal_price+';'+discount_price

        # print('\n'+discount_per)
        # print('\n'+'Precio Normal: '+ normal_price + '\t' +'Precio de descuento: '+ discount_price)
        return m

    except:
        #print('\n'+'No tiene descuentos el juego')
        return ''