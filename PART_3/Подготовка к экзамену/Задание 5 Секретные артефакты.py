# 1. Создайте абстрактный класс `Artifact` с абстрактным методом `activate`.
# 2. Создайте два класса:
#     - `HealingArtifact`, метод `activate` возвращает: "Восстановлено 50 здоровья".
#     - `DamageArtifact`, метод `activate` возвращает: "Нанесено 30 урона врагу".
# 3. Создайте объекты и вызовите метод `activate`.

from abc import ABC, abstractmethod

class Artifact(ABC):
    @abstractmethod
    def activate(self):
        pass

class HealingArtifact(Artifact):
    def activate(self):
        return "Восстановлено 50 здоровья"

class DamageArtifact(Artifact):
    def activate(self):
        return "Нанесено 30 урона врагу"
