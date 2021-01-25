#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests
from os import path
from progress.bar import Bar


if path.exists("wp_plugins.txt"):
    w = open("wp_plugins.txt", "r")
    w = w.read().split("\n")
    #print(w)
    lista = []
    url = "http://pnaw2.morenojose.com/"
    b = Bar("Espere...", max=len(w))

    for plugin in w:
        b.next ()
        try:
            p = requests.get(url=url+"/"+plugin)
            if p.status_code == 200:
                final = url+"/"+plugin
                lista.append(final.split("/")[-2])
        except:
            pass
    b.finish()
    for plugin in lista:
        print("Plugin encontrado: {}".format(plugin))

else:
    print("No se encuentra la lista")