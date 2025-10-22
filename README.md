A simple ComfyUI node that takes any window you have as an Input to ComfyUI node (WORKS IN WINDOWS ONLY <-- No pygetwindow for Linux sorry)

1. Download to  custom_nodes folder
2. Install the requirements.txt

**Select Window Dropdown**

Use this to get a dropdown of all the windows currently open. You will need to refresh the page if the window option is not available

<img width="895" height="586" alt="image" src="https://github.com/user-attachments/assets/ac2a0890-1cba-4bc4-8d6e-14c230ae7968" />

**Select Window Text**

Use this to type the name of the window if the window changes "use * windowname *" (Example: if you are viewing a png file in an image viewer and the name of the window changes when you change). This also inputs the top,bottom, height and width of the location of the window on screen, to be used with **Select Window JSON** as its input

<img width="1454" height="601" alt="image" src="https://github.com/user-attachments/assets/08ea5e0d-9e10-41b7-8405-567600653e46" />

**Select Window Json**

Use this with the input of the **SCREEN LOCATION** from the **Select Window Text** in order to keep the location consistent. 

<img width="1149" height="612" alt="image" src="https://github.com/user-attachments/assets/e54ce078-f703-45b5-ad0c-a00b992f8087" />



SEED and SEED CONTROL are for continous refresh.

To get ComfyUI to continously refresh changes in the window, choose this option
<img width="417" height="107" alt="image" src="https://github.com/user-attachments/assets/aabf43c4-f6cf-4611-ae4b-46993f02c6e0" />


IMPORTANT NOTE TO REMEMBER: YOUR WINDOW NEEDS TO BE VISBLE. Windows will now allow me to automatically activate the window so ensure that your window is visible to capture. 



![pacchik_window](https://github.com/user-attachments/assets/9758c7de-b8c1-4560-9e26-029d6ad2b97b)

