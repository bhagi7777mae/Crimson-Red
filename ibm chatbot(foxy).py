import gradio as gr

def create_interface():
    """Create the Gradio interface"""

    # Convert uploaded fox image to base64 for embedding
    # Placeholder for the actual fox image base64 string
    fox_image_base64 = ""
    # Placeholder for custom CSS
    CUSTOM_CSS = ""
    # Placeholder for sample prompts
    SAMPLE_PROMPTS = []

    with gr.Blocks(css=CUSTOM_CSS) as interface:
        gr.HTML("<h1 class='header-title'>🦊 Foxy Finance Chatbot 🦊</h1>")
        gr.HTML("<p class='header-subtitle'>Your clever guide to personal finance with the cunning of a fox!</p>")

        # Add the Foxy avatar image
        with gr.Row():
             gr.HTML(f'<img src="{fox_image_base64}" id="foxy-avatar" alt="Foxy Finance Avatar">')


        # Main chat interface
        with gr.Row():
            with gr.Column(scale=4):
                chatbot = gr.Chatbot(
                    height=500,
                    bubble_full_width=False,
                    elem_classes=["chat-container"]
                )

                with gr.Row():
                    msg = gr.Textbox(
                        placeholder="Ask me about savings, taxes, investments, or any financial question... I'm clever like a fox! 🦊",
                        label="",
                        scale=4
                    )
                    send_btn = gr.Button("🦊 Send", variant="primary", scale=1)

                # Sample prompts
                gr.HTML("<h3 style='color: white; text-align: center; margin-top: 20px;'>💡 Try these questions:</h3>")
                sample_buttons = []
                with gr.Row():
                    for prompt in SAMPLE_PROMPTS[:3]:
                        btn = gr.Button(prompt, size="sm")
                        sample_buttons.append(btn)

                with gr.Row():
                    for prompt in SAMPLE_PROMPTS[3:]:
                        btn = gr.Button(prompt, size="sm")
                        sample_buttons.append(btn)

            # Sidebar with financial tools
            with gr.Column(scale=1):
                gr.HTML("<h3 style='color: white; text-align: center;'>🧮 Quick Calculators</h3>")

                with gr.Accordion("Compound Interest", open=False):
                    principal_input = gr.Number(label="Principal ($)", value=1000)
                    rate_input = gr.Number(label="Annual Rate (%)", value=7)
                    time_input = gr.Number(label="Years", value=10)
                    calc_btn = gr.Button("Calculate")
                    calc_result = gr.Textbox(label="Result", interactive=False)

                gr.HTML("""
                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; margin-top: 20px; color: white;">
                    <h4>🦊 Foxy's Financial Focus Areas:</h4>
                    <ul style="list-style-type: none; padding-left: 0;">
                        <li>💰 Smart Emergency Fund Planning</li>
                        <li>📊 Clever Investment Strategies</li>
                        <li>🏦 Cunning Tax Optimization</li>
                        <li>🏠 Wise Retirement Planning</li>
                        <li>💳 Strategic Debt Management</li>
                        <li>📈 Credit Score Improvement</li>
                    </ul>
                </div>
                """)

        # Event handlers
        def respond(message, chat_history):
            if not message.strip():
                return "", chat_history

            response = generate_response(message, chat_history)
            chat_history.append([message, response])
            return "", chat_history

        def use_sample_prompt(prompt):
            return prompt

        def calculate_compound_interest(principal, rate, time):
            try:
                result = FinanceCalculator.compound_interest(principal, rate/100, time)
                return f"${principal:,.2f} grows to ${result:,.2f} in {time} years at {rate}% annually"
            except:
                return "Please enter valid numbers"

        # Wire up events
        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        send_btn.click(respond, [msg, chatbot], [msg, chatbot])

        # Sample prompt buttons
        for i, btn in enumerate(sample_buttons):
            btn.click(use_sample_prompt, [gr.State(SAMPLE_PROMPTS[i])], [msg])

        # Calculator
        calc_btn.click(
            calculate_compound_interest,
            [principal_input, rate_input, time_input],
            [calc_result]
        )

        # Welcome message
        interface.load(
            lambda: [["", "🦊 Hey there! I'm Foxy Finance, your clever financial advisor with the cunning wisdom of a fox! Whether you need help with savings, taxes, investments, or any financial question, I'll use my sharp instincts to guide you to financial success. Let's be clever about your money - what would you like to explore today?"]],
            outputs=[chatbot]
        )

    return interface

# Launch the application
if __name__ == "__main__":
    print("🚀 Launching Foxy Finance...")
    print("📱 Model: IBM Granite 3.2-2B")
    print("💰 Specialization: Personal Finance")
    print("🦊 Features: Savings, Taxes, Investments + Calculations")

    interface = create_interface()
    interface.launch(
        share=True,
        debug=True,
        server_name="0.0.0.0",
        server_port=7860
    )
