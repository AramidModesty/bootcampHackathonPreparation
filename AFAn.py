#Welcome to the asistant for analysis, also called AFAn, made by Aramid
from openai import OpenAI
client= OpenAI(api_key="[apikey]",#Replace this [apikey] with your own api key
               base_url="https://openrouter.ai/api/v1")
def getFreeModels():
    models = client.models.list()
    freemodels=[]
    for model in models.data:
        if(model.id.find('free')!=-1):
            freemodels.append(model.id)
    return freemodels
models = None
def methodsToTools(library):
    for i in library:
        if(i.isinstance(object)):
            print(i)
            tools=i
    return tools
def message(text:str,role:str,
            idModel:str
            ):
    print(idModel)
    chat= client.chat.completions.create(
        model=idModel,
        messages=[
            {
            "role":role,
            "content":text
            }
        ]
    )
    return chat
def sampleConversation():
    model=getFreeModels()[0]
    answer=message("Who are you?",
                   "data analyst",
                   model,
                   analyst)
    print(answer.choices[0].message.content)
    return answer
import analyst
print(True==("freedom".find('free')!=-1))
if __name__=="__main__":
    print("Hello world")
    print(analyst)
    print(sampleConversation())
    
    
