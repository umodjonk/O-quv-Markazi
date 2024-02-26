from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "ℹ️ Biz haqimizda")
        ],
        [
            KeyboardButton(text = "🎓 Kurslar"),
            KeyboardButton(text = "📞 Aloqa")
        ],
        [
            KeyboardButton(text = "📍 Manzil")
        ],
        [
            KeyboardButton(text="®️ Kursga yozilish")
        ]
    ]
)

cuorses = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text = "🖥 Kompyuter savodxonligi")
        ],
        [
            KeyboardButton(text = "🌐 Web dasturlash"),

        ],
        [
            KeyboardButton(text = "🖼 Grafik dizayn")
        ],
        [
            KeyboardButton(text = "❇️ Telegram bot"),

        ],
        [
            KeyboardButton(text = "🥪Data analytic")
        ],
        [
            KeyboardButton(text = "🏙 Sun`iy intellekt"),
            KeyboardButton(text = "🐍 Python")
        ],
        [
            KeyboardButton(text= "®️ Kursga yozilish")
        ],
        [
            KeyboardButton(text = "🔙 Ortga qaytish")
        ]
    ]
)