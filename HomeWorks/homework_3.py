import flet as ft

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

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
        text_input.value = ""

        page.update()
    
    def thememode(e):
            if page.theme_mode == ft.ThemeMode.DARK:
                page.theme_mode = ft.ThemeMode.LIGHT
            else:
                page.theme_mode = ft.ThemeMode.DARK
            
            page.update()

    text_hello = ft.Text('', color=ft.Colors.RED)
    text_input = ft.TextField(label='Введите свой возраст', on_submit=text_name)
    btn = ft.ElevatedButton('Отправить', icon=ft.Icons.SEND, on_click=text_name,)
    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    

    page.add(text_hello, text_input, btn, theme_btn )

ft.app(main_page)