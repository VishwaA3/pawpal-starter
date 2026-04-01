from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    title: str
    duration: int
    priority: str
    completed: bool = False

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def get_tasks(self):
        pass


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass

    def get_all_tasks(self):
        pass


class Scheduler:

    def generate_schedule(self, owner: Owner):
        pass

    def sort_tasks(self, tasks: List[Task]):
        pass