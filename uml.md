classDiagram

class Owner {
  - name: str
  - pets: list
  + add_pet(pet)
  + get_all_tasks()
}

class Pet {
  - name: str
  - species: str
  - tasks: list
  + add_task(task)
  + get_tasks()
}

class Task {
  - title: str
  - duration: int
  - priority: str
  - completed: bool
  + mark_complete()
}

class Scheduler {
  + generate_schedule(owner)
  + sort_tasks(tasks)
}

Owner --> Pet
Pet --> Task
Scheduler --> Owner