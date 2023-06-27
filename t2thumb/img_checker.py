import cv2
import numpy as np

FRAC_NON_BLACK_REQUIRED = 0.5

class ImgChecker:
    @staticmethod
    def validate(img: np.ndarray) -> bool:
        """Validate the image.

        Args:
            img: The image to validate.

        Returns:
            Whether the image is valid.
        """
        return ImgChecker._is_not_mostly_black(img)

    @staticmethod
    def _is_not_mostly_black(img: np.ndarray) -> bool:
        """Returns True if the image does not contain too
           much fraction of black pixels.
        """
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)[1]
        return cv2.countNonZero(img) / img.size > FRAC_NON_BLACK_REQUIRED
