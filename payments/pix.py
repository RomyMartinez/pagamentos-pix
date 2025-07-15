import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        #criar pagamento na instuição financeira
        bank_payment_id = str(uuid.uuid4())
        
        #qr code
        hash_payment = f"hash_{bank_payment_id}"

        img = qrcode.make(hash_payment)
        img.save(f"{base_dir}static/img/qr_code_payment_{bank_payment_id}.png")


        return {
            "bank_payment_id": bank_payment_id,
            "qr_code": f"qr_code_payment_{bank_payment_id}"
        }