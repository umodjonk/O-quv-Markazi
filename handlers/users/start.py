from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.keyboards import *
from loader import dp, bot
from keyboards.inline.rate import *
from states.Register import RegisterState
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=main)


@dp.message_handler(text = "ℹ️ Biz haqimizda")
async def bot_about(messgae: types.Message):
    matn = """
GOLD  IT  CENTRE haqida bilasizmi ?

GOLD  IT  CENTER dasturlash yo'nalishi bo'yicha O'zbekistondagi eng zamonaviy bilimlarni beruvchi akademiyalardan biri bo'lib, qisqa muddat ichida o'z o'rnini tobora topib borayotgan muvaffaqiyatli akademiya hisoblanadi. Hozirgi kunda akademiya tasnifida: 

❇️  KOMPYUTER SAVODXONLIGI

❇️  WEB DASTURLASH  (FRONT END,  BECK END)    

❇️  GRAFIK DIZAYN

❇️  TELEGRAM BOT

❇️  PYTHON

❇️ Data analytic

❇️  Data Science va Sun'iy Intellekt

 kabi jahondagi eng ommabop dasturlash tillaridan yuqori darajadagi darslar tashkil etilgan. Akademiyada nafaqat dasturlash, balki dasturlashdan tashqari, o'quvchilar o'zlarida liderlik qobiliyatini ham rivojlantirib olish imkoniyatiga ega bo'ladilar. Turli xil seminarlar, qiziqarli bahslar va real loyihalar barchasi bizda!

♐️ Natijalar: Hozirda bir qancha o'quvchilar ushbu kursni tamomlagan holda IT sohasida o'z yo'nalishlarini topib borishmoqda.  Darslarda o'zlarini ko'rsatgan, masalalarga o'zgacha yechim beradigan, o'z ustida ishlashdan to'xtamaydigan o'quvchilar 100% jamoaga taklif etiladi!

🗞 PS:: SIZ KURSLARIMIZNI A'LO NATIJALAR BILAN TAMOMLASANGIZ, BIZ SIZNI ISH BILAN TAMINLAYMIZ!
    """
    await messgae.answer(text = matn)

@dp.message_handler(text = "📞 Aloqa")
async def connect(message: types.Message):
    matn = """
Biz bilan bog'lanish: 

📞 Tel.: +998(88) 604 82  22
            
📧 E-mail: umodjonk@gmail.com
        
            
Ijtimoiy tarmoqlar:

Telegram: https://t.me/ssfjdkjfghfjgfgjfhdjghdjkgdl
            
Facebook:@becens
            
    """
    await message.answer(matn)


@dp.message_handler(text = "🎓 Kurslar")
async def answer_courses(message: types.Message):
    matn = "<i>Aynan qaysi yo'nalishdagi kursimiz haqida ma'lumot kerak?</i>"
    await message.answer(matn, reply_markup=cuorses)


@dp.message_handler(text = "🖥 Kompyuter savodxonligi")
async def answer(message: types.Message):
    matn = """
🎓 Kurs: Kompyuter savodxonligi! 

📚 Texnologiyalar : Kompyuterning ichki va tashqi tuzilishi, Ishlash sxemasi, Word, Excel, Powerpoint, PDF hujjatlar, Ta'lim saytlari bilan ishlash, Rangli va rangsiz Printerlar bilan ishlash

👨🏻‍💻 Jarayon: Umumiy kurs 3 oy muddatni o'z ichiga olib, ushbu muddat ichida siz eng sodda kompyuter amallaridan tortib eng murakkablarigacha bemalol bajara olasiz. Bundan tashqari kursimizni A'Lo natijalar bilan tamomlasangiz, o'z sertifikatingizga ega bo'lgan holda kursni yakunlaysiz.

🎁 Bonus : Kurs davomida Kompyuter bilimlaridan tashqari, o'quvchilar o'zlarida liderlik qobiliyati va ilm olish sirlarini ham rivojlantirib olishadi. Turli xil seminarlar, qiziqarli bahslar va real loyihalar barchasi sizni kutmoqda shoshiling! Darslarda o'zlarini ko'rsatgan, masalalarga o'zgacha yechim beradigan, o'z ustida ishlashdan to'xtamaydigan o'quvchilar 100% jamoaga taklif etiladi!  
    """
    await message.answer(matn)


