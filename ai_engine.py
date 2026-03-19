import json
import random
from google import genai
from google.genai import types

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("[-] Error: config.json not found.")
        exit(1)

class LogicHunterAI:
    def __init__(self):
        self.config = load_config()
        self.keys = self.config['logic_hunter_ai']['api_keys']
        self.agents = self.config['logic_hunter_ai']['agents']
        
        self.active_key = random.choice(self.keys)
        
        if self.active_key == "YOUR_REAL_API_KEY_HERE" or not self.active_key:
            print("[\033[1;31m-\033[0m] Fatal Error: Please insert a valid Gemini API key in config.json")
            exit(1)
            
        self.client = genai.Client(api_key=self.active_key)

    # الفانكشن القديمة (للسؤال السريع بدون سياق)
    def ask_agent(self, agent_role, prompt):
        model_name = self.agents.get(agent_role, {}).get("model", "gemini-2.5-flash")
        try:
            response = self.client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.2)
            )
            return response.text
        except Exception as e:
            print(f"[\033[1;31m-\033[0m] AI Error: {e}")
            return None

    # الفانكشن الجدييييدة (لفتح جلسة شات مستمرة للـ Target)
    def start_hunt_session(self, agent_role, skill_file_path=None):
        model_name = self.agents.get(agent_role, {}).get("model", "gemini-3.1-flash-lite-preview")
        
        # بنجهز شخصية الموديل
        sys_instruction = "You are LogicHunter, an elite Bug Bounty AI assistant. Be concise, technical, and accurate."
        
        # لو ملف المهارات موجود، بنحقنه في عقل الموديل
        if skill_file_path:
            try:
                with open(skill_file_path, 'r') as f:
                    skill_content = f.read()
                    sys_instruction += f"\nFollow this Bug Bounty methodology strictly:\n{skill_content}"
            except FileNotFoundError:
                pass # لو الملف مش موجود هيشتغل عادي من غيره
                
        config = types.GenerateContentConfig(
            temperature=0.2,
            system_instruction=sys_instruction
        )
        
        print(f"[\033[1;34m*\033[0m] Initializing Brain: \033[1;33m{agent_role}\033[0m (Context Loaded!)")
        
        # بنفتح الشات ونرجعه عشان logichunter.py يستخدمه
        chat_session = self.client.chats.create(
            model=model_name,
            config=config
        )
        return chat_session
