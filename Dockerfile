FROM pytorch/pytorch:2.2.0-cuda11.8-cudnn8-runtime

RUN pip install matplotlib pillow numpy tqdm opencv-python-headless

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p data/portra data/digital output checkpoints

ENV PYTHONPATH=/app

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]