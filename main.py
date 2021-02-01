#!/usr/bin/env python3

from coolapk import create_app

app = create_app()

app.debug = True
app.run("0.0.0.0")
