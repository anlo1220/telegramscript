from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 設定bot的token和群組ID
TOKEN = 'TOKEN'  # 將'YOUR_BOT_TOKEN'替換成從BotFather獲得的token
GROUP_ID = '-GROUP_ID'  # 將'YOUR_GROUP_CHAT_ID'替換成目標群組的ID

def start(update: Update, context: CallbackContext):
    update.message.reply_text('您好！請發送一個影片，我將把它轉發到群組。')

def handle_video(update: Update, context: CallbackContext):
    try:
        # 獲取影片文件
        video_file = update.message.video

        # 使用預設的文件名
        file_name = '未命名影片'

        # 轉發影片到群組
        context.bot.send_video(chat_id=GROUP_ID, video=video_file.file_id, caption=f"文件名: {file_name}")
        update.message.reply_text('您的影片已經轉發到群組！')
    except Exception as e:
        print(f"傳送影片時出現錯誤: {e}")
        update.message.reply_text('傳送影片失敗。請檢查機器人是否為群組成員並具備正確的權限。錯誤: ' + str(e))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # 註冊命令和消息處理器
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.video, handle_video))

    # 開始機器人
    updater.start_polling()

    # 在控制台打印啟動成功訊息
    print("機器人已成功啟動！")

    # 可選：向管理群組發送機器人已啟動的訊息
    # updater.bot.send_message(chat_id=GROUP_ID, text="機器人已成功啟動！")

    updater.idle()

if __name__ == '__main__':
    main()
