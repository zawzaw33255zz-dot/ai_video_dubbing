import gradio as gr
import google.generativeai as genai

def generate_dubbing(api_key, character_name, script_text):
    if not api_key:
        return "ကျေးဇူးပြု၍ Gemini API Key ထည့်ပါ။"
    try:
        # API Key ဖြင့် Gemini ကို ချိတ်ဆက်ခြင်း
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Character/Voice: {character_name}\nScript: {script_text}\n\nဒီ script အတွက် AI Dubbing / Voiceover ဇာတ်ကောင်အလိုက် စီစဉ်ပေးပါ။"
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        return f"အမှားအယွင်းရှိ습니다: {str(e)}"

# Gradio Interface တည်ဆောက်ခြင်း
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎬 AI Video Dubbing Pro (Test Version)")
    gr.Markdown("လာရောက်သုံးစွဲသူများအနေဖြင့် မိမိတို့၏ ကိုယ်ပိုင် Gemini API Key ဖြင့် အသုံးပြုနိုင်ပါသည်။")
    
    with gr.Row():
        api_key_input = gr.Textbox(label="၁။ Gemini API Key ထည့်ပါ", type="password", placeholder="AI Studio မှ API Key ထည့်ရန်")
    
    with gr.Row():
        char_input = gr.Textbox(label="၂။ အသံရွေးချယ်ရန် / ဇာတ်ကောင်", value="ကောင်လေး")
        
    with gr.Row():
        script_input = gr.Textbox(label="၃။ Script / စာသားထည့်ရန်", lines=5, placeholder="ပြောမည့် စာသား သို့မဟုတ် script ကို ဒီမှာ ရေးပါ...")
        
    output = gr.Textbox(label="ရလဒ် (Result)", lines=5)
    
    submit_btn = gr.Button("စတင်လုပ်ဆောင်မည် (Generate)", variant="primary")
    submit_btn.click(fn=generate_dubbing, inputs=[api_key_input, char_input, script_input], outputs=output)

if __name__ == "__main__":
    demo.launch()
