import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_titulo_da_pagina(page: Page):
    page.goto("https://playwright.dev")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")