@dp.message_handler(text = "🌐 Web dasturlash")
async def answer(message: types.Message):
    matn = """
🎓 Kurs:  Web dasturlash!

 Bu kursimiz Frontend va Backend qismlarga bo'linadi. 

📚 Frontend : Bu kursimizda siz web saytlarning dizayn qismi bo'yicha barcha bilimlarni olasiz va real loyihalar bilan ishlaysiz! 

📚 Texnologiyalar: HTML5, CSS3, Bootstrap4, SASS, Javascript, IT resume.

👨🏻‍💻 Jarayon: Umumiy kurs 4 oy muddatni o'z ichiga olib, shu muddat ichida siz eng sodda web sayt maketlaridan tortib eng murakkablarigacha bemalol yasay olasiz. Bundan tashqari bir qancha real online magazinlar dizayni ustida ishlaysiz, kurs so'ngida siz kursimizni A'Lo natijalar bilan tamomlasangiz, o'z sertifikatingiz va portfoliongizga ega bo'lgan holda kursni yakunlaysiz! 
   Darslarda o'zlarini ko'rsatgan, masalalarga o'zgacha yechim beradigan, o'z ustida ishlashdan to'xtamaydigan o'quvchilar 100% jamoaga taklif etiladi!



🎓  Backend : Bu kursimizda siz web saytlarning  dinamik qismi ustida ishlash bo'yicha barcha bilimlarni olasiz va real loyihalar ustida ishlaysiz! 

📚 Texnologiyalar: Javascript, Python, php, SQL, Node.js, Yii2/Laravel, IT resume. 

👨🏻‍💻 Jarayon: Back end kursimiz 4 oy muddatni tashkil etadi, kurs davomida siz saytlarning dinamik qismi ustida ishlashni Python, Javascript va php dasturlash tilida o'rganasiz. Faqatgina dinamik saytlar emas, balki  online magazin va bir qancha dasturlarni  ham bemalol qura olish imkoniyatiga ega bo'lasiz.

🎁 Bonus : Kurs davomida dasturlashdan tashqari, o'quvchilar o'zlarida liderlik qobiliyati va ilm olish sirlarini ham rivojlantirib olishadi. Turli xil seminarlar, qiziqarli bahslar, real loyihalar barchasi sizni kutmoqda shoshiling! 
   Darslarda o'zlarini ko'rsatgan, masalalarga o'zgacha yechim beradigan, o'z ustida ishlashdan to'xtamaydigan o'quvchilar 100% jamoaga taklif etiladi!    
    """
    await message.answer(matn)


@dp.message_handler(text = "🖼 Grafik dizayn")
async def answer(message: types.Message):
    matn = """
🎓 Kurs: Grafik dizayner!

 Bu kursimizda siz grafik dizayn bo'yicha barcha bilimlarga ega bo'lasiz va real loyihalar bilan ishlaysiz!

📚 Texnologiyalar : Photoshop, corelDRAW, Adobe illustrator, Logo, Reklama 

👨🏻‍💻 Jarayon: Umumiy kurs 8 oy muddatni o'z ichiga olib, ushbu muddat ichida siz Grafik dizany bo'yicha barcha bilimlarni olib, real loyihalar bilan ishlaysiz!. Bundan tashqari kursimiz yakunida siz kursimizni A'Lo natijalar bilan tamomlasangiz, o'z sertifikatingiz va portfoliongizga ega bo'lgan holda kursni yakunlaysiz!

🎁 Bonus : Kurs davomida Grafik dizayn bilimlaridan tashqari, o'quvchilar o'zlarida liderlik qobiliyati va ilm olish sirlarini ham rivojlantirib olishadi. Turli xil seminarlar, qiziqarli bahslar va real loyihalar barchasi sizni kutmoqda shoshiling! Darslarda o'zlarini ko'rsatgan, masalalarga o'zgacha yechim beradigan, o'z ustida ishlashdan to'xtamaydigan o'quvchilar 100% jamoaga taklif etiladi!    
    """
    await message.answer(matn)

@dp.message_handler(text = "❇️ Telegram bot")
async def answer(message: types.Message):
    matn = """
🎓 Kurs: Telegram bot!

 Bu kursimizda siz Telagram bot bo'yicha barcha bilimlarga ega bo'lasiz va real loyihalar bilan ishlaysiz!

👨🏻‍💻 Jarayon: Umumiy kurs 2 oy muddatni o'z ichiga olib, shu muddat ichida siz Python dasturlash tili orqali telegram bot yaratishning eng sodda amallaridan tortib eng murakkablarigacha bemalol bajara olasiz.   Bundan tashqari kursimiz yakunida siz kursimizni A'Lo natijalar bilan tamomlasangiz, o'z sertifikatingiz va portfoliongizga ega bo'lgan holda kursni yakunlaysiz!

🎁 Bonus: Kurs davomida Telegram bot bilimlaridan tashqari, o'quvchilar o'zlarida liderlik qobiliyati va ilm olish sirlarini ham rivojlantirib olishadi. Turli xil seminarlar, qiziqarli bahslar va real loyihalar barchasi sizni kutmoqda shoshiling! Darslarda o'zlarini ko'rsatgan, masalalarga o'zgacha yechim beradigan, o'z ustida ishlashdan to'xtamaydigan o'quvchilar 100% jamoaga taklif etiladi!

📉 Qo'shimcha : O'zingizda hech qanday o'sish his qilmasangiz,  pulingiz 100 % qaytariladi.    
    """
    await message.answer(matn)



