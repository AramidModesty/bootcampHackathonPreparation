#Archivo por Aramid Monsalve
import os
from dotenv import load_dotenv
from openai import OpenAI

# Carga el archivo con tu clave api .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key,
                base_url="https://openrouter.ai/api/v1")
def getFreeModels():
    models = client.models.list()
    freemodels=[]
    for model in models.data:
        if(model.id.find('free')!=-1):
            freemodels.append(model.id)
    return freemodels
def message(text:str,role:str,
            idModel:str,tools:list[dict]
            ):
    if role not in {"system", "user", "assistant"}:
        raise ValueError(f"Invalid role: {role}")
    print(idModel)
    chat= client.chat.completions.create(
        model=idModel,
        messages=[
            {
            "role":role,
            "content":text,
            "tools":tools
            }
        ]
    )
    return chat
def sampleConversation():
    model=getFreeModels()[0]
    answer=message("Who are you?",
                   "system",
                   model)
    print(answer.choices[0].message.content)
    return answer
import analyst
get_dataframe=analyst.getDataframe
if __name__=="__main__":
    print("Hola mundo")
    print(analyst)
    print(sampleConversation())
