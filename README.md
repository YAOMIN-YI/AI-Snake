貪食蛇 AI 專案

《專案簡介》

本專案以 Python 為主軸，結合 pygame 遊戲視覺化、gym 強化學習環境，以及 stable-baselines3 深度強化學習套件，
實現一個能自動訓練、持續優化策略的貪食蛇 AI。AI 透過 DQN（Deep Q-Network）模型學習遊戲規則，並持續提升分數，
展現強化學習於經典遊戲中的應用與成效。

專案僅需三個主要 Python 檔案即可完成完整流程，結構簡潔，方便理解及後續擴充。

《技術棧與依賴套件》

Python 3.x

pygame（遊戲顯示）

gym（強化學習環境）

numpy（數值運算）

stable-baselines3（強化學習演算法）

shimmy（Gym 兼容性支援）

【專案結構與檔案說明】

snake_pygame_gym.py

【實作貪食蛇遊戲邏輯，包裝為 Gym 環境，支援即時畫面顯示與分數統計。】

train_dqn_snake.py

【用於訓練 DQN 模型，訓練完成後自動儲存權重，可重複訓練累積經驗。】

watch_trained_snake.py

【載入已訓練模型，讓 AI 自動遊玩並即時顯示遊戲分數與表現。】

《安裝步驟》

建議使用 Anaconda 管理 Python 虛擬環境。

建立新環境並安裝 Python 3.x。

安裝必要套件（於終端機或 Anaconda Prompt 輸入以下安裝套件，並請手動安裝所需全部套件）：

bash

pip install pygame gym numpy stable-baselines3 shimmy 

《使用說明》

1. 訓練 AI 模型
在終端機輸入以下指令開始訓練 DQN 模型，訓練結果將自動保存，可多次累積訓練：

bash

python train_dqn_snake.py

2. 測試已訓練模型
輸入以下指令觀察 AI 自動遊玩貪食蛇遊戲及分數表現：

bash

python watch_trained_snake.py
