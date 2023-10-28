from flask import Flask, render_template, request, send_file
import qrcode
import os
import uuid
import datetime

app = Flask(__name__)

# A dictionary to store the expiration time for each QR code image
qr_code_expiration = {}

# Directory to store QR code images
qrcodes_directory = "static/qrcodes"
os.makedirs(qrcodes_directory, exist_ok=True)  # Ensure the directory exists


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data_to_encode = request.form['data']
    img_path, unique_id = generate_qr_code(data_to_encode)

    # Set the expiration time (e.g., 10 minutes from now)
    expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    qr_code_expiration[unique_id] = expiration_time

    # Send the file for display and download
    return render_template('index.html', qr_code_path=img_path, unique_id=unique_id)


@app.route('/download_qr/<unique_id>')
def download_qr(unique_id):
    # Check if the unique_id is still valid
    if unique_id not in qr_code_expiration or datetime.datetime.now() > qr_code_expiration[unique_id]:
        return "QR code not found or expired."

    img_path = os.path.join(qrcodes_directory, f"{unique_id}.png")
    return send_file(img_path, as_attachment=True, download_name=f'{unique_id}.png')


def generate_qr_code(data):
    unique_id = str(uuid.uuid4())
    img_path = os.path.join(qrcodes_directory, f"{unique_id}.png")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(img_path)

    return img_path, unique_id


if __name__ == '__main__':
    app.run(debug=True)
