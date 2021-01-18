from datetime import datetime

todo_time = "12:35"
formated_time = datetime.strptime(todo_time, "%H:%M")
print(formated_time)