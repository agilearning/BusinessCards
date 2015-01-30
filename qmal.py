#!/usr/bin/python

import wudukers


@wudukers.cofounder
def qmal(**my):

    assert my["name"] is "Yin-Chen, Liao", "Or you can call me Qmal"
    assert my["github"] is "http://github.com/dboyliao"
    assert my["email"] in ["qmalliao@gmail.com", "qmalliao@wudukers.com"]
    assert my["phone_number"] is "+886 912-110-265"
    assert wudukers.VAT_ID is "24755908"
