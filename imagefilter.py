from PIL import Image, ImageEnhance
import webbrowser
import os
 
original = r'C:\Users\admin\Desktop\imagefilter\img.jpg'
def apply_grayscale_filter(image_path, output_path):
    image = Image.open(image_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)
    return grayscale_image

def apply_yellowish_filter(image_path, output_path):
    image = Image.open(image_path)
    enhanced_image = ImageEnhance.Color(image).enhance(4)
    enhanced_image.save(output_path)
    return enhanced_image
def apply_redish_filter(image_path, output_path):
    image = Image.open(image_path)
    enhanced_image = ImageEnhance.Color(image).enhance(-0.5)
    enhanced_image.save(output_path)
    return enhanced_image

def apply_sepia_filter(image_path, output_path):
    image = Image.open(image_path)
    image = Image.open(image_path)
    desaturated_image = ImageEnhance.Color(image).enhance(0.5)
    desaturated_image.save(output_path)
    return desaturated_image

def create_html_page(title, content):
    html_content = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #E0B0FF;
        }}

        .center-box {{
            width: 30%;
            height: 30%;
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            padding: 10% ;
            text-align: center;
            border-radius: 20px;
            display:flex;
            justify-content: center;
            align-items: center;
        }}

        .img-box {{
            /* Adjust the gap between items */
            margin:30px;
        }}

        .img-box img {{
            width: 300px;
            height: 300px;
        }}
        center-box:hover{{
            box-shadow: 0 4px 8px rgba(0, 0, 0, 3);
        }}
    </style>
    <title>Centered Box with Shadow</title>
</head>
<body>
    
        <div class="center-box">
            <!-- Your first image content goes here -->
        
        <div class="img-box">
            <h1>Original Image</h1>
           <img src="{original}" alt="Original Image" width="200" height="200">
        </div>
        
        <div class="img-box">
            <h1>{title}</h1>
            <img src="{content}" alt="Original Image" width="200" height="200">
        </div>
      </div>
</body>
</html>

    """

    with open("output.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    input_image_path = r'C:\Users\admin\Desktop\imagefilter\img.jpg'
    output_path = r'C:\Users\admin\Desktop\imagefilter\result.jpg'

    # Display available filters
    print("Available Filters:")
    print("1. Grayscale")
    print("2. Yellowish")
    print("3. Purplish")
    print("4. Sepia")

    # Get user input for the desired filter
    filter_choice = input("Enter the number corresponding to the desired filter: ")

    if filter_choice == "1":
        result_image = apply_grayscale_filter(input_image_path, output_path)
    elif filter_choice == "2":
        result_image = apply_yellowish_filter(input_image_path, output_path)
    elif filter_choice == "3":
        result_image = apply_redish_filter(input_image_path, output_path)
    elif filter_choice == "4":
        result_image = apply_sepia_filter(input_image_path, output_path)

    else:
        print("Invalid choice. Please choose 1 to 4.")
        exit()

    # Resize the resulting image to 200x200 pixels
    resized_image = result_image.resize((200, 200))

    # Save the resized image to a file
    resized_image.save(output_path)

    # Create HTML page and open it in the default web browser
    create_html_page("Filtered Image", "result.jpg")
    webbrowser.open(os.path.abspath("output.html"))
