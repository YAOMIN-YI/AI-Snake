import gym
from gym import spaces
import numpy as np
import pygame
import random

class SnakeGame:
    def __init__(self, grid_size=10, block_size=30):
        self.grid_size = grid_size
        self.block_size = block_size
        pygame.init()
        self.screen = pygame.display.set_mode((grid_size * block_size, grid_size * block_size))
        pygame.display.set_caption('Snake Gym')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.high_score = 0  # 新增最高分

        self.reset()

    def reset(self):
        # 死亡時更新最高分
        if hasattr(self, "score") and self.score > self.high_score:
            self.high_score = self.score
        self.snake = [(self.grid_size // 2, self.grid_size // 2)]
        self.direction = random.choice([0, 1, 2, 3])
        self.spawn_food()
        self.done = False
        self.score = 0

    def spawn_food(self):
        while True:
            self.food = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
            if self.food not in self.snake:
                break

    def step(self, action):
        if abs(action - self.direction) != 1:
            self.direction = action
        head_x, head_y = self.snake[0]
        if self.direction == 0: head_y -= 1
        elif self.direction == 1: head_y += 1
        elif self.direction == 2: head_x -= 1
        elif self.direction == 3: head_x += 1
        new_head = (head_x, head_y)
        
        if (head_x < 0 or head_x >= self.grid_size or head_y < 0 or head_y >= self.grid_size or new_head in self.snake):
            self.done = True
            return -1, True
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.spawn_food()
            return 1, False
        else:
            self.snake.pop()
            return -0.01, False

    def render(self):
        # 處理pygame事件，防止卡住
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.screen.fill((0, 0, 0))
        for x, y in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
        fx, fy = self.food
        pygame.draw.rect(self.screen, (255, 0, 0), (fx * self.block_size, fy * self.block_size, self.block_size, self.block_size))

        # 顯示當前分數和最高分
        score_surf = self.font.render(f"Score: {self.score}  High: {self.high_score}", True, (255, 255, 255))
        self.screen.blit(score_surf, (10, 10))

        pygame.display.flip()
        self.clock.tick(10)

    def close(self):
        pygame.quit()

class SnakeGymEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    def __init__(self):
        super(SnakeGymEnv, self).__init__()
        self.game = SnakeGame()
        self.action_space = spaces.Discrete(4)
        low = np.zeros(4)
        high = np.array([self.game.grid_size - 1] * 4)
        self.observation_space = spaces.Box(low, high, dtype=np.int32)
        self.reset()

    def reset(self):
        self.game.reset()
        return self._get_obs()

    def step(self, action):
        reward, done = self.game.step(action)
        obs = self._get_obs()
        return obs, reward, done, {}

    def render(self, mode='human'):
        self.game.render()

    def close(self):
        self.game.close()

    def _get_obs(self):
        head_x, head_y = self.game.snake[0]
        food_x, food_y = self.game.food
        return np.array([head_x, head_y, food_x, food_y], dtype=np.int32)

# 測試功能（直接執行本檔案可觀察蛇自動亂走並顯示分數和最高分）
if __name__ == "__main__":
    env = SnakeGymEnv()
    obs = env.reset()
    for _ in range(200):
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        if done:
            print(f"Game Over! 分數: {env.game.score}  最高分: {env.game.high_score}")
            obs = env.reset()
    env.close()
    input("請按Enter關閉視窗...")
