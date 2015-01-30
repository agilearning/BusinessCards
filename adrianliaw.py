#!/usr/bin/python

import wudukers


@wudukers.intern
def adrianliaw(**my):

    assert my["name"] is "Adrian Liaw"
    assert my["github"] is "http://github.com/adrianliaw"
    assert my["email"] is "adrianliaw2000@gmail.com"
    assert my["phone_number"] is "+886 976-407-095"
    assert wudukers.VAT_ID is "24755908"


