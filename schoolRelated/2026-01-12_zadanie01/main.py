from browser import document

# TODO: STATUS
# Skús zmeniť text v prvku 'status' tak, aby si videl, že Brython beží.
document["status"].text = "Brython beží!"

# premenná na počítanie pozdravov
count = 0

def greet(ev):
    """Spustí sa po kliknutí na tlačidlo."""
    # TODO: načítaj meno z inputu inp_name, ošetri prázdny vstup a vypíš do prvku out
    # Nápoveda: document["inp_name"].value
    # Nápoveda: document["out"].text = "..."
    if ev.type == "keydown" and ev.key != "Enter":
        return
    meno = document["inp_name"].value
    if meno == "":
        document["out"].text = "Zdaj meno!"
    else:
        global count
        count += 1
        document["out"].text = f"Ahoj, {meno}! x{count}"
    # pass

def reset(ev):
    global count
    count = 0
    document["out"].text = ""
    document["hint"].style.display = "none"
    document["inp_name"].value = ""

def show_tip(ev):
    if document["hint"].style.display == "block":
        document["hint"].style.display = "none"
    else:
        document["hint"].style.display = "block"
    

# TODO: BIND
# Pripoj funkciu greet na kliknutie tlačidla btn_greet.
document["btn_greet"].bind("click", greet)
document.bind("keydown", greet)
document["btn_reset"].bind("click", reset)
document["btn_tip"].bind("click", show_tip)
