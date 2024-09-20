import cv2
from pyzbar.pyzbar import decode

def start_scanning():
    cap = cv2.VideoCapture(1)
    frame_width = 1280
    frame_height = 720
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    while cap.isOpened():
        success, frame = cap.read()

        if not success:
            print("Failed to capture image")
            break
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detectedBarcodes = decode(gray)

        for barcode in detectedBarcodes:
            barcode_data = barcode.data.decode('utf-8').strip()
            cv2.putText(frame, barcode_data, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.imwrite("code.png", frame)
            print(f"Detected Barcode: {barcode_data}")
        cv2.imshow('scanner', frame)
        if cv2.waitKey(1) == ord('p'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_scanning()
