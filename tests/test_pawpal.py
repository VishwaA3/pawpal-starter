from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_completion():
    task = Task("Walk", 20, "high")
    task.mark_complete()
    assert task.completed == True


def test_add_task_to_pet():
    pet = Pet("Mochi", "dog")
    task = Task("Feed", 10, "medium")

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_sorting_tasks():
    t1 = Task("Low task", 10, "low")
    t2 = Task("High task", 20, "high")
    t3 = Task("Medium task", 15, "medium")

    scheduler = Scheduler()
    sorted_tasks = scheduler.sort_tasks([t1, t2, t3])

    assert sorted_tasks[0].priority == "high"
    assert sorted_tasks[1].priority == "medium"
    assert sorted_tasks[2].priority == "low"