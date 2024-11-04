import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "Un viaje a través del tiempo"
    page.bgcolor = "purple"
    page.window_width = 600
    page.window_height = 800

    img_height = 105
    img_width = 105
    border_radius = 25 

    # Audios
    audios = {
        "intro": ft.Audio(src="intro.mp3"),
        "luna": ft.Audio(src="luna.mp3"),
        "reni": ft.Audio(src="revindu.mp3"),
        "revc": ft.Audio(src="revcient.mp3"),
        "org": ft.Audio(src="orgespc.mp3"),
        "imp": ft.Audio(src="imprenta.mp3"),
        "enrg": ft.Audio(src="energia.mp3"),
        "compus": ft.Audio(src="compus.mp3"),
        "albert": ft.Audio(src="albert.mp3"),
        "adn": ft.Audio(src="adn.mp3"),
    }

    for audio in audios.values():
        page.overlay.append(audio)

    def stop_all():
        for audio in audios.values():
            audio.pause()

    def play_audio(audio_key):
        stop_all()
        audios[audio_key].play()

    # Botones
    buttons = {
        "org": ElevatedButton(content=ft.Image(src="orespc.jpg", width=img_width, height=img_height, border_radius=border_radius, fit=ft.ImageFit.COVER), on_click=lambda _: play_audio("org")),
        "luna": ElevatedButton(content=ft.Image(src="luna.jpg", width=img_width, height=img_height, border_radius=border_radius, fit=ft.ImageFit.COVER), on_click=lambda _: play_audio("luna")),
        "revc": ElevatedButton(content=ft.Image(src="crencient.jpg", width=img_width, height=img_height, border_radius=border_radius, fit=ft.ImageFit.COVER), on_click=lambda _: play_audio("revc")),
        "enrg": ElevatedButton(content=ft.Image(src="elec.jpg", width=img_width, height=img_height, border_radius=border_radius, fit=ft.ImageFit.COVER), on_click=lambda _: play_audio("enrg")),
        "adn": ElevatedButton(content=ft.Image(src="gemhum.jpg", width=img_width, height=img_height, border_radius=border_radius, fit=ft.ImageFit.COVER), on_click=lambda _: play_audio("adn")),
        "compus": ElevatedButton(content=ft.Image(src="compu.jpg", width=img_width, height=img_height, border_radius=border_radius, fit=ft.ImageFit.COVER), on_click=lambda _: play_audio("compus")),
        "reni": ElevatedButton(content=ft.Image(src="ind.jpg", width=img_width, height=img_height, border_radius=border_radius, fit=ft.ImageFit.COVER), on_click=lambda _: play_audio("reni")),
        "imp": ElevatedButton(content=ft.Image(src="imp.jpg", width=img_width, height=img_height, border_radius=border_radius, fit=ft.ImageFit.COVER), on_click=lambda _: play_audio("imp")),
        "albert": ElevatedButton(content=ft.Image(src="albert.jpg", width=img_width, height=img_height, border_radius=border_radius, fit=ft.ImageFit.COVER), on_click=lambda _: play_audio("albert")),
    }

    #cambio de ruta
    def route_change(route):
        stop_all()  
        page.views.clear()

        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(title=ft.Text("Un viaje a través del tiempo"), bgcolor="pink"),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ElevatedButton("Escucha el intro", on_click=lambda _: play_audio("intro"), bgcolor="#25232A"),
                                            ElevatedButton('Ver acontecimientos', on_click=lambda _: page.go('/acontecimientos'), bgcolor="#092A3B")
                                        ],
                                        alignment="spaceBetween",
                                        width=600,
                                        spacing=20,
                                    ),
                                    ft.Image(src="portada.png", width=400, height=200, fit=ft.ImageFit.CONTAIN),
                                    ft.Text("Integrantes del equipo:", size=24, weight="bold", color="black", text_align="center"),
                                    ft.Column(
                                        controls=[
                                            ft.Text("• Robledo Hernández Valeria"),
                                            ft.Text("• Zaragoza Villa Joselyn Esmeralda                        Programación"),
                                            ft.Text("• Ruíz Ramos Alyn Dannae                                    3 b"),
                                            ft.Text("• López Martínez Alison Valentina                         CETIS 50"),
                                            ft.Text("• Hernández Sánchez Samuel                                Emplea frameword"),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        elif page.route == '/acontecimientos':
            page.views.append(
                View(
                    "/acontecimientos",
                    controls=[
                        AppBar(title=ft.Text("Acontecimientos relevantes en el origen de STEM"), bgcolor="blue"),
                        ft.Container(
                            ft.Column(
                                alignment="CENTER",
                                spacing=10,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ElevatedButton('Volver al inicio', on_click=lambda _: page.go('/'), bgcolor="lightcoral"),
                                    ft.Row(alignment="CENTER", controls=[buttons["org"], buttons["luna"], buttons["revc"]]),
                                    ft.Row(alignment="CENTER", controls=[buttons["enrg"], buttons["adn"], buttons["compus"]]),
                                    ft.Row(alignment="CENTER", controls=[buttons["reni"], buttons["imp"], buttons["albert"]]),
                                ]
                            ),
                            bgcolor="red",  
                            expand=True
                        )
                    ],
                    bgcolor="red"  
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
