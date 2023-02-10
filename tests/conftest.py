import pytest
import selenium.webdriver

@pytest.fixture
def browser():
    
    # Initialize ChromeDriver instance
    b = selenium.webdriver.Chrome(executable_path=r"./webdriver")

    # Wait 10 s for elements to apear
    b.impolicitly_wait(10)

    # Return instance
    yield b

    # quit instance for cleanup
    b.quit()