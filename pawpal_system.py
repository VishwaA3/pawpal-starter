from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta

@dataclass
class Task:
    """Represents a single pet care task."""
    title: str
    duration: int
    priority: str
    completed: bool = False
    frequency: str = None  
    due_date: datetime = None  
    pet_name: str = None  

    def mark_complete(self):
        self.completed = True
        # Auto-create next recurring task
        if self.frequency == "daily":
            return Task(
                title=self.title,
                duration=self.duration,
                priority=self.priority,
                frequency=self.frequency,
                due_date=(self.due_date + timedelta(days=1)) if self.due_date else None,
            )
        elif self.frequency == "weekly":
            return Task(
                title=self.title,
                duration=self.duration,
                priority=self.priority,
                frequency=self.frequency,
                due_date=(self.due_date + timedelta(weeks=1)) if self.due_date else None,
            )
        return None


@dataclass
class Pet:
    """Represents a pet and its list of tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        task.pet_name = self.name 
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Represents a pet owner and their pets."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's pets."""
        self.pets.append(pet)   

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks

@dataclass
class Scheduler:
    """Handles generating and sorting schedules for a pet owner."""

    def generate_schedule(self, owner: Owner):
        tasks = []
        for pet in owner.pets:
            for t in pet.tasks:
                t.pet_name = pet.name  
                tasks.append(t)

        # Sort tasks by priority
        tasks = self.sort_tasks(tasks, by="priority")
        # Detect conflicts
        conflicts = self.detect_conflicts(tasks)

        return tasks, conflicts

    def sort_tasks(self, tasks: List[Task], by: str = "priority"):
        """Sort tasks by priority (high > medium > low) or duration (shortest first)."""
        if by == "priority":
            priority_order = {"high": 0, "medium": 1, "low": 2}
            return sorted(tasks, key=lambda t: priority_order[t.priority])
        elif by == "duration":
            return sorted(tasks, key=lambda t: t.duration)
        else:
            return tasks
        
    def filter_tasks(self, tasks: List[Task], pet_name: str = None, completed: bool = None):
        """Return tasks filtered by pet name and/or completion status."""
        filtered = tasks
        if pet_name:
            filtered = [t for t in filtered if t.pet_name == pet_name]  
        if completed is not None:
            filtered = [t for t in filtered if t.completed == completed]
        return filtered
    
    def detect_conflicts(self, tasks: List[Task]):
        """Return a list of warning messages if two tasks are scheduled at the same time for the same pet."""
        warnings = []
        scheduled_tasks = [t for t in tasks if t.due_date]
        for i, t1 in enumerate(scheduled_tasks):
            for t2 in scheduled_tasks[i+1:]:
                if t1.due_date == t2.due_date:
                    warnings.append(f"Conflict: {t1.title} and {t2.title} scheduled at the same time.")
        return warnings