from browser import document, html

tasks = [
    {"title": "Homework", "status": True, "priority": "low"},
    {"title": "Feed cat", "status": True, "priority": "medium"},
    {"title": "Buy groceries", "status": False, "priority": "medium"},
]

def list_tasks():
    my_div = document["tasks"]
    my_div.clear()
    tab = html.TABLE(Class="task-table")
    header = html.TR([html.TH("Task"), html.TH("Status"), html.TH("Priority")])
    tab <= header

    for task in tasks:
        row = html.TR()
        row <= html.TD(task["title"])
        status = "Done" if task["status"] else "Pending"
        row <= html.TD(status)
        row <= html.TD(task["priority"].capitalize())
        tab <= row