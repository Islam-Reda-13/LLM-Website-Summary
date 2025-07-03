import gradio as gr
from models_and_prompting import stream_brochure

with gr.Blocks() as view:
    gr.Markdown("# Summary Generator")
    
    with gr.Row():
        with gr.Column():
            company_name = gr.Textbox(label="Company name:")
            landing_url = gr.Textbox(label="Landing page URL including http:// or https://")
            model_choice = gr.Dropdown(["Qwen", "Deepseek", "Llama"], label="Select model")
            
            generate_btn = gr.Button("Generate Summary", variant="primary")
    
    with gr.Row():
        output_markdown = gr.Markdown(label="Summary:")
    
    generate_btn.click(
        fn=stream_brochure,
        inputs=[company_name, landing_url, model_choice],
        outputs=[output_markdown],
        show_progress=True
    ).then(
        fn=lambda: gr.Button(interactive=True),
        outputs=[generate_btn]
    ).success(
        fn=lambda: gr.Button("Generate Summary", interactive=True),
        outputs=[generate_btn]
    )
    
    generate_btn.click(
        fn=lambda: gr.Button("Generating...", interactive=False),
        outputs=[generate_btn]
    )
view.launch(share=False, debug=True)    