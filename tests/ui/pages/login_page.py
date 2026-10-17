from playwright.sync_api import Page

class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        self.page = page
        self.campo_usuario = page.locator("#user-name")
        self.campo_senha = page.locator("#password")
        self.botao_login = page.locator("#login-button")
        self.mensagem_erro = page.locator("[data-test='error']")

    def abrir(self):
        self.page.goto(self.URL)

    def fazer_login(self, usuario: str, senha: str):
        self.campo_usuario.fill(usuario)
        self.campo_senha.fill(senha)
        self.botao_login.click()