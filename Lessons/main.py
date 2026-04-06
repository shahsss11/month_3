import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    def text_name(e):  # e - event | "_" 
        text_hello.value = f"Добро пожаловать! {text_input.value}"
        name = text_input.value.strip()
        text_hello.value = None

        if name:
           text_hello.value = f"hello {name}"
        else:
            text_hello.value = "Введи имя быстрее пожалуйста плиз!!!" 
            text_hello.color = ft.Colors.RED_900

        page.update()

    text_hello = ft.Text('Hello', color=ft.Colors.RED)
    text_input = ft.TextField(label='Введите свое имя')
    btn = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=text_name)
    
    theme = page.theme_mode

    def theme_change(e):
        if theme == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

    
    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=theme_change)

    page.add(text_hello, text_input, btn, theme_btn)


ft.app(main_page, )