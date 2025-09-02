import gradio as gr
import base64


class FinanceCalculator:
    @staticmethod
    def compound_interest(principal, rate, time):
        """Calculate compound interest."""
        return principal * ((1 + rate) ** time)

def generate_response(message, chat_history):
    """Simulate an AI response — replace with actual LLM/API later."""
    return f"🦊 Foxy says: Great question! Here's a quick tip on that — '{message}' is important. Let's dive deeper together!"

def load_fox_image_base64(path="foxy_avatar.png"):
    try:
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Red_fox_Vulpes_vulpes_full_body_profile.jpg/320px-Red_fox_Vulpes_vulpes_full_body_profile.jpg"

# --------------------------
# App Configuration
# --------------------------

fox_image_base64 = load_fox_image_base64()

CUSTOM_CSS = """
.header-title {
    text-align: center;
    font-size: 2.5rem;
    color: orange;
    margin-bottom: 0;
}
.header-subtitle {
    text-align: center;
    color: white;
    font-size: 1.2rem;
    margin-top: 5px;
}
#foxy-avatar {
    width: 100px;
    border-radius: 50%;
    margin: auto;
    display: block;
}
.chat-container {
    background-color: #f0f0f0;
    padding: 10px;
    border-radius: 10px;
}
"""

SAMPLE_PROMPTS = [
    "How can I start saving with a low income?",
    "What are some smart investment strategies?",
    "How do I build an emergency fund?",
    "How can I reduce my taxes legally?",
    "What’s the best way to pay off credit card debt?",
    "How much do I need to retire at 60?"
]

# --------------------------
# Interface
# --------------------------

def create_interface():
    with gr.Blocks(css=CUSTOM_CSS) as interface:
        gr.HTML("<h1 class='header-title'>🦊 Foxy Finance Chatbot 🦊</h1>")
        gr.HTML("<p class='header-subtitle'>Your clever guide to personal finance with the cunning of a fox!</p>")

        with gr.Row():
            gr.HTML(f'<img src="{fox_image_base64}" id="foxy-avatar" alt="Foxy Finance Avatar">')

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

        # ---------- Event Handlers ----------

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
                result = FinanceCalculator.compound_interest(principal, rate / 100, time)
                return f"${principal:,.2f} grows to ${result:,.2f} in {time} years at {rate}% annually"
            except Exception as e:
                return f"64659: {str(e)}"

        # ---------- Wire Events ----------

        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        send_btn.click(respond, [msg, chatbot], [msg, chatbot])

        for i, btn in enumerate(sample_buttons):
            btn.click(use_sample_prompt, [gr.State(SAMPLE_PROMPTS[i])], [msg])

        calc_btn.click(
            calculate_compound_interest,
            [principal_input, rate_input, time_input],
            [calc_result]
        )

        interface.load(
            lambda: [["", "🦊 Hey there! I'm Foxy Finance, your clever financial advisor with the cunning wisdom of a fox! Whether you need help with savings, taxes, investments, or any financial question, I'll use my sharp instincts to guide you to financial success. Let's be clever about your money - what would you like to explore today?"]],
            outputs=[chatbot]
        )

    return interface



if __name__ == "__main__":
    print("🚀 Launching Foxy Finance...")
    print("📱 Model: IBM Granite 3.2-2B (Placeholder)")
    print("💰 Specialization: Personal Finance")
    print("🦊 Features: Savings, Taxes, Investments + Calculations")

    interface = create_interface()
    interface.launch(
        share=True,
        debug=True,
        server_name="127.0.0.1",
        server_port=7860
    )