@dp.message_handler(text = "🏙 Sun`iy intellekt")
async def answer(message: types.Message):
    matn = """
🎓 Kurs: Sun`iy intellekt!

Bu kursimizda siz Data Science va Sun'iy Intellekt bo'yicha barcha bilimlarga ega bo'lasiz va real loyihalar bilan ishlaysiz!

📚 Texnologiya:  Python, Data Science va Sun'iy Intellekt

Bu kursimizda siz Python bo'yicha barcha bilimlarga ega bo'lasiz va real loyihalar bilan ishlaysiz!  Bundan tashqari kursimiz yakunida siz kursimizni A'Lo natijalar bilan tamomlasangiz, o'z sertifikatingiz va portfoliongizga ega bo'lgan holda kursni yakunlaysiz!

👨🏻‍💻 Jarayon: Kurs 8 oy muddatni tashkil etadi. Kurs davomida o'quvchilar Data Science va Sun'iy Intellektdan tashqari o'zlarida liderlik qobiliyati va ilm olish sirlarini ham rivojlantirib olishadi. Turli xil seminarlar, qiziqarli bahslar, real loyihalar barchasi sizni kutmoqda shoshiling! Darslarda o'zlarini ko'rsatgan, masalalarga o'zgacha yechim beradigan, o'z ustida ishlashdan to'xtamaydigan o'quvchilar 100 % jamoaga taklif etiladi!    
    """
    await message.answer(matn)

@dp.message_handler(text = "🐍 Python")
async def answer(message: types.Message):
    matn = """
🎓 Kurs: Python! 

📚 Texnologiya:  Python! 

Bu kursimizda siz Python bo'yicha barcha bilimlarga ega bo'lasiz va real loyihalar bilan ishlaysiz!

👨🏻‍💻 Jarayon: Kurs 5 oy muddatni tashkil etadi. Kurs davomida siz  telegram bot, Django da e-shop (online magazin), Bankomatlarning ishlash sxemasi va kodini yozish kabi ko'plab loyihalar ustida ishlaysiz.  Bundan tashqari kursimiz yakunida siz kursimizni A'Lo natijalar bilan tamomlasangiz, o'z sertifikatingiz va portfoliongizga ega bo'lgan holda kursni yakunlaysiz!

🎁 Bonus : Kurs davomida o'quvchilar Pythondan tashqari o'zlarida liderlik qobiliyati va ilm olish sirlarini ham rivojlantirib olishadi. Turli xil seminarlar, qiziqarli bahslar, real loyihalar barchasi sizni kutmoqda shoshiling! Darslarda o'zlarini ko'rsatgan, masalalarga o'zgacha yechim beradigan, o'z ustida ishlashdan to'xtamaydigan o'quvchilar 100 % jamoaga taklif etiladi.!    
    """
    await message.answer(matn)

    @dp.message_handler(text="🥪Data analytic")
    async def answer(message: types.Message):
        matn = """
    🥪Kurs: Data analytic! 

    📚 Texnologiya: Data analytic ! 

    Bu kursimizda siz Data analytic  bo'yicha barcha bilimlarga ega bo'lasiz va real loyihalar bilan ishlaysiz!

    👨🏻‍💻 Jarayon: Kurs 5 oy muddatni tashkil etadi. Kurs davomida siz  SQL,Database va undan tashqari ma'lumotlar bazasi bilan ishlashni organasiz.  Bundan tashqari kursimiz yakunida siz kursimizni A'Lo natijalar bilan tamomlasangiz, o'z sertifikatingiz va portfoliongizga ega bo'lgan holda kursni yakunlaysiz!

    🎁 Bonus : Kurs davomida o'quvchilar Data analytic tashqari o'zlarida liderlik qobiliyati va ilm olish sirlarini ham rivojlantirib olishadi. Turli xil seminarlar, qiziqarli bahslar, real loyihalar barchasi sizni kutmoqda shoshiling! Darslarda o'zlarini ko'rsatgan, masalalarga o'zgacha yechim beradigan, o'z ustida ishlashdan to'xtamaydigan o'quvchilar 100 % jamoaga taklif etiladi.!    
        """
        await message.answer(matn)




























@dp.message_handler(text = "🔙 Ortga qaytish")
async def answer(message: types.Message):
    await message.answer("Bosh menyudasiz.", reply_markup=main)

@dp.message_handler(text = "📍 Manzil")
async def answer(message: types.Message):
    await message.answer_location(latitude=37.22871, longitude=67.272341)

