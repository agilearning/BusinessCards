#!/usr/bin/python
 
import agilearning
 
 
@agilearning.intern
def chihcheng(**my):
    """ Learning Supervisor """
 
    assert my["name"] is "Chih-Cheng Liang"
    assert my["github"] is "http://github.com/ChihChengLiang"
    assert my["email"] is "chihchengliang@gmail.com"
    assert my["phone_number"] is "+886 921-315607"
    assert agilearning.VAT_ID is 24755908


