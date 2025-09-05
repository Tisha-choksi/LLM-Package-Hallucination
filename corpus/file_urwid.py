import urwid

tasks = []

def add_task(button, user_data):
    tasks.append(user_data.get_edit_text())
    update_list()

def update_list():
    list_content = [urwid.Text(task) for task in tasks]
    list_widget = urwid.ListBox(urwid.SimpleFocusListWalker(list_content))
    urwid.MainLoop(list_widget).run()

if __name__ == "__main__":
    input_widget = urwid.Edit("Enter a task: ")
    done_button = urwid.Button("Add Task", on_press=add_task, user_data=input_widget)
    main_widget = urwid.Pile([input_widget, done_button])
    urwid.MainLoop(main_widget).run()