@dp.message_handler(text = "®️ Kursga yozilish")
async def answer(message: types.Message):
    matn = """
Familiya Ism Sharif ?

(Masalan : Ergashev Islom O'rolovich) 
    """
    await message.answer(matn)
    await RegisterState.name.set()


@dp.message_handler(state = RegisterState.name)
async def name(message: types.Message, state: FSMContext):
    await state.update_data({
        "name":message.text
    })

    await message.answer("""
Yoshingiz?

(Masalan : 17 yosh)
    """)

    await RegisterState.next()

@dp.message_handler(state = RegisterState.age)
async def age(message: types.Message, state: FSMContext):
    await state.update_data({
        "age":message.text
    })

    await message.answer("""
Qaysi kursimiz bo'yicha tahsil olmoqchisiz?

🎓 Kurslarimiz : 

❇️  KOMPYUTER SAVODXONLIGI

❇️  WEB DASTURLASH  (FRONT END,  BECK END)   


❇️  GRAFIK DIZAYN

❇️  TELEGRAM BOT

❇️ Data analytic

❇️  PYTHON

❇️  Data Science va Sun'iy Intellekt
    """)

    await RegisterState.next()

@dp.message_handler(state = RegisterState.course)
async def course(message: types.Message, state: FSMContext):
    await state.update_data({
        "course":message.text
    })

    await message.answer("""
Tanlagan yo'nalishingiz bo'yicha bilim darajangiz qanday?

(Masalan : Umuman yo'q, Oz-moz bilaman, To'liq bilaman)
    """)

    await RegisterState.next()


@dp.message_handler(state = RegisterState.rank)
async def rank(message: types.Message, state: FSMContext):
    await state.update_data({
        "rank":message.text
    })

    await message.answer("""
Telefon raqamingizni kiriting?

(Masalan : +99897 1234567)
    """)
    await RegisterState.next()

@dp.message_handler(state = RegisterState.number)
async def number(message: types.Message, state: FSMContext):
    await state.update_data({
        "number":message.text
    })

    await message.answer("""
Ma'lumotlar muvaffaqiyatli saqlandi!, 

Iltimos bot faoliyatini baholang!
    """, reply_markup=rating)
    await RegisterState.next()

@dp.callback_query_handler(state = RegisterState.rate)
async def ratsedaefing(call: types.CallbackQuery, state: FSMContext):
    if call.data == "great":
        await state.update_data({
            "rate":"👍 Ajoyib"
        })
        data = await state.get_data()

        text = "Sizning Anketangiz tayyor bo'ldi,\n\nBarcha ma'lumotlaringizni tasdiqlaysizmi?\n\n"
        text += f"🎓 Shogird: {data['name']}\n"
        text += f"🌐 Yosh: {data['age']}\n"
        text += f"🎓 Kurs: {data['course']}\n"
        text += f"👨🏻‍💻 Daraja: {data['rank']}\n"
        text += f"📞 Aloqa: {data['number']}\n"
        text += f"☑️ Rating: {data['rate']}\n"
        await call.message.answer(text=text, reply_markup=check)
        await RegisterState.next()
    else:
        await state.update_data({
            "rate":"👎 Yomon"
        })
        data = await state.get_data()

        text = "Sizning Anketangiz tayyor bo'ldi,\n\nBarcha ma'lumotlaringizni tasdiqlaysizmi?\n\n"
        text += f"🎓 Shogird: {data['name']}\n"
        text += f"🌐 Yosh: {data['age']}\n"
        text += f"🎓 Kurs: {data['course']}\n"
        text += f"👨🏻‍💻 Daraja: {data['rank']}\n"
        text += f"📞 Aloqa: {data['number']}\n"
        text += f"☑️ Rating: {data['rate']}\n"
        await call.message.answer(text=text, reply_markup=check)
        await RegisterState.next()

@dp.callback_query_handler(state = RegisterState.check)
async def check_datas(call: types.CallbackQuery, state: FSMContext):
    if call.data == "yes":
        data = await state.get_data()
        text = "🎉Yangi o'quvchi:\n\n"
        text += f"🎓 Shogird: {data['name']}\n"
        text += f"🌐 Yosh: {data['age']}\n"
        text += f"🎓 Kurs: {data['course']}\n"
        text += f"👨🏻‍💻 Daraja: {data['rank']}\n"
        text += f"📞 Aloqa: {data['number']}\n"
        text += f"☑️ Rating: {data['rate']}\n"

        await bot.send_message(chat_id=-1001861972459, text=text)
        await state.finish()
        await call.message.answer("""
✅ Sizning Anketangiz xodimlarimizga muvaffaqiyatli jo'natildi, qisqa fursatlarda sizga aloqaga chiqamiz! E'tiboringiz uchun rahmat
        """, reply_markup=main)
        await call.message.delete()
    else:
        await state.finish()
        await call.message.answer("Bekor qilindi!", reply_markup=main)

