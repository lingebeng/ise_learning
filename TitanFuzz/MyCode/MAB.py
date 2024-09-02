import random

class Arm:
    def __init__(self, win_rate):
        self.win_rate = win_rate
        self.total_reward = 0
        self.num_pulls = 0

    def pull(self):
        # 根据赢率生成奖励
        reward = 1 if random.random() < self.win_rate else 0
        self.total_reward += reward
        self.num_pulls += 1
        return reward

    def average_reward(self):
        return self.total_reward / self.num_pulls if self.num_pulls > 0 else 0

class EpsilonGreedyPolicy:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def choose_arm(self, arms):
        if random.random() < self.epsilon:
            # 探索：随机选择一个手臂
            return random.choice(arms)
        else:
            # 利用：选择平均奖励最高的手臂
            best_arm = max(arms, key=lambda arm: arm.average_reward())
            return best_arm

# 创建一些手臂
arms = [Arm(0.1), Arm(0.2), Arm(0.3), Arm(0.4)]

# 创建策略
policy = EpsilonGreedyPolicy(epsilon=0.1)

# 运行实验
num_rounds = 1000
total_reward = 0

for _ in range(num_rounds):
    chosen_arm = policy.choose_arm(arms)
    reward = chosen_arm.pull()
    total_reward += reward

print(f"Total reward over {num_rounds} rounds: {total_reward}")
