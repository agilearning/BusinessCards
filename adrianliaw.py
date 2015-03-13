#!/usr/bin/python

import agilearning


@agilearning.intern
def adrianliaw(**my):
    """ Learning Reinforcer """

    assert my["name"] is "Adrian Liaw"
    assert my["github"] is "http://github.com/adrianliaw"
    assert my["email"] is "adrianliaw2000@gmail.com"
    assert my["phone_number"] is "+886 976-407095"
    assert agilearning.VAT_ID is 24755908


