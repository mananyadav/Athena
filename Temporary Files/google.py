#!/usr/bin/python3

import webbrowser

new = 2

tabUrl="http://google.com/?#q=";
term= input("Enter query = ");

webbrowser.open(tabUrl+term,new=new);
