from browser import document, html

# ===== Checkpoint A: načítaj prvky =====
# TODO: doplň načítanie prvkov z HTML podľa id
inp = document["inp_item"]
btn_add = document["btn_add"]
btn_clear = document["btn_clear"]
out = document["out"]

# ===== Checkpoint B: stav aplikácie =====
# TODO: vytvor zoznam položiek
items = []

# ===== Checkpoint D: render (vykreslenie) =====
def render():
    if items == []:
        out.clear()
        out.text("zoznam je prázdny")
    else:
        out.clear()
        itemList = html.UL()
        for i in items:
            listItem = html.LI(i)
            itemList <= listItem
        out <= itemList
    # TODO: vypíš items do out (ako <ul><li>...)
    # TIP: ak je zoznam prázdny, ukáž text "Zoznam je prázdny."
    


# ===== Checkpoint C: pridanie položky =====
def add_item(ev):
    global items
    # TODO: prečítaj text z inputu, ošetri prázdny reťazec (.strip())
    # TODO: pridaj do items, vyčisti input, zavolaj render()
    polozka = inp.value.strip()
    if len(polozka) > 0:
        items.append(polozka)
        inp.value = ""
        render()
    


# ===== Checkpoint E (Support): vymaž všetko =====
def clear_all(ev):
    global items
    # TODO: vymaž items a zavolaj render()
    items = []
    render()


# ===== Naviazanie eventov =====
# TODO: bind na klik
btn_add.bind("click", add_item)
btn_clear.bind("click", clear_all)

# Voliteľne: render pri štarte
render()
