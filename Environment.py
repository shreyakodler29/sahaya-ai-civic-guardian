import random

class SahayaEnv:
    def __init__(self):
        self.state_data = None
        self.steps = 0

    def reset(self):
        self.state_data = {
            "damage": random.uniform(0, 1),
            "maintenance": random.uniform(0, 1),
            "feedback": random.uniform(0, 1)
        }
        self.steps = 0
        return self.state_data

    def step(self, action):
        reward = self._reward(action)

        if action == "repair":
            self.state_data["damage"] *= 0.5
            self.state_data["maintenance"] += 0.1
        elif action == "ignore":
            self.state_data["damage"] += 0.1

        self.steps += 1
        done = self.steps > 20

        return self.state_data, reward, done, {}

    def state(self):
        return self.state_data

    def _reward(self, action):
        damage_penalty = -10 * self.state_data["damage"]
        repair_bonus = 20 if action == "repair" else 0
        feedback_bonus = 5 * self.state_data["feedback"]
        return damage_penalty + repair_bonus + feedback_bonus
