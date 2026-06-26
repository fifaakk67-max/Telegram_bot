import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Боттың жаңа токені
BOT_TOKEN = "8594504587:AAEvAi9MYmUgeslPHOoJ1gaKkK4D9tLkr2g"
# Сенің жеке Telegram ID-ің
ADMIN_ID = 8553514836

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- 1. СТАРТ КОМАНДАСЫ (Тіл таңдау) ---
@dp.message(CommandStart())
async def start_command(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Русский 🇷🇺", callback_data="lang_ru")
    builder.button(text="Қазақша 🇰🇿", callback_data="lang_kk")
    builder.adjust(2)

    await message.answer(
        text="Здравствуйте выберите язык / Сәлеметсізбе тілді таңдаңыз:",
        reply_markup=builder.as_markup()
    )

# --- 2. ОРЫС ТІЛІ СЦЕНАРИЙІ ---
@dp.callback_query(F.data == "lang_ru")
async def process_ru_lang(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="Временный ⌛️", callback_data="ban_ru_temp")
    builder.button(text="Навсегда 😢", callback_data="ban_ru_perm")
    builder.adjust(2)

    await callback.message.edit_text(
        text="Здравствуйте скажите какой у вас бан?",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@dp.callback_query(F.data == "ban_ru_temp")
async def ru_temp_pay(callback: types.CallbackQuery):
    text = (
        "🏦 Банк для оплаты: 🔴 Каспи\n\n"
        "👤 Получатель: Болат.А\n"
        "🤩 Реквизиты: `4400430319313810`\n"
        "💰 Сумма: 250\n\n"
        "✅ После оплаты отправьте скриншот чека ⤵️"
    )
    await callback.message.edit_text(text=text, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "ban_ru_perm")
async def ru_perm_pay(callback: types.CallbackQuery):
    text = (
        "🏦 Банк для оплаты: 🔴 Каспи\n\n"
        "👤 Получатель: Болат.А\n"
        "🤩 Реквизиты: `4400430319313810`\n"
        "💰 Сумма: 500\n\n"
        "✅ После оплаты отправьте скриншот чека ⤵️"
    )
    await callback.message.edit_text(text=text, parse_mode="Markdown")
    await callback.answer()

# --- 3. ҚАЗАҚ ТІЛІ СЦЕНАРИЙІ ---
@dp.callback_query(F.data == "lang_kk")
async def process_kk_lang(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="Уақытша ⌛️", callback_data="ban_kk_temp")
    builder.button(text="Мәңгілік 🥲", callback_data="ban_kk_perm")
    builder.adjust(2)

    await callback.message.edit_text(
        text="Сәлеметсізбе сізде қандай бан екенін айтып жіберіңіз:",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@dp.callback_query(F.data == "ban_kk_temp")
async def kk_temp_pay(callback: types.CallbackQuery):
    text = (
        "🏦 Төлем жасау үшін банктің аты: 🔴 Каспи\n\n"
        "👤 Төлем алушы: Болат.А\n"
        "🤩 Реквизиты: `4400430319313810`\n"
        "💰 Сумма: 250\n\n"
        "✅ Төлем жасағаннан кейін квитанция немесе чек жіберіңіз⤵️"
    )
    await callback.message.edit_text(text=text, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "ban_kk_perm")
async def kk_perm_pay(callback: types.CallbackQuery):
    text = (
        "🏦 Төлем жасау үшін банктің аты: 🔴 Каспи\n\n"
        "👤 Төлем алушы: Болат.А\n"
        "🤩 Реквизиты: `4400430319313810`\n"
        "💰 Сумма: 500\n\n"
        "✅ Төлем жасағаннан кейін квитанция немесе чек жіберіңіз⤵️"
    )
    await callback.message.edit_text(text=text, parse_mode="Markdown")
    await callback.answer()

# --- 4. ЧЕК КЕЛГЕНДЕ ЖАУАП БЕРУ ЖӘНЕ САҒАН ЖІБЕРУ ---
@dp.message(F.photo)
async def handle_photo(message: types.Message):
    response_text = (
        "🌟💡 **[RU]** Спасибо за оплату мы скоро проверим ваш запрос\n"
        "А пока что заполните эти пункты:\n"
        "Ваш Nickname:\n"
        "Администратор который вас заблакировал:\n"
        "Напишите время получение бана:\n"
        "Напишите как вы получтли этот бан(тем больше вы напишите тем больше шанс выйти с бана):\n"
        "фото ващего бана:\n\n"
        "_________________________\n\n"
        "Төлем жасағаныңызға рахмет біз жақын арада сізге жауап береміз.\n"
        "Сіз мына сұраққа жауап бере беріңіз:\n"
        "Сіздің ойындағы Атыңыз:\n"
        "Сізді банға тыққан администратордың аты:\n"
        "Сіз қашан банға кеттіңіз:\n"
        "Қалай бан алғаныңызды айтыңыз(сіз қалай бан алғаныңызды көбірек жазсаңыз аккаунтыңыз да баннан шығу пайызы көп болады):\n"
        "Банның суреті."
    )
    await message.answer(text=response_text)

    # Саған хабарлама жіберу (Личкаңа барады)
    user_info = f"👤 **Жаңа чек келді!**\n\n" \
                f"Аты: {message.from_user.full_name}\n" \
                f"Username: @{message.from_user.username if message.from_user.username else 'Жоқ'}\n" \
                f"ID: `{message.from_user.id}`"
    
    try:
        await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id, caption=user_info, parse_mode="Markdown")
    except Exception as e:
        print(f"Қате: Саған хабарлама жіберілмеді: {e}")

# Ботты іске қосу
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

Ос
