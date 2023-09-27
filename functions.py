from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

def draft_email(user_input, name="Orlando"):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)
    template = """
    Eres un asistente útil que redacta una respuesta de correo electrónico basada en un nuevo correo electrónico.
    Tu objetivo es ayudar al usuario a crear rápidamente una respuesta de correo electrónico perfecta.
    Mantén tu respuesta breve y concisa y imita el estilo del correo electrónico para que tu respuesta sea de manera similar y coincida con el tono.
    Comienza tu respuesta diciendo: "Hola {name}, aquí tienes un borrador para tu respuesta:". Y luego continúa con la respuesta en una nueva línea.
    Asegúrate de firmar con {signature}.
    """

    signature = f"Saludos cordiales, \n\{name}"
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Here's the email to reply to and consider any other comments from the user for reply as well: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, signature=signature, name=name)

    return response