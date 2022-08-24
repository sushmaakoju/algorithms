#task_list = list()
def get_tasks(task_list, n):
    count = 0
    position = 0
    while len(task_list) > 1:
        position = (position + n - 1) % len(task_list)
        print(position)
        task_list.remove(task_list[position])
        if position == len(task_list):
            position = 0
    print(task_list)
    return task_list[0]

get_tasks(["a","b","c","d"], 2)
get_tasks(["a","b","c","d","e"], 3)
