import logging
from telethon import TelegramClient, events
from datetime import datetime

# 設置日誌格式
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# 透過 Telegram API 取得的 api_id 和 api_hash
api_id = xxxxxxxxxxx
api_hash = 'xxxxxxxxxxx'

# 你的電話號碼
phone_number = '+xxxxxxxxxx'  # 請更換成您的電話號碼，包含國際區號

# 來源群組 ID 和目標群組 ID
incoming_group_id = -xxxxxxxxxx
outgoing_group_id = -xxxxxxxx
admin_panel_id = -xxxxxx

# 初始化 Telegram 客戶端
client = TelegramClient(phone_number, api_id, api_hash)

# 處理新訊息的事件處理程序
@client.on(events.NewMessage(chats=incoming_group_id))
async def handler(event):
    try:
        # 判斷訊息是否包含媒體
        if event.media:
            # 獲取文件名稱或指示文件名不存在
            file_name = event.message.file.name if event.message.file and event.message.file.name else "未知文件名"
            # 發送媒體文件和文件名稱
            await client.send_file(outgoing_group_id, event.media, caption=event.text)
            await client.send_message(outgoing_group_id, f'{file_name}')
        else:
            # 對於純文本訊息，僅發送文本
            await client.send_message(outgoing_group_id, event.text)
        # 發送操作完成的通知
        completion_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        notification_message = f'已處理{file_name}' if event.media else f'{completion_time} - 已處理純文本訊息'
        logging.info(notification_message)  # 將通知記錄到日誌
        await client.send_message(admin_panel_id, notification_message)  # 將通知發送到管理面板
    except Exception as e:
        error_message = f"處理時發生錯誤: {e}"
        logging.error(error_message)
        # 向管理面板發送錯誤訊息
        await client.send_message(admin_panel_id, error_message)

# 主函式
def main():
    client.start()
    print("客戶端已啟動！")
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
