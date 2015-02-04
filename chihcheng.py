#!/usr/bin/python
 
import wudukers
 
 
@wudukers.intern
def chihcheng(**my):
 
    assert my["name"] is "Chih-Cheng Liang"
    assert my["github"] is "http://github.com/ChihChengLiang"
    assert my["email"] is "chihchengliang@gmail.com"
    assert my["phone_number"] is "+886 921-315-607"
    assert wudukers.VAT_ID is "24755908"


