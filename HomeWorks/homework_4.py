import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []

    chose_history = []

    greeting_text = ft.Text('История заполнения:')

    chose_text = ft.Text('Избранное:')

    def text_name(e):
        name = text_input.value.strip()
        if not name:
            text_hello.value = "Введите корректное имя!" 
            text_hello.color = ft.Colors.RED_900


        elif name in greeting_history:
               text_hello.value = 'Это имя уже есть в списке!'
               text_hello.color = ft.Colors.RED_900
        elif name.isdigit():
            text_hello.value = 'Имя не может состоять из цифр!'
            text_hello.color = ft.Colors.RED_900
        elif len(name) < 2:
            text_hello.value = 'Имя не может состоять из одного символа!'
            text_hello.color = ft.Colors.RED_900
        else:
            text_hello.value = f"Привет! {name}"
            text_hello.color = ft.Colors.BLUE
            greeting_history.append(name)
            greeting_text.value = f'Избранное: \n' + "\n".join(greeting_history)

        if len(greeting_history) > 4:
            delete_name(index=0)

        text_input.value = ""

        page.update()

    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        
        page.update()


    text_hello = ft.Text('Как тебя зовут?', size=20)
    text_input = ft.TextField(label='Ваше имя', on_submit=text_name, expand=False)
    btn = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=text_name)


    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История приветствия:"
        chose_history.clear()
        chose_text.value = 'Избранное'
        page.update()

    def add_favorite(e):
        name = text_input.value.strip()
        if not name:
            text_hello.value = "Введите корректное имя!" 
            text_hello.color = ft.Colors.RED_900
        elif name in chose_history:
               text_hello.value = 'Это имя уже есть в списке!'
               text_hello.color = ft.Colors.RED_900
        elif len(name) < 2:
            text_hello.value = 'Имя не может состоять из одного символа!'
            text_hello.color = ft.Colors.RED_900
        elif name.isdigit():
            text_hello.value = 'Имя не может состоять из цифр!'
            text_hello.color = ft.Colors.RED_900
        else:
            chose_history.append(name)
            chose_text.value = f'Избранное: \n' + "\n".join(chose_history)
            text_hello.value = f"{name} добавлен в избранное"

        text_input.value = ""
        page.update()


    def delete_name(index):
        greeting_history.pop(index)
        
        


    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    chose_button = ft.IconButton(icon=ft.Icons.FAVORITE, on_click=add_favorite)

    row = ft.Row(
    controls=[theme_btn, clear_button],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    main_object = ft.Row(
    controls=[text_input, btn, chose_button],
    alignment=ft.MainAxisAlignment.CENTER)
    row = ft.Row(
    controls=[theme_btn, clear_button],
    alignment=ft.MainAxisAlignment.CENTER
)

    layout = ft.Column(
    controls=[
        row,
        text_hello,
        main_object,
        greeting_text,
        chose_text
    ],
    alignment=ft.MainAxisAlignment.START,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)
    page.add(layout)


ft.app(main_page, view=ft.AppView.WEB_BROWSER)