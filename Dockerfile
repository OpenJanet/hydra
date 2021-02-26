FROM rasa/rasa-sdk:2.0.0

WORKDIR /app

COPY requirements.txt ./

USER ROOT

RUN pip install -r requirements.txt

COPY ./actions /app/actions

RUN python -m spacy download en_core_web_md
RUN python -m spacy link en_core_web_md en

USER 1001

CMD ["start", "--actions", "actions.actions"]
