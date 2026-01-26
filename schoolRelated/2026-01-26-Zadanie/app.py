from browser import document, html, window

# VERZIA: A
# Hotovo: Hotovo prepína klávesou K (keď je položka vybraná).
# Poradie: Nové položky idú NAVRCH.
# Odstránenie: Odstránenie funguje len pri kliknutí so stlačeným Shift.
STORAGE_KEY = "todo_y2_A"

# Stav aplikácie
items = []  # list[dict]: {"id": int, "text": str, "done": bool}
selected_id = None
active_filter = "all"  # "all" | "active" | "done"
audit = []  # posledné akcie (string)
shift = False

def render():
    """Zobrazí zoznam podľa filtra + aktualizuje počítadlá a audit."""
    lst = document["list"]
    lst.clear()

    visible = items
    if active_filter == "active":
        visible = [x for x in items if not x["done"]]
    elif active_filter == "done":
        visible = [x for x in items if x["done"]]

    for it in visible:
        li = html.LI()
        li.attrs["data-id"] = str(it["id"])

        # --- TODO: vyznačenie selected + done (class) ---
        # tip: li.class_name = "..."
        # ----------------------------------------------

        

        # Text
        txt = html.SPAN(it["text"])
        txt.attrs["data-role"] = "text"

        # Ovládacie prvky
        btn_done = html.BUTTON("Hotovo")
        btn_done.attrs["data-role"] = "done"

        btn_del = html.BUTTON("X")
        btn_del.attrs["data-role"] = "del"

        if it["done"] == True:
            li.class_name = "hotovo"
            btn_done.class_name = "hotovobtn"
            btn_del.class_name = "hotovobtn"
        else:
            li.class_name = ""
            btn_done.class_name = ""
            btn_del.class_name = ""

        li <= txt + " " + btn_done + " " + btn_del
        lst <= li

    update_counts()
    render_audit()

def update_counts():
    total = len(items)
    done = sum(1 for x in items if x["done"])
    document["counts"].text = f"{total} spolu • {done} hotové"

def push_audit(msg: str):
    audit.insert(0, msg)
    del audit[3:]

def render_audit():
    document["audit"].text = " | ".join(audit) if audit else "—"

def save():
    """TODO (Hodina 2): ulož items do localStorage ako JSON."""
    pass

def load():
    """TODO (Hodina 2): načítaj items z localStorage a nastav selected_id = None."""
    pass

def add_item(text: str):
    global items, selected_id
    text = text.strip()
    if len(text) < 1:
        return

    new_id = (max([x["id"] for x in items]) + 1) if items else 1
    obj = {"id": new_id, "text": text, "done": False}

    # --- TODO: poradie pridania podľa verzie (navrch/naspodok) ---
    # items.insert(0, obj) alebo items.append(obj)
    # ------------------------------------------------------------

    items.append(obj)

    selected_id = new_id
    push_audit("+Pridané")
    render()
    save()

def toggle_done(item_id: int):
    for x in items:
        if x["id"] == item_id:
            x["done"] = not x["done"]
            push_audit("✓Hotovo" if x["done"] else "↩︎Späť")
            break
    render()
    save()

def delete_item(item_id: int):
    global items, selected_id
    items = [x for x in items if x["id"] != item_id]
    if selected_id == item_id:
        selected_id = None
    push_audit("−Odstránené")
    render()
    save()

def set_filter(name: str):
    global active_filter
    active_filter = name
    document["filter_lbl"].text = "All" if name == "all" else ("Active" if name == "active" else "Done")
    render()

def on_add_click(ev):
    add_item(document["todo_in"].value)
    document["todo_in"].value = ""
    document["todo_in"].focus()

def on_input_key(ev):
    # Enter pridá položku
    if ev.key == "Enter":
        on_add_click(ev)

def on_list_click(ev):
    """Delegovanie klikov v zozname: zistí data-role a data-id."""
    global selected_id

    target = ev.target
    role = target.attrs.get("data-role")
    # nájdi LI rodiča
    li = target
    while li and li.tagName != "LI":
        li = li.parent
    if not li:
        return
    item_id = int(li.attrs.get("data-id"))

    # vždy označ vybranú položku
    selected_id = item_id

    # --- TODO: pravidlá podľa verzie ---
    # 1) hotovo: podľa role ("done") alebo klik na text alebo dvojklik atď.
    # 2) odstránenie: podľa role ("del") + pravidlo (Shift/Alt/Ctrl/dvojklik/confirm/selected)
    # -----------------------------------
    if ev.target.textContent == "Hotovo":
        for i in items:
            if i["id"] == item_id:
                if i["done"] == False:
                    i["done"] = True
                elif i["done"] == True:
                    i["done"] = False  
    elif ev.target.tagName == "BUTTON":
        delete_item(item_id)
                                                     
    render()

def on_keydown(ev):
    """TODO: podľa verzie – hotovo cez klávesu (K/H/Space...) pre selected_id."""
    if ev.key == "Enter":
        on_add_click()
    

def wire_events():
    document["add_btn"].bind("click", on_add_click)
    document["todo_in"].bind("keydown", on_input_key)
    document["list"].bind("click", on_list_click)
    document.bind("keydown", on_keydown)

    document["f_all"].bind("click", lambda ev: set_filter("all"))
    document["f_active"].bind("click", lambda ev: set_filter("active"))
    document["f_done"].bind("click", lambda ev: set_filter("done"))

def main():
    wire_events()
    load()  # v hodine 1 môže byť prázdne
    render()

main()
