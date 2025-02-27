import os
import client as clientLog

# Удалили конфиг и все, что связано с вводом данных.
def run():
    from method.method import SteamGift as steamGif
    for index in range(4):
        clientLog.log(clientLog.array_logo[index], "green")
    clientLog.log("\nEnjoy using our product!", "white")
    clientLog.log("Created by: github.com/PalmaLuv | palmaluv.live\nStay tuned for further app updates", "red")
    
    # Заменяем все параметры на значения из переменных окружения.
    cookie = os.getenv('PHPSESSID_COOKIE', '')  # Получаем cookie из переменной окружения
    log_info = os.getenv('LOG_INFO', 'False') == 'True'  # Логирование (по умолчанию False, если переменная не установлена)
    
    # Логирование
    clientLog.createdLogs(log_info)
    
    pinnedGames = True  # Поставить по умолчанию True для "Should the bot enter pinned games?"
    giftTYPE = 'All'  # Поставить по умолчанию 'All' для типа подарков
    minPoin = 60  # Поставить по умолчанию 60 для минимальных баллов

    # Запуск с заданными параметрами
    steamGif(cookie, giftTYPE, pinnedGames, minPoin).start()

if __name__ == '__main__':
    run()
import os
import client as clientLog

# Удалили конфиг и все, что связано с вводом данных.
def run():
        from method.method import SteamGift as steamGif
        for index in range(4):
                    clientLog.log(clientLog.array_logo[index], "green")
                clientLog.log("\nEnjoy using our product!", "white")
    clientLog.log("Created by: github.com/PalmaLuv | palmaluv.live\nStay tuned for further app updates", "red")

    # Заменяем все параметры на значения из переменных окружения.
    cookie = os.getenv('PHPSESSID_COOKIE', '')  # Получаем cookie из переменной окружения
    log_info = os.getenv('LOG_INFO', 'False') == 'True'  # Логирование (по умолчанию False, если переменная не установлена)

    # Логирование
    clientLog.createdLogs(log_info)

    pinnedGames = True  # Поставить по умолчанию True для "Should the bot enter pinned games?"
    giftTYPE = 'All'  # Поставить по умолчанию 'All' для типа подарков
    minPoin = 60  # Поставить по умолчанию 60 для минимальных баллов

    # Запуск с заданными параметрами
    steamGif(cookie, giftTYPE, pinnedGames, minPoin).start()

if __name__ == '__main__':
        run()
