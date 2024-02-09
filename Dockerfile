CMD ["python","main.py"]
FROM python
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN apt-get update && \
    apt-get install -y \
    python3-opencv \
    libgl1-mesa-glx
# RUN chmod 666 /dev/video0
RUN pip install opencv-python
RUN pip install numpy
RUN pip install matplotlib

CMD ["python","main.py"]

