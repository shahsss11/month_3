import flet as ft
def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text('Hello')
    text_hello2 = ft.Text('Мое приложение')

    text_input = ft.TextField(label='Введите имя')

    elevated_button = ft.ElevatedButton("send", icon=ft.Icons.SEND, color=ft.Colors.GREEN_700, icon_color=ft.Colors.BLUE_900)
    text_button = ft.TextButton('send')
    icon_button = ft.IconButton(icon=ft.Icons.SEND)


    page.add(text_hello, text_hello2, text_input, text_button, elevated_button, icon_button)

ft.app(target=main_page)


