import random as r
import time
import xlsxwriter

start_time = time.time()

def email(n):
    let_and_num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4',
                    '5', '6', '7', '8', '9']
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', '.', '-', '_']
    domens = ['@mail.ru', '@list.ru', '@bk.ru', '@internet.ru', '@inbox.ru']
    name = ""
    name += let_and_num[r.randint(0, 61)]
    for j in range(1, r.randint(5, 30)):
        symbol = symbols[r.randint(0, 64)]
        if (symbol != ('.' or '-' or '_')) or ((symbol == ('.' or '-' or '_')) and (name[j - 1] != ('.' or '-' or '_'))):
            name += symbol
        else:
            name += let_and_num[r.randint(0, 61)]
    name += let_and_num[r.randint(0, 61)]
    name += domens[r.randint(0, 4)]
    return name


def ip_adress(n):
    ip = str(r.randint(1, 255)) + '.' + str(r.randint(0, 255)) + '.' + str(r.randint(0, 255)) + '.' + str(
        r.randint(0, 255))
    return ip


def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def dates_creator(start, end, prop):
    return strTimeProp(start, end, '%d/%m/%Y', prop)


platforms = ['facebook.com', 'youtube.com', 'instagram.com', 'tiktok.com', 'badoo.com',
             'twiter.com', 'tinder.com', 'vk.com', 'pinterest.ru', 'twitch.tv',
             'viber.com', 'telegram.org', 'likee.video', 'linkedin.com', 'wechat.com',
             'snapchat.com', 'ok.ru', 'my.mail.ru', 'livejournal.com', 'clubhouse.com',
             'dailymotion.com', 'vimeo.com', 'toxicbun.com', 'vimple.ru', 'cincopa.com',
             'brightcove.com', 'dacast.com', 'rutube.ru', 'wistia.com', 'sproutvideo.com',
             'twentythree.com', 'vidyard.com', 'jwplayer.ru', 'videos.kaltura.com', 'panopto.com',
             'tambrl.com', 'liveinternet.ru', 'habr.com', 'currents.google.com', 'vkrugudruzei.ru',
             'last.fm', 'teamo.ru', 'blogger.com', 'subscribe.ru', 'whotrades.com',
             'povarenok.ru', 'scipeople.ru', 'agrobook.ru', 'fotokto.ru', 'nsportal.ru']

products = ["Пуховик Columbia", "Пуховик Marmot", "Пуховик Outdoor Research", "Пуховик BASK", "Пуховик Canada Goose",
            "Коньки Edea", "Коньки Jackson", "Коньки Wifa", "Коньки Risport",
            "Валенки Russy Valenki", "Валенки Ярославские", "Угги Teva", "Угги Tsubo",
            "Ветровка Quiksilver", "Ветровка Under Armour", "Ветровка Trespass", "Ветровка Ellesse",
            "Ветровка Baleaf", "Ветровка Puma", "Ветровка Helly Hansen", "Ветровка Salomon",
            "Костюм Fila", "Костюм New balance", "Костюм Putin team",
            "Костюм Reebok", "Костюм Under armour",
            "Купальник BodyPoetry", "Купальник My Nude Nymph", "Купальник ПАЧЕ", "Купальник Blizhe",
            "Купальник Mesh`n`Flesh", "Купальник LOVEGOODS Lingerie", "Купальник Atumatu", "Купальник Baes",
            "Очки Persol", "Очки Philipp Plein", "Очки Police",
            "Очки Polo Ralph Lauren", "Очки Porsche Design",
            "Зонт Balenciaga", "Зонт Pasotti", "Зонт Blunt", "Зонт Happy Rain",
            "Зонт Zest", "Зонт Fulton", "Зонт Doppler", "Зонт Flioraj",
            "Плед Versace", "Плед Кристин Диор", "Плед Hermes", "Плед Hermes"]

book = xlsxwriter.Workbook('Dataset.xlsx')
sheet = book.add_worksheet()

sheet.set_column('A:A', 50)
sheet.set_column('B:B', 15)
sheet.set_column('C:C', 20)
sheet.set_column('D:D', 15)
sheet.set_column('E:E', 15)
sheet.set_column('F:F', 25)
sheet.set_column('G:G', 40)

sheet.write(0, 0, "Пользователь")
sheet.write(0, 1, "IP адрес")
sheet.write(0, 2, "Платформа")
sheet.write(0, 3, "Дата просмотра")
sheet.write(0, 4, "Кол-во рекламы")
sheet.write(0, 5, "Время просмотра рекламы")
sheet.write(0, 6, "Вид рекламы")

for y in range(260000):
    e = email(1)
    i = ip_adress(1)
    pl = platforms[r.randint(0, 49)]
    d = dates_creator("1/1/2021", "3/10/2022", r.random())
    ad_amount = r.randint(1, 100)
    k = r.randint(30, 120)
    viewing_time = ad_amount * k
    ad_amount = str(ad_amount) + " " + "раз"
    viewing_time = str(viewing_time // 60) + ':' + str(viewing_time % 60) + " " + 'минут'
    if (d.split("/")[1] == "01") or (d.split("/")[1] == "02") or (d.split("/")[1] == "12"):
        pr = products[r.randint(0, 12)]
    elif (d.split("/")[1] == "03") or (d.split("/")[1] == "04") or (d.split("/")[1] == "05"):
        pr = products[r.randint(13, 25)]
    elif (d.split("/")[1] == "06") or (d.split("/")[1] == "07") or (d.split("/")[1] == "08"):
        pr = products[r.randint(26, 38)]
    else:
        pr = products[r.randint(39, 50)]

    sheet.write(y+1, 0, e)
    sheet.write(y+1, 1, i)
    sheet.write(y+1, 2, pl)
    sheet.write(y+1, 3, d)
    sheet.write(y+1, 4, ad_amount)
    sheet.write(y+1, 5, viewing_time)
    sheet.write(y+1, 6, pr)
book.close()

print("--- %s seconds ---" % (time.time() - start_time))