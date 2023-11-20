# ImageFilter made using python, html , css 
#This Python script utilizes the Python Imaging Library (PIL), specifically the
`Image` and `ImageEnhance` modules, to apply various image filters and
showcase the results in an HTML page.
Here's a step-by-step explanation of the code:
1. Import Libraries:
- The script starts by importing necessary modules from the PIL library, as well
as the `webbrowser` and `os` modules for HTML page creation and opening.
2. Define Original Image Path:
- The path to the original image is specified using the `original` variable.
3. Define Filter Functions:
- Several functions (`apply_grayscale_filter`, `apply_yellowish_filter`,
`apply_redish_filter`, `apply_sepia_filter`) are defined to apply different filters to an
input image and save the result. Each function returns the filtered image.
4. Create HTML Page Function:
- The `create_html_page` function generates an HTML page dynamically. It
includes styling with CSS to center and display images in a box. This function
takes the title and content (path to the image) and creates an HTML file.
5. User Interaction and Image Filtering:
- The script then prompts the user to choose a filter from the available options
(grayscale, yellowish, purplish, sepia).
- Based on the user's choice, the corresponding filter function is called, and the
resulting image is saved.
6. Resize and Save Filtered Image:
- The resulting image is resized to 200x200 pixels and saved.
7. Create and Open HTML Page:
- The `create_html_page` function is called with the title "Filtered Image" and the
path to the filtered image. The generated HTML file is then opened in the default
web browser using `webbrowser.open`.
8. Note:
- It's important to note that the script assumes the availability of the original
image at the specified path, and it saves the filtered image in the same directory
as the script.
9. CSS Styling:
- The CSS styling within the `create_html_page` function provides a centered
box with a shadow effect. It includes two image boxes, one for the original image
and one for the filtered image, both displayed with captions.
In summary, this script enables users to apply various filters to an image and view
the original and filtered images side by side in a visually appealing HTML page.
The dynamic creation of the HTML page adds an interactive element to the image
filtering process.
![Capture](https://github.com/JASLEENKAURGILL556/ImageFilter/assets/72688106/e8784b82-b129-4d96-ad8e-198b2fa2819b)

