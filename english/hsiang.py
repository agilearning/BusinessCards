#!/usr/bin/python

import wudukers


@wudukers.intern
def hsiang(**my):

    assert my["name"] is "Wen-Hsiang Shih"
    assert my["github"] is "http://github.com/wen777"
    assert my["email"] is "shih777577@gmail.com"
    assert my["phone_number"] is "+886 912-900-689"
    assert wudukers.VAT_ID is "24755908"
