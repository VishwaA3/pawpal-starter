from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import datetime, timedelta

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

def test_recurring_task():
    today = datetime(2026, 3, 31, 8, 0)
    task = Task("Daily Walk", 20, "high", frequency="daily", due_date=today)
    new_task = task.mark_complete()
    
    assert task.completed is True
    assert new_task.due_date == today + timedelta(days=1)

def test_conflict_detection():
    pet = Pet("Mochi", "dog")
    t1 = Task("Walk", 20, "high", due_date=datetime(2026,3,31,8,0))
    t2 = Task("Feed", 10, "medium", due_date=datetime(2026,3,31,8,0))
    pet.add_task(t1)
    pet.add_task(t2)

    owner = Owner("Jordan", pets=[pet])
    scheduler = Scheduler()
    tasks, conflicts = scheduler.generate_schedule(owner)
    
    assert len(conflicts) == 1
    assert "Conflict" in conflicts[0]

def test_filtering_tasks():
    pet = Pet("Mochi", "dog")
    t1 = Task("Walk", 20, "high")
    t2 = Task("Feed", 10, "medium", completed=True)
    pet.add_task(t1)
    pet.add_task(t2)
    
    owner = Owner("Jordan", pets=[pet])
    scheduler = Scheduler()
    all_tasks = owner.get_all_tasks()
    
    # filter completed tasks
    completed_tasks = scheduler.filter_tasks(all_tasks, completed=True)
    assert len(completed_tasks) == 1
    assert completed_tasks[0].title == "Feed"
    
    # filter by pet
    pet_tasks = scheduler.filter_tasks(all_tasks, pet_name="Mochi")
    assert len(pet_tasks) == 2

def test_empty_pet_tasks():
    pet = Pet("Empty", "cat")
    owner = Owner("Jordan", pets=[pet])
    scheduler = Scheduler()
    tasks, conflicts = scheduler.generate_schedule(owner)
    
    assert tasks == []
    assert conflicts == []