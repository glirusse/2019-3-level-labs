import unittest
from lab_1.lr1.crawl import valid, articles

class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.url = 'https://3dnews.ru/'
        self.articles_expected = ['Системная камера Olympus E-M5 Mark III представляет собой мини-E-M1 II', 'Установка аппаратной «закладки» может стоить всего $200', 'Обзор 4K-проектора LG CineBeam HU80KSW: здравствуй, огромный экран!', 'Обзор смартфона OPPO Reno2: вторая попытка войти в высшее общество', 'Xiaomi выпустила массивный 34" изогнутый игровой монитор и 23,8" монитор', 'Откровения первого покупателя Intel Core i9-9900KS: запаса по разгону не ждите', 'Анонсирован электромобиль Volvo XC40 Recharge мощностью 408 л. с.', 'Католическая церковь представила умные чётки eRosary', 'CD Projekt RED опасалась, что в The Witcher 3: Wild Hunt не будет хватать контента', 'Jonsbo TR03: необычный ПК-корпус треугольной формы', 'Раскрыты имена смартфонов Samsung Galaxy A модельного ряда 2021 года', 'Монитор Philips 346B1C оснащён вогнутым экраном UltraWide QHD', 'NZXT вместе с ASRock представила корпус H510i Phantom Gaming Special Edition', 'ASML сообщает о превосходном спросе на EUV-сканеры', 'Xiaomi подтвердила, что через неделю выпустит RedmiBook с процессором AMD', 'Olympus представ��ла системную камеру PEN E-PL10 с матрицей Micro 4:3 и откидным экраном', 'MSI готовит видеокарты GeForce GTX 1660 Super серий Gaming X и Ventus XS', 'Сетевая платформа WIN Enterprises LP-82000 использует Intel Atom Denverton', 'Huawei опасается, что связанные с США сотрудники могут стать источником утечки конфиденциальных данных', 'Tesla получила добро на производство электромобилей в Китае', 'Oppo выпустит двухрежимный смартфон 5G в конце года', 'Малый бизнес теряет $200 тыс. от кибератак и закрывается', 'Сетевой экшен RAN: Lost Islands выйдет в раннем доступе Steam до конца года', 'PlayStation 4 Pro осталась без 4K в The Outer Worlds', 'На отчётной конференции IBM говорила о бизнесе вокруг Red Hat, с остальным всё не слишком хорошо', 'Релиз вампирской RPG Vampire: The Masquerade – Bloodlines 2 отложен', 'Control, наконец, получила обновление с фоторежимом', 'Анимационный трейлер нового чемпиона Сенны и другие обновления League of Legends', 'Legends of Runeterra — коллекционная карточная игра во вселенной League of Legends', 'В пятом сезоне PUBG можно будет кидать во врагов топоры и сковородки', 'Blizzard забанила американскую команду по Hearthstone\xa0на полгода за плакат с призывом об освобождении Гонконга', 'Для PC-версии Saints Row 2 выйдет обновление с техническими улучшениями, хотя игре уже 11 лет', 'Видео: персонажи и весёлые сражения с использованием разного оружия в Plants vs. Zombies: Battle for Neighborville', 'Обзор Huawei MateBook D 15 (MRC-W10): недорогой ноутбук для учебы и работы', 'Обзор NVMe-накопителя Lexar NM610: возвращение легенды', 'Gamesblender № 434: перенос Doom Eternal, PlayStation 5 в конце 2020-го и Blizzard в центре скандала', 'Обзор iPhone 11: Apple против жабы', "Tom Clancy's Ghost Recon: Breakpoint — удивительный винегрет. Рецензия", 'Code Vein — у вампиров тоже есть душа. Рецензия', 'Обзор игрового WQHD-монитора ASUS TUF Gaming VG27AQ:\nизбавление от кандалов', 'Обзор и тестирование корпуса NZXT H510: минимализм с компромиссами', 'Обзор смартфона BQ Strike Power Max: я хочу еще немного дольше', 'Обзор умной колонки Яндекс.Станция Мини: джедайские шт��чки', 'Компьютер месяца. Спецвыпуск: собираем игровой ПК за 100\nтысяч рублей (осень-зима 2019 года)', 'Обзор ASUS ROG Phone II: самый мощный Android-смартфон', 'Gamesblender № 433: RDR2 на ПК, Sony без Лейдена и новая эра VR в The Walking Dead: Saints & Sinners', 'Обзор видеокарты SAPPHIRE PULSE Radeon RX 5700 XT: кулер здорового человека', 'Ренессанс мобильных игр? Обзор Apple Arcade', 'От DOOM Eternal до King’s Bounty II: 11 игр, ради которых стоит сходить на «ИгроМир 2019»', 'Обзор игрового WQHD-монитора Gigabyte AORUS CV27Q: впереди планеты всей', 'Обзор электросамоката Starway Z9: чемпион в тяжелом весе', 'Обзор смартфона Huawei Mate 30 Pro: особенный', 'Обзор материнской платы ASRock X570 Steel Legend: начальный уровень X570', 'Обзор смартфона Huawei Mate 30 Pro: особенный', 'Обзор материнской платы ASRock X570 Steel Legend: начальный уровень X570', 'Компьютер месяца — октябрь 2019 года', 'Gamesblender № 432: жестокая The Last of Us Part II, бескровная Fallen Order и Medal of Honor в VR', 'Групповое тестирование 43 видеокарт в Borderlands 3', 'Oninaki — умереть спокойно не дадут. Рецензия', 'The Legend of Zelda: Link’s Awakening — милый музейный экспонат. Рецензия', 'Обзор корпуса Phanteks Evolv X Glass Galaxy Silver: эстетика в каждой детали', 'Обзор Nintendo Switch Lite: больше не переключатель', 'Обзор игрового 34-дюймового UWQHD-монитора LG UltraGear 34GK950G: оправданные ожидания', 'Обзор Apple iPhone 11 Pro Max: лучший в мире смартфон с худшим названием', 'Обзор ASUS ZenBook Pro Duo UX581GV: провальный эксперимент или будущее ноутбуков?', 'The Surge 2 — мастер-класс по сиквелам. Рецензия', 'Gamesblender № 431: эпическая Total War Saga: Troy, хардкорная Nioh 2 и прорывная Disco Elysium', 'Обзор видеокарты ROG Strix GeForce RTX 2080 SUPER OC: в погоне за тишиной', 'Borderlands 3 — игра, застрявшая в прошлом. Рецензия', 'Daemon x Machina — а можно нам другое будущее? Рецензия', 'Обзор камеры Canon PowerShot G5 X Mark II: зачем нужны «мыльницы» в наше время?', 'Первые впечатления от Huawei Mate 30 и Mate 30 Pro: жизнь по-новому', 'Блок питания Cougar VTX600: новый «старый конь»', 'Обзор беспроводных наушников JBL TUNE 120TWS: мобильный звук для требовательных', 'Как прав��льно и красиво организовать кабель-менеджмент в игровом ПК', 'Обзор материнской платы ASUS ROG Crosshair VIII Formula: первая Formula для Ryzen', 'Первые впечатления от Vivo NEX 3: смартфон без кнопок', 'МойОфис. Эволюция проекта']
        
    def test_valid(self):
        self.assertEqual(valid(self.url).status_code, 200)

    def test_articles(self):
        self.assertCountEqual(articles, self.articles_expected)
