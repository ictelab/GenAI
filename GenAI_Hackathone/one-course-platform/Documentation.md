import os

import time

from jaseci.actions.live\_actions import jaseci\_action

from openai import OpenAI



\# Initialize OpenAI client from environment variable

client = OpenAI(api\_key=os.getenv("OPENAI\_API\_KEY"))



@jaseci\_action

def byllm\_eval(question: str, answer: str, expected: str):

&nbsp;   """

&nbsp;   Evaluates a learner's answer against an expected answer

&nbsp;   using an LLM and returns a JSON score between 0 and 1.

&nbsp;   """

&nbsp;   prompt = f"""

Evaluate the user's answer to the question.



Question: {question}

Expected: {expected}

User: {answer}



Return JSON strictly in this format:

{{"score": 0-1}}

"""



&nbsp;   response = client.responses.create(

&nbsp;       model="gpt-5.1",

&nbsp;       input=prompt

&nbsp;   )



&nbsp;   return response.output\_text





\# Keeps container alive for Jaseci to load actions

if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   print("Jaseci LLM Evaluation Action Loaded...")

&nbsp;   while True:

&nbsp;       time.sleep(3600)





…………………………………………………………………………………………………………….



**How to run** 

Dockerfile (Single Container Definition)

FROM python:3.10-slim



WORKDIR /app



**# Install dependencies**

RUN pip install --no-cache-dir jaseci openai



\# Copy single application file

COPY app.py .



ENV PYTHONUNBUFFERED=1



CMD \["python", "app.py"]



 **Build the Container**

docker build -t byllm-eval .



 **Run the Container**

docker run -d \\

&nbsp; --name byllm-eval \\

&nbsp; -e OPENAI\_API\_KEY=your\_openai\_api\_key\_here \\

&nbsp; byllm-eval



 **Load the Action in Jaseci**



Inside Jaseci:



actions load module app





**Call it:**



byllm\_eval(

&nbsp; question="What is photosynthesis?",

&nbsp; answer="Plants make food using sunlight",

&nbsp; expected="Photosynthesis is the process by which plants convert light energy into chemical energy."

)











