import sys
sys.path.append("..")

import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    pix_obj = Pix()


    payment_info = pix_obj.create_payment("../")

    assert "bank_payment_id" in payment_info
    assert "qr_code" in payment_info

    qr_code_path = payment_info['qr_code']

    assert os.path.isfile(f"../static/img/{qr_code_path}.png")

