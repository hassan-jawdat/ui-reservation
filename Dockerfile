from python:3.10-slim

RUN mkdir Ui

COPY . /Ui

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir tk DbConnect

CMD ["python", "/Ui/Control.py"]

