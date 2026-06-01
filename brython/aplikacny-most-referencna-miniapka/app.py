from browser import document, html
from browser.local_storage import storage
import json

# Referenčná miniappka pre Aplikačný most.
# Nové položky idú navrch. Hotovo sa prepína tlačidlom alebo klávesou K.
# Odstránenie má dve cesty: Shift + klik na X ukazuje desktopový modifikátor; tlačidlo Odstrániť vybranú funguje aj na dotyku.
STORAGE_KEY = "aplikacny_most_todo_pwa"


# Stav aplikácie
items = []
selected_id = None
active_filter = "all"
audit = []


# Zobrazenie

def render():
    lst = document["list"]
    lst.clear()

    visible = items
    if active_filter == "active":
        visible = [item for item in items if not item["done"]]
    elif active_filter == "done":
        visible = [item for item in items if item["done"]]

    for item in visible:
        li = html.LI()
        li.attrs["data-id"] = str(item["id"])

        classes = []
        if item["id"] == selected_id:
            classes.append("selected")
        if item["done"]:
            classes.append("done")
        if classes:
            li.class_name = " ".join(classes)

        text = html.SPAN(item["text"])
        text.attrs["data-role"] = "text"

        done_button = html.BUTTON("Hotovo")
        done_button.attrs["type"] = "button"
        done_button.attrs["data-role"] = "done"

        delete_button = html.BUTTON("X")
        delete_button.attrs["type"] = "button"
        delete_button.attrs["data-role"] = "del"
        delete_button.attrs["title"] = "Odstrániť cez Shift + klik"

        li <= text + " " + done_button + " " + delete_button
        lst <= li

    update_counts()
    render_audit()
    update_selected_actions()


def update_counts():
    total = len(items)
    done = sum(1 for item in items if item["done"])
    document["counts"].text = f"{total} spolu • {done} hotové"


def push_audit(message):
    audit.insert(0, message)
    del audit[3:]


def render_audit():
    document["audit"].text = " | ".join(audit) if audit else "—"


def update_selected_actions():
    document["delete_selected_btn"].disabled = selected_id is None


# Ukladanie

def save():
    storage[STORAGE_KEY] = json.dumps(items, ensure_ascii=False)


def load():
    global items, selected_id

    selected_id = None
    items = []

    data = storage.get(STORAGE_KEY)
    if not data:
        return

    try:
        loaded = json.loads(data)
    except (TypeError, ValueError):
        return

    if not isinstance(loaded, list):
        return

    used_ids = set()
    for raw_item in loaded:
        if not isinstance(raw_item, dict):
            continue

        text = str(raw_item.get("text", "")).strip()
        item_id = raw_item.get("id")
        if not text or not isinstance(item_id, int) or item_id < 1 or item_id in used_ids:
            continue

        used_ids.add(item_id)
        items.append({
            "id": item_id,
            "text": text,
            "done": bool(raw_item.get("done", False)),
        })


# Zmeny dát

def add_item(text):
    global selected_id

    text = text.strip()
    if not text:
        return

    new_id = max((item["id"] for item in items), default=0) + 1
    item = {"id": new_id, "text": text, "done": False}

    items.insert(0, item)
    selected_id = new_id
    push_audit("+ Pridané")
    render()
    save()


def toggle_done(item_id):
    for item in items:
        if item["id"] == item_id:
            item["done"] = not item["done"]
            push_audit("✓ Hotovo" if item["done"] else "↩ Späť")
            render()
            save()
            return


def delete_item(item_id):
    global items, selected_id

    before = len(items)
    items = [item for item in items if item["id"] != item_id]
    if len(items) == before:
        return

    if selected_id == item_id:
        selected_id = None

    push_audit("− Odstránené")
    render()
    save()


def set_filter(name):
    global active_filter, selected_id

    if name not in ("all", "active", "done"):
        return

    active_filter = name
    selected_id = None
    labels = {
        "all": "Všetky",
        "active": "Aktívne",
        "done": "Hotové",
    }
    document["filter_lbl"].text = labels[name]
    render()


# Udalosti

def on_add_click(ev):
    add_item(document["todo_in"].value)
    document["todo_in"].value = ""
    document["todo_in"].focus()


def on_input_key(ev):
    if ev.key == "Enter":
        on_add_click(ev)


def find_parent_li(element):
    current = element
    while current and getattr(current, "tagName", "") != "LI":
        current = current.parent
    return current


def on_list_click(ev):
    global selected_id

    target = ev.target
    role = target.attrs.get("data-role")
    li = find_parent_li(target)
    if not li:
        return

    item_id = int(li.attrs["data-id"])
    selected_id = item_id

    if role == "done":
        toggle_done(item_id)
    elif role == "del" and ev.shiftKey:
        delete_item(item_id)
    else:
        render()


def on_delete_selected_click(ev):
    if selected_id is not None:
        delete_item(selected_id)


def on_keydown(ev):
    target_tag = getattr(ev.target, "tagName", "")
    if target_tag in ("INPUT", "TEXTAREA"):
        return

    if selected_id is not None and ev.key.lower() == "k":
        toggle_done(selected_id)


def wire_events():
    document["add_btn"].bind("click", on_add_click)
    document["todo_in"].bind("keydown", on_input_key)
    document["list"].bind("click", on_list_click)
    document["delete_selected_btn"].bind("click", on_delete_selected_click)
    document.bind("keydown", on_keydown)

    document["f_all"].bind("click", lambda ev: set_filter("all"))
    document["f_active"].bind("click", lambda ev: set_filter("active"))
    document["f_done"].bind("click", lambda ev: set_filter("done"))


def main():
    wire_events()
    load()
    render()


main()
