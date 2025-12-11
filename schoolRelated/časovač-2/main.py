from browser import document, timer

# KROK 1 – jednoduchý klik

def pozdrav(ev):
    # TODO: nastav text prvku "output" na "Ahoj Brython!"
    # document["output"].text = ...
    document["output"].text = "Ahoj Brython!"
    pass

# document["btn_click"].bind("click", pozdrav)

# KROK 2 – počítadlo klikov

pocet_klikov = 0

def pocitaj_kliky(ev):
    global pocet_klikov
    # TODO:
    # 1. zvýš pocet_klikov o 1
    # 2. vypíš do output napr. "Klikol si X-krát"
    pocet_klikov += 1
    document["output"].text = "Klikol si " + str(pocet_klikov) + " krát."
    pass

# na začiatku nechávame zakomentované, použijeme až neskôr
document["btn_click"].bind("click", pocitaj_kliky)

# KROK 3 – odpočítavanie

zvysok = 100        # začíname od 5
id_timer = None   # sem si uložíme id časovača

def tik():
    global zvysok, id_timer
    # TODO:
    # 1. vypíš hodnotu zvysok do output
    # 2. zníž zvysok o 1
    # 3. keď zvysok klesne pod 0, zastav timer.stop(id_timer)
    document["output"].text = str(zvysok)
    zvysok -= 1
    if zvysok < 0:
        timer.clear_interval(id_timer)
        document["output"].text = str("done")
    pass

def start_odpoctu(ev):
    global zvysok, id_timer
    zvysok = 100
    # TODO: nastav id_timer = timer.set_interval(tik, 1000)
    id_timer = timer.set_interval(tik, 100)
    pass

document["btn_start"].bind("click", start_odpoctu)
