from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards import main_kb, filters_kb, houses_kb
from human import Human
from generation import generate_houses
from recommendations import get_recommendations

discount = 'idc'
houses = generate_houses()
human = Human('', 0, 0, '')

router = Router()


class Account(StatesGroup):
    full_name = State()
    age = State()
    money = State()
    house = State()


class Money(StatesGroup):
    money = State()


class Purchase(StatesGroup):
    chosen_house = State()


@router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext):
    await state.set_state(Account.full_name)
    await message.answer('Input your full name')


@router.message(Account.full_name)
async def start_cmd(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(Account.age)
    await message.answer('Input your age')


@router.message(Account.age)
async def start_cmd(message: Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await state.set_state(Account.money)
    await message.answer('Input your money count')


@router.message(Account.money)
async def start_cmd(message: Message, state: FSMContext):
    await state.update_data(money=int(message.text))
    await state.set_state(Account.house)
    await message.answer('Do you have house?(Yes/No)')


@router.message(Account.house)
async def start_cmd(message: Message, state: FSMContext):
    await state.update_data(house=message.text.capitalize())
    data = await state.get_data()
    await state.clear()
    human.full_name = data['full_name']
    human.age = data['age']
    human.money = data['money']
    human.house = data['house']
    await message.answer(f'Your info:\n{human}', reply_markup=main_kb)


@router.message(F.text.lower() == 'get recommendations')
async def get_rec(message: Message):
    rec_houses = get_recommendations(human, houses, discount)
    if rec_houses:
        await message.answer('\n\n'.join(f'House #{i + 1}\n\n{house}' for i, house in enumerate(rec_houses)),
                             reply_markup=main_kb)
    else:
        await message.answer('No houses for you', reply_markup=main_kb)


@router.message(F.text.lower() == 'earn money')
async def earn(message: Message, state: FSMContext):
    await state.set_state(Money.money)
    await message.answer('Input money count that you earn')


@router.message(Money.money)
async def earn(message: Message, state: FSMContext):
    await state.update_data(money=int(message.text))
    data = await state.get_data()
    await state.clear()
    await message.answer(human.earn_money(data['money']))


@router.message(F.text.lower() == 'show info')
async def show_info(message: Message):
    await message.answer(f'Your info:\n{human}')


@router.message(F.text.lower() == 'filters')
async def show_filters(message: Message):
    await message.answer('Choose filter', reply_markup=filters_kb)


@router.callback_query(F.data)
async def apply_filters(callback: CallbackQuery):
    global discount
    discount = callback.data
    if discount == 'on':
        await callback.answer('Discount✅')
    elif discount == 'off':
        await callback.answer('Discount❌')
    else:
        await callback.answer('Off filter')


@router.message(F.text.lower() == 'buy house')
async def buy(message: Message, state: FSMContext):
    await state.set_state(Purchase.chosen_house)
    rec_houses = get_recommendations(human, houses, discount)
    await message.answer('Choose house to buy', reply_markup=houses_kb(rec_houses))


@router.message(Purchase.chosen_house)
async def chosen_house(message: Message, state: FSMContext):
    index = int(message.text[-1]) - 1
    rec_houses = get_recommendations(human, houses, discount)
    await state.update_data(chosen_house=rec_houses[index])
    data = await state.get_data()
    await state.clear()

    await message.answer(human.buy_house(data['chosen_house']), reply_markup=main_kb)
