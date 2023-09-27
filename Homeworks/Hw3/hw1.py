"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without -
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes
you want.
"""

import datetime

class DeadlineError(Exception):
    pass

class Homework:
    def __init__(self, homework_text, deadline: datetime.timedelta.days):
        self.homework_text = homework_text
        self.deadline = deadline
        self.creation_date = datetime.datetime.now()

    def deadline_has_passed(self) -> bool:
        if self.creation_date.day + self.deadline < self.creation_date.day:
            return True
        else:
            return False


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: Homework, solution_text: str):
        if homework.deadline_has_passed():
            raise DeadlineError("You are late")
        result = Result(homework, solution_text)
        result.author = self
        return result


class Result:
    def __init__(self, homework: Homework, solution: str):
        self.homework = homework
        self.solution = solution


class Teacher:
    homework_done = {}

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @classmethod
    def create_homework(cls, homework_task: str, time_for_task):
        return Homework(homework_task, time_for_task)

    @classmethod
    def check_homework(cls, result: Result):
        if result.homework in cls.homework_done:
            return True
        else:
            if len(result.solution) > 5:
                if cls.homework_done.get(result.homework) is None:
                    cls.homework_done[result.homework] = set()
                    cls.homework_done[result.homework].add(result)
                else:
                    cls.homework_done[result.homework].add(result)
                return True
            else:
                cls.homework_done[result.homework] = set()
                return False

    @classmethod
    def reset_results(cls):
        cls.homework_done.clear()


