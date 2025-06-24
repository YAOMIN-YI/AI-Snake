import os
import time
from stable_baselines3 import DQN
from snake_pygame_gym import SnakeGymEnv

# 建立環境
env = SnakeGymEnv()

# 自動判斷是否已有模型，決定是新訓練還是接續訓練
if os.path.exists("dqn_snake.zip"):
    model = DQN.load("dqn_snake", env=env)
    print("載入已存在的模型，繼續訓練！")
else:
    model = DQN("MlpPolicy", env, verbose=1)
    print("建立新模型，開始訓練！")

# 設定這次要繼續訓練多少步
model.learn(total_timesteps=100000)
model.save("dqn_snake")
print("模型已保存為 dqn_snake.zip！")

# 訓練結束後馬上觀察AI自動玩蛇
print("AI開始自動玩蛇（可觀察成果）...")
obs = env.reset()
for _ in range(1000): #可以改成更長或更短
    env.render()
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    time.sleep(0.05)  # 控制動畫速度，想更快可改小
    if done:
        obs = env.reset()
env.close()

input("請按Enter關閉視窗...")
