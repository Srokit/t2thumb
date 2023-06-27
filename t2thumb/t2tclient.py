from collections.abc import Callable

from selenium.webdriver import We

ImageReadyCallback = Callable[[bytes], None]

class T2TClient:
    def __init__(self,
                 img_crop_to_size: tuple[int, int] = (300, 300),
                 img_size_out: tuple[int, int] = (100, 100),
                 tiktok_page: str = 'explore') -> None:
        """Set up the client."""
        self._img_crop_to_size = img_crop_to_size
        self._img_size_out = img_size_out
        self._page = tiktok_page
        
        self._sel_driver

    def download_all_with_callback(self, img_ready_cb: ImageReadyCallback) -> None:
        """Download all the images from TikTok and pass each of them
           to the callback as they are ready.
        """
        pass
