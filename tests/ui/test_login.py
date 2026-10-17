import pytest
from playwright.sync_api import Page, expect
from tests.ui.pages.login_page import LoginPage


@pytest.mark.ui
def test_login_com_sucesso(page: Page):
    login = LoginPage(page)
    login.abrir()
    login.fazer_login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.ui 
def test_login_com_senha_invalida(page: Page):
    login = LoginPage(page)
    login.abrir()
    login.fazer_login("standard_user", "senha_incorreta")
    expect(login.mensagem_erro).to_be_visible

@pytest.mark.ui
def test_login_usuario_bloqueado(page: Page):
    login = LoginPage(page)
    login.abrir()
    login.fazer_login("locked_out_user", "secret_sauce")
    expect(login.mensagem_erro).to_contain_text("locked out")