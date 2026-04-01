from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner("Vishwa")

# Create pets
dog = Pet("Mochi", "dog")
cat = Pet("Luna", "cat")

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks
t1 = Task("Morning walk", 30, "high")
t2 = Task("Feed Mochi", 10, "medium")
t3 = Task("Clean litter box", 15, "low")

# Assign tasks
dog.add_task(t1)
dog.add_task(t2)
cat.add_task(t3)

# Run scheduler
scheduler = Scheduler()
schedule = scheduler.generate_schedule(owner)

# Print schedule
print("Today's Schedule:")
for task in schedule:
    print(f"- {task.title} ({task.priority}, {task.duration} mins)")