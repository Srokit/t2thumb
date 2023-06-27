from typing import Generator

from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://www.tiktok.com"
IMGS_XPATH = "//*[@id=\"main-content-explore_page\"]/div/div/div/div/div/div/div/a/div/div/img"

class T2TClient:
    def __init__(self,
                 img_crop_to_size: tuple[int, int] = (300, 300),
                 img_size_out: tuple[int, int] = (100, 100),
                 tiktok_page: str = 'explore?',
                 is_firefox: bool = True) -> None:
        """Set up the client.

        Args:
            img_crop_to_size: The size of the image to crop to.
            img_size_out: The size of the image to output.
            tiktok_page: The page to download images from.
            is_firefox: Whether to use Firefox or Chrome (if False).
        """
        self._img_crop_to_size = img_crop_to_size
        self._img_size_out = img_size_out
        self._page = tiktok_page

        if is_firefox:
            opts = webdriver.FirefoxOptions()
            opts.add_argument("-headless")
            self._sel_driver = webdriver.Firefox(opts)
        else:
            self._sel_driver = webdriver.Chrome()

    def for_each_img(self) -> Generator[bytes, None, None]:
        """Download all the images from TikTok and yield them as bytes.
        """
        self._sel_driver.get(f"{BASE_URL}/{self._page}")
        eles = self._sel_driver.find_elements(By.XPATH, IMGS_XPATH)
        for ele in eles: yield ele.screenshot_as_png
