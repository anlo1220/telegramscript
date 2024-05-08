from telethon.sync import TelegramClient

# 填入你的 Telegram API 金鑰
api_id = 'YOUR_API_ID'  # 你的 Telegram API ID
api_hash = 'YOUR_API_HASH'  # 你的 Telegram API 金鑰

# 電話號碼
phone_number = '+phone_number'  # 替換成您的電話號碼，包括國際區號


# 創建一個 TelegramClient 實例
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # 登錄到 Telegram
    await client.start(phone_number)

    # 打開文件並準備寫入頻道資訊
    with open('gettgchanelid.txt', 'w', encoding='utf-8') as file:
        file.write("頻道名稱\t頻道ID\n")  # 寫入檔案表頭
        # 將頻道名稱和對應的 ID 寫入檔案
        async for dialog in client.iter_dialogs():
            if dialog.is_channel:
                file.write(f"{dialog.title}\t{dialog.id}\n")  # 寫入頻道名稱和ID到文件中
    print("頻道名稱和ID已寫入到 gettgchanelid.txt 文件中。")  # 輸出提示資訊

# 運行主函數
with client:
    client.loop.run_until_complete(main())
