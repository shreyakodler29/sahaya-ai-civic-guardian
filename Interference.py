from environment import SahayaEnv
from tasks.integrity_scoring import compute_integrity

env = SahayaEnv()

state = env.reset()

for _ in range(5):
    action = "repair"
    state, reward, done, _ = env.step(action)
    print("State:", state)
    print("Reward:", reward)

score = compute_integrity(
    state["damage"],
    state["maintenance"],
    state["feedback"]
)

print("Civic Integrity Score:", score)
