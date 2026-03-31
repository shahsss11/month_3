import flet as ft

def main(page: ft.Page):
    page.title = "Счетчик"

    count = 0  

    text_hello = ft.Text(f"Нажато: {count} раз")

    def button_click(e):
        nonlocal count
        count += 1
        text_hello.value = f"Нажато: {count} раз"
        page.update()

    btn = ft.ElevatedButton("Нажми меня", on_click=button_click)

    page.add(text_hello, btn)

ft.app(target=main)