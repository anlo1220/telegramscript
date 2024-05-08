## 使用 Telegram 機器人轉發影片

**準備工作**

1. **創建 Telegram 機器人:**

   - 使用 BotFather ([https://core.telegram.org/bots/tutorial](https://core.telegram.org/bots/tutorial)) 創建一個 Telegram 機器人。
   - 記錄機器人令牌。

2. **安裝 Python 庫:**

   - 使用以下命令安裝 `telegram` 庫：

   ```bash
   pip install python-telegram-bot
   ```

   - 安裝指定版本的 python-telegram-bot

     請先卸載當前的庫，然後安裝指定版本的庫：

     ```bash
     pip uninstall python-telegram-bot
     pip install python-telegram-bot==12.8
     ```

3. **獲取目標群組 ID:**

   - 打開目標群組，在地址欄中找到群組 ID。
   - 群組 ID 通常以 `-` 開頭，例如：`-XXXXXXXXXXXXXXX`。

**使用說明**

1. **下載並修改腳本:**

   - 下載並保存腳本 `bottransfervideotochat.py`。
   - 打開腳本並替換以下內容：
     - 將 `TOKEN = 'XXXXXXXXXXX'` 中的 `'XXXXXXXXXXX'` 替換為您的機器人令牌。
     - 將 `GROUP_ID = '-XXXXXXXXXXXXXXX'` 中的 `'-XXXXXXXXXXXXXXX'` 替換為目標群組的 ID。

2. **運行腳本:**

   - 打開終端或命令提示符窗口。
   - 導航到包含腳本的目錄。
   - 使用以下命令運行腳本：

   ```bash
   python bottransfervideotochat.py
   ```

3. **使用機器人:**

   - 在 Telegram 中，向您的機器人發送 `/start` 命令以啟動對話。
   - 向機器人發送影片消息，機器人會自動將影片轉發到目標群組。

**注意事項**

- 確保機器人已添加到目標群組並具有發送消息的權限。
- 機器人將使用默認檔案名“未命名影片”用於轉發的影片。
- 您可以通過修改腳本中的 `handle_video` 函數來更改默認檔案名。
- 如果遇到任何問題，請檢查控制台輸出中的錯誤消息並檢查代碼是否存在任何潛在錯誤。

**附加資訊**

- Telegram 機器人文件: [https://core.telegram.org/](https://core.telegram.org/)
- Python `telegram` 庫文件: [https://docs.telethon.dev/](https://docs.telethon.dev/)
