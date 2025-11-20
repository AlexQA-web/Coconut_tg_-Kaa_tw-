# - Задание
# 2: Расширение методов с super()
# Расширяем функциональность родительских методов

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.tasks_completed = 0

    def complete_task(self, task_name, points):
        self.tasks_completed += 1
        print(f"{self.name} выполнил задание '{task_name}' за {points} баллов")
        return points


class HonorStudent(Student):
    def __init__(self, name, grade, scholarship):
        super().__init__(name, grade)
        self.scholarship = scholarship
        self.bonus_points = 0

    def complete_task(self, task_name, points):
        base_points = super().complete_task(task_name, points)
        bonus = int(base_points * 0.1)
        self.bonus_points += bonus
        total_points = base_points + bonus

        print(f"Отличник получает бонус: +{bonus} баллов (всего: {total_points})")
        return total_points


class TeamLeader(HonorStudent):
    def __init__(self, name, grade, scholarship, team_size):
        super().__init__(name, grade, scholarship)
        self.team_size = team_size
        self.team_points = 0

    def complete_task(self, task_name, points):
        # TODO: Вызови родительский метод (включает базовое выполнение + бонус отличника)
        personal_points = super().complete_task(task_name, points)
        # TODO: Добавь командные баллы (5 баллов за каждого члена команды)
        team_bonus = self.team_size * 5
        self.team_points += team_bonus
        total_with_team = personal_points + team_bonus

        print(f"Лидер команды получает командный бонус: +{team_bonus} баллов")
        print(f"Итого с командным бонусом: {total_with_team} баллов")
        return total_with_team


# Тестирование:
team_leader = TeamLeader("Анна", 11, 5000, 4)
result = team_leader.complete_task("Математика", 100)

# Ожидаемый результат:
# Анна выполнил задание 'Математика' за 100 баллов
# Отличник получает бонус: +10 баллов (всего: 110)
# Лидер команды получает командный бонус: +20 баллов
# Итого с командным бонусом: 130 баллов

print(f"Выполнено заданий: {team_leader.tasks_completed}")  # Должно быть 1
print(f"Бонусных баллов отличника: {team_leader.bonus_points}")  # Должно быть 10
print(f"Командных баллов: {team_leader.team_points}")  # Должно быть 20