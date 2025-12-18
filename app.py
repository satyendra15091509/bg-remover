import gradio as gr
from rembg import remove
from PIL import Image
import io

def process_image(image):
    if image is None:
        return None
    # Rembg works best when we convert the image to RGBA (with transparency)
    output = remove(image)
    return output

# Create the Interface
with gr.Blocks(title="Agency Background Remover") as demo:
    gr.Markdown("# 🚀 Professional Background Remover")
    gr.Markdown("Upload a photo to instantly remove the background.")
    
    with gr.Row():
        input_img = gr.Image(type="pil", label="Input Image")
        output_img = gr.Image(type="pil", label="Output Image", show_download_button=True)
    
    btn = gr.Button("Remove Background", variant="primary")
    btn.click(fn=process_image, inputs=input_img, outputs=output_img)

# Launch it
if __name__ == "__main__":
    demo.launch()
