import os

# Удалили конфиг и все, что связано с вводом данных.
def run():
    from method.method import SteamGift as steamGif

    # Логотип
    for index in range(4):
        print("Logo", index)  # Вывод логотипа (заменил clientLog.log на простое print для демонстрации)
    
    print("\nEnjoy using our product!")
    print("Created by: github.com/PalmaLuv | palmaluv.live\nStay tuned for further app updates")
    
    # Заменяем все параметры на значения из переменных окружения.
    cookie = os.getenv('PHPSESSID_COOKIE', '')  # Получаем cookie из переменной окружения
    log_info = os.getenv('LOG_INFO', 'False') == 'True'  # Логирование (по умолчанию False, если переменная не установлена)
    
    # Параметры по умолчанию
    pinnedGames = True  # Поставить по умолчанию True для "Should the bot enter pinned games?"
    giftTYPE = 'All'  # Поставить по умолчанию 'All' для типа подарков
    minPoin = 60  # Поставить по умолчанию 60 для минимальных баллов

    # Запуск с заданными параметрами
    steamGif(cookie, giftTYPE, pinnedGames, minPoin).start()

if __name__ == '__main__':
    run()
