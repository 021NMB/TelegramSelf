from .library import *
from .Information import *

def get_user_bio():
    with open('settings/bio.txt', 'r') as f:
        return f.read().strip()

timezone = pytz.timezone('Asia/Tehran')

current_time_str = datetime.datetime.now(timezone).strftime("%H:%M")

async def update_last_name():
    global current_time_str
    while True:
        with open('settings/time.txt', 'r') as f:
            option_enabled = f.read().strip() == 'True'
        with open('settings/heart.txt', 'r') as f:
            heart_enabled = f.read().strip() == 'True'
        with open('settings/mode.txt', 'r') as f:
            mode = f.read().strip()

        if option_enabled:
            current_time = datetime.datetime.now(timezone)
            rounded_time = current_time.replace(second=0, microsecond=0) + datetime.timedelta(minutes=ceil(current_time.second/60))
            current_time_str = rounded_time.strftime("%H:%M")
            
            if mode == 'Bold':
                current_time_str = current_time_str.replace("0", "𝟎").replace("1", "𝟏").replace("2", "𝟐").replace("3", "𝟑").replace("4", "𝟒").replace("5", "𝟓").replace("6", "𝟔").replace("7", "𝟕").replace("8", "𝟖").replace("9", "𝟗")
            if mode == 'Mono':
                current_time_str = current_time_str.replace("0", "０").replace("1", "１").replace("2", "２").replace("3", "３").replace("4", "４").replace("5", "５").replace("6", "６").replace("7", "７").replace("8", "８").replace("9", "９")
            if mode == 'Mini':
                current_time_str = current_time_str.replace("0", "⁰").replace("1", "¹").replace("2", "²").replace("3", "³").replace("4", "⁴").replace("5", "⁵").replace("6", "⁶").replace("7", "⁷").replace("8", "⁸").replace("9", "⁹")
            
            
            heart_list = ['❤️', '💛', '💚', '💙', '💜', '🖤', '🤍', '🧡', '💖', '💗', '💓', '💞', '💕', '💘', '💝', '💟', '🩵']
            heart = random.choice(heart_list)

            with open('settings/nameinfo.txt', 'r') as f:
                user_lname = f.read()
            user_lname = user_lname.replace("time", current_time_str).replace("heart", heart)
            await client(UpdateProfileRequest(last_name=f"{user_lname}"))
        
        await asyncio.sleep(60 - datetime.datetime.now().second)



async def update_about():
    while True:
        with open('settings/bioinfo.txt', 'r') as f:
            bio_info_enabled = f.read().strip() == 'True'

        if bio_info_enabled:
            with open('settings/mode.txt', 'r') as f:
                mode = f.read().strip()

            current_time = datetime.datetime.now(timezone)
            rounded_time = current_time.replace(second=0, microsecond=0) + datetime.timedelta(minutes=ceil(current_time.second / 60))
            current_time_str = rounded_time.strftime("%H:%M")
            persian_date = jdatetime.datetime.now().strftime("%Y/%m/%d")

            if mode == 'Bold':
                current_time_str = current_time_str.replace("0", "𝟎").replace("1", "𝟏").replace("2", "𝟐").replace("3", "𝟑").replace("4", "𝟒").replace("5", "𝟓").replace("6", "𝟔").replace("7", "𝟕").replace("8", "𝟖").replace("9", "𝟗")
                persian_date = persian_date.replace("0", "𝟎").replace("1", "𝟏").replace("2", "𝟐").replace("3", "𝟑").replace("4", "𝟒").replace("5", "𝟓").replace("6", "𝟔").replace("7", "𝟕").replace("8", "𝟖").replace("9", "𝟗")

            if mode == 'Mono':
                current_time_str = current_time_str.replace("0", "０").replace("1", "１").replace("2", "２").replace("3", "３").replace("4", "４").replace("5", "５").replace("6", "６").replace("7", "７").replace("8", "８").replace("9", "９")
                persian_date = persian_date.replace("0", "０").replace("1", "１").replace("2", "２").replace("3", "３").replace("4", "４").replace("5", "５").replace("6", "６").replace("7", "７").replace("8", "８").replace("9", "９")
            if mode == 'Mini':
                current_time_str = current_time_str.replace("0", "⁰").replace("1", "¹").replace("2", "²").replace("3", "³").replace("4", "⁴").replace("5", "⁵").replace("6", "⁶").replace("7", "⁷").replace("8", "⁸").replace("9", "⁹")
                persian_date = persian_date.replace("0", "⁰").replace("1", "¹").replace("2", "²").replace("3", "³").replace("4", "⁴").replace("5", "⁵").replace("6", "⁶").replace("7", "⁷").replace("8", "⁸").replace("9", "⁹")
                
            heart_list = ['❤️', '💛', '💚', '💙', '💜', '🖤', '🤍', '🧡', '💖', '💗', '💓', '💞', '💕', '💘', '💝', '💟', '🩵']
            heart = random.choice(heart_list)

            bio = get_user_bio().replace("time", current_time_str).replace("heart", heart).replace("DATE", persian_date)
            await client(UpdateProfileRequest(about=bio))

        await asyncio.sleep(60 - datetime.datetime.now().second)


async def update_first_name():
    prev_name = ''
    while True:
        with open('settings/rnamest.txt', 'r') as f:
            rname_enabled = f.read().strip() == 'True'
        if rname_enabled:
            with open('settings/rname.txt', 'r') as f:
                names = f.read().strip().split(',')
            if len(names) >= 1:
                first_name = random.choice(names).strip()
                while first_name == prev_name:
                    first_name = random.choice(names).strip()
                await client(UpdateProfileRequest(first_name=first_name))
                prev_name = first_name
        current_time = datetime.datetime.now(timezone)
        rounded_time = current_time.replace(second=0, microsecond=0) + datetime.timedelta(minutes=ceil(current_time.second/60))
        current_time_str = rounded_time.strftime("%H:%M")
        next_minute = (rounded_time + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
        time_until_next_minute = (next_minute - current_time).total_seconds()
        await asyncio.sleep(time_until_next_minute)
