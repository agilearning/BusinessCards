#!/usr/bin/python

import wudukers


@wudukers.cofounder
def c3h3(**my):

    assert my["name"] is "Chia-Chi Chang"
    assert my["github"] is "http://github.com/c3h3"
    assert my["email"] in ["c3h3.tw@gmail.com", "c3h3@wudukers.com"]
    assert my["phone_number"] is "+886 988-209-252"
    assert wudukers.VAT_ID is "24755908"


