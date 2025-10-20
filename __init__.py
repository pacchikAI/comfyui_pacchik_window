import torch
import numpy as np
from PIL import Image, ImageSequence, ImageOps
import numpy as np
import pygetwindow as gw
from mss import mss
from typing import Union

def pil_to_tensor(img: Union[Image.Image, 'mss.screenshot.ScreenShot'], normalize: bool = True) -> torch.Tensor:

    if not isinstance(img, Image.Image):
        img = Image.frombytes('RGB', img.size, img.bgra, 'raw', 'BGRX')
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    img_array = np.array(img).astype(np.float32)
    
    if normalize:
        img_array = img_array / 255.0
    
    tensor = torch.from_numpy(img_array).unsqueeze(0)
    
    return tensor


class DynamicSelectionNode:
    @classmethod
    def INPUT_TYPES(cls):
        # Generate the list of options
        options = cls.generate_options()
        
        return {
            "required": {
                "window_name": (options, {"default": options[0] if options else None}),
                "Left_Ignore": ("INT", {
                    "default": 0, 
                    "min": 0,
                    "max": 90, 
                }),
                "Top_Ignore": ("INT", {
                    "default": 0, 
                    "min": 0,
                    "max": 90, 
                }),
                "Right_Ignore": ("INT", {
                    "default": 0, 
                    "min": 0,
                    "max": 90, 
                }),
                "Bottom_Ignore": ("INT", {
                    "default": 0, 
                    "min": 0,
                    "max": 90, 
                }),
                                                                
                "seed": ("INT", {
                    "default": 0, 
                    "min": 0, 
                }),
            }
        }

    @classmethod
    def generate_options(cls):
        windows = gw.getAllWindows()

        num_options = min(len(windows), 5)  # Change this if you have lots of windows
        options=[]
        for i, window in enumerate(windows):
            if window.title: 
                option = window.title 
                options.append(option)
            else:
                option = window.title

        return options

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "capture_window"
    CATEGORY = "PacchiK Nodes"

    def capture_window(self, window_name, Top_Ignore, Left_Ignore,Right_Ignore,Bottom_Ignore,seed):
        windows = gw.getAllWindows()
        target_window = next((win for win in windows if win.title == window_name), None)
        test= seed        
        
        top_pixels = int(target_window.height * (Top_Ignore / 100))
        bottom_pixels = int(target_window.height * (Bottom_Ignore / 100))
        left_pixels = int(target_window.width * (Left_Ignore / 100))
        right_pixels = int(target_window.width * (Right_Ignore / 100))

        with mss() as sct:
            monitor = {
                "top": target_window.top + top_pixels,
                "left": target_window.left + left_pixels,
                "width": target_window.width - (left_pixels + right_pixels),
                "height": target_window.height - (top_pixels + bottom_pixels)
            }
            
            screenshot = sct.grab(monitor)
            return_image = pil_to_tensor(screenshot)
        

        return (return_image,)

NODE_CLASS_MAPPINGS = {
    "DynamicSelectionNode": DynamicSelectionNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "DynamicSelectionNode": "Select Window"
}