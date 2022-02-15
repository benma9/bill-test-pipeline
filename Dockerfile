From python
RUN pip install flask
copy app.py /app
expose 19999
cmd python3 /app/app.py
