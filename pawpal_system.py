from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    """Represents a single pet care task."""
    title: str
    duration: int
    priority: str
    completed: bool = False

    def mark_complete(self):
        """Mark task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Represents a pet and its list of tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
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


class Scheduler:
    """Handles generating and sorting schedules for a pet owner."""

    def generate_schedule(self, owner: Owner):
        """Return a sorted list of all tasks for the owner."""
        tasks = owner.get_all_tasks()
        sorted_tasks = self.sort_tasks(tasks)
        return sorted_tasks

    def sort_tasks(self, tasks: List[Task]):
        """Sort tasks by priority (high > medium > low)."""
        priority_order = {"high": 3, "medium": 2, "low": 1}
        return sorted(tasks, key=lambda task: priority_order[task.priority], reverse=True)