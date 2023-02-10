import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    
    # Initialize ChromeDriver instance
    b = webdriver.Chrome()

    # Wait 10 s for elements to apear
    b.implicitly_wait(10)

    # Return instance
    yield b

    # quit instance for cleanup
    b.quit()