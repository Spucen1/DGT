from browser import document, html, window

tasks = [
    {"title": "Homework", "status": False, "priority": "low"},
    {"title": "Feed cat", "status": False, "priority": "medium"},
    {"title": "Buy groceries", "status": False, "priority": "medium"},
]

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

def add_task(ev):
    title = document["title"].value
    priority = document["priority"].value
    if title:
        tasks.append({"title": title, "status": False, "priority": priority})
        document["title"].value = ""
        list_tasks()

document["add-task"].bind("click", add_task)

list_tasks()