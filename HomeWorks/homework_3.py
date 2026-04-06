import flet as ft

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    def text_name(e):
        age = text_input.value.strip()

        if age.isdigit() and int(age) >= 18:
            text_hello.value = f'Добро пожаловать!'
            text_hello.color = ft.Colors.GREEN_900
        elif not age.isdigit():
            text_hello.value = 'Введите число!'
            text_hello.color = ft.Colors.RED_900
        else:
            text_hello.value = "Доступ запрещен!"
            text_hello.color = ft.Colors.RED_900

        page.update()

    text_hello = ft.Text('', color=ft.Colors.RED)
    text_input = ft.TextField(label='Введите свой возраст')
    btn = ft.ElevatedButton('Отправить', icon=ft.Icons.SEND, on_click=text_name)

    page.add(text_hello, text_input, btn)

ft.app(main_page)