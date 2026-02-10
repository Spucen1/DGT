from browser import document, html, window
from browser.local_storage import storage
import json

if "tasks" in storage:
    try:
        tasks = json.loads(storage["tasks"])
    except:
        tasks = []
else:
    tasks = []

if "old_tasks" in storage:
    try:
        old_tasks = json.loads(storage["old_tasks"])
    except:
        old_tasks = []
else:
    old_tasks = []

def list_tasks():
    my_div = document["tasks"]
    my_div.clear()
    tab = html.TABLE(Class="task-table")
    header = html.TR([html.TH("Task"), html.TH("Status"), html.TH("Priority"), html.TH("Remove")])
    tab <= header

    for task in tasks:
        row = html.TR()
        row <= html.TD(task["title"])
        toggle_status = html.BUTTON("✔️" if task["status"] else "✖️")
        row.style["background-color"] = "gray" if task["status"] else ""
        toggle_status.bind("click", toggle_done)
        row <= html.TD(toggle_status)
        row <= html.TD(task["priority"].capitalize())
        remove_btn = html.BUTTON("🗑️", Class = "remove")
        remove_btn.bind("click", remove_task)
        row <= html.TD(remove_btn)
        tab <= row

    my_div <= tab

def remove_task(ev):
    row = ev.currentTarget.parentElement.parentElement
    if window.confirm("Are you sure you want to delete this task?"):
        title = row.children[0].textContent
        for task in tasks:
            if task["title"] == title:
                tasks.remove(task)
                break
        row.remove()
        old_tasks = json.loads(storage["tasks"])
        storage["old_tasks"] = json.dumps(old_tasks)
        storage["tasks"] = json.dumps(tasks)
        #list_tasks()

def toggle_done(ev):
    btn = ev.target
    row = btn.parentElement.parentElement
    title = row.children[0].textContent
    for task in tasks:
        if task["title"] == title:
            task["status"] = not task["status"]
            break
    list_tasks()
    old_tasks = json.loads(storage["tasks"])
    storage["old_tasks"] = json.dumps(old_tasks)
    storage["tasks"] = json.dumps(tasks)

def add_task(ev):
    title = document["title"].value
    priority = document["priority"].value
    if title:
        tasks.append({"title": title, "status": False, "priority": priority})
        document["title"].value = ""
        list_tasks()
        old_tasks = json.loads(storage["tasks"])
        storage["old_tasks"] = json.dumps(old_tasks)
        storage["tasks"] = json.dumps(tasks)

def CMhandler(ev):
    if ev.target.tagName == "INPUT":
        return
    ev.preventDefault()

def bck_fn(ev):
    global tasks
    tasks = json.loads(storage["old_tasks"])
    storage["tasks"] = json.dumps(tasks)
    list_tasks()

def bck_dbl_fn(ev):
    global tasks
    old_tasks = json.loads(storage["tasks"])
    storage["old_tasks"] = json.dumps(old_tasks)
    del storage["tasks"]
    tasks = []
    storage["tasks"] = json.dumps(tasks)
    list_tasks()

def resize_print(ev):
    print("widthh:", window.innerWidth, "height:", window.innerHeight)

def new_on_enter(ev):
    if ev.key == "Escape":
        document["title"].value = ""
        ev.preventDefault()
    elif ev.key == "Enter":
        #add_task(ev)
        ev.preventDefault()
        document["add-task"].dispatchEvent(window.Event.new("click"))


document["add-task"].bind("click", add_task)
document["bck_btn"].bind("click", bck_fn)
document["bck_btn"].bind("dblclick", bck_dbl_fn)
document.bind("contextmenu", CMhandler)
window.bind("resize", resize_print)
document["title"].bind("keydown", new_on_enter)

list_tasks()