from PIL import Image, ImageDraw, ImageFont

print('Генератор мемов запущен!')

top_text = input('Введите верхний текст: ')
bottom_text = input('Введите нижний текст: ')

print(top_text, bottom_text)

print('Список картинок:')
print('1) Кот говорит: а а а')
print('2) Спанч боб неандерталец')

user_number = int(input('Выберите номер картинки: '))

if user_number == 1:
    image = './img/cat-mem.png'
elif user_number == 2:
    image = './img/spanch_bob.png'

image = Image.open(image)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=30)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw. text(((width - text_width) / 2, 5), top_text, font=font, fill='#7afff0')
text = draw. textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill="#7afff0")

image.save('./img/new_mem.png')