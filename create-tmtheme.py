#!/usr/bin/env python

from json2html import *
import json

def main():
    f = open('Catppuccin.sublime-color-scheme','r')
    theme = json.load(f)
    colors = theme['variables']
    globals = theme['globals']
    rules = theme['rules']
    f.close()

    header = """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>name</key>
        <string>Catppuccin</string>
        <key>settings</key>
        <array>"""

    footer = """
        </array>
        <key>uuid</key>
        <string>4d0379b5-ef82-467b-b8b8-365889420646</string>
        <key>colorSpaceName</key>
        <string>sRGB</string>
        <key>semanticClass</key>
        <string>theme.dark.Catppuccin</string>
        <key>author</key>
        <string>BrunDerSchwarzmagier</string>
    </dict>
    </plist>"""

    # Global settings
    body = """
        <dict>
            <key>settings</key>
            <dict>"""

    for k,v in globals.items():
        if 'var' not in v: continue
        k = getCamelCase(k)
        v = colors[getVar(v)]

        body = body + f"""
                <key>{k}</key>
                <string>{v}</string>"""

    body = body + """
            </dict>
        </dict>"""

    # Scope settings
    for rule in rules:
        if 'name' not in rule: continue

        name = f"""
                <key>name</key>
                <string>{rule['name']}</string>"""

        scope = f"""
                <key>scope</key>
                <string>{rule['scope']}</string>"""

        settings = """
                <key>settings</key>
                <dict>"""

        for k,v in rule.items():
            if k in ['name','scope']: continue
            k = getCamelCase(k)
            if 'var' in v: v = colors[getVar(v)]
            settings = settings + f"""
                    <key>{k}</key>
                    <string>{v}</string>"""
        
        settings = settings + """
                </dict>"""

        body = body + """
            <dict>""" \
             + name \
             + scope \
             + settings \
             + """
             </dict>"""

    output = header + body + footer

    f = open('Catppuccin.tmTheme','w')
    f.write(output)
    f.close()

"""
We need camelCase keys for .tmTheme, 
but .sublime-color-scheme uses snake_case.
"""
def getCamelCase(k):
    k0, *kN = k.split('_')
    return ''.join([k0.lower(), *map(str.title, kN)])

"""
Strip var() from the name of a variable
so we can get the hex code from the string.
"""
def getVar(v):
    return v[v.find('var(')+4:v.find(')')].strip()

if __name__ == '__main__':
    main()