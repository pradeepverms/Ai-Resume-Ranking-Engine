# models.py
from dataclasses import dataclass


@dataclass
class Job:
    id: int
    title: str
    skills: str
    description: str
    experience_required: int


@dataclass
class Resume:
    id: int
    name: str
    skills: str
    experience: int
    text: str