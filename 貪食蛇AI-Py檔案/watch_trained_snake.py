from stable_baselines3 import DQN
from snake_pygame_gym import SnakeGymEnv
import time

env = SnakeGymEnv()
model = DQN.load("dqn_snake", env=env)

obs = env.reset()
for game in range(100): # 連續玩100局
    score = 0
    done = False
    while not done:
        env.render()
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        time.sleep(0.05)  # 調整動畫速度
        score = env.game.score
    print(f"第 {game+1} 局分數：{score}")
    obs = env.reset()

env.close()
input("請按Enter關閉視窗...")
