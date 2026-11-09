import base64, os, sys
H = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(H, "plantilla.html"), encoding="utf-8").read()
s = s.replace("Domingo 16 de noviembre", "Lunes 16 de noviembre").replace("<span>Domingo</span>", "<span>Lunes</span>")
s = s.replace(',"● CUPOS LIMITADOS"', ',"● PRESENCIAL Y VIRTUAL"')
WA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1-.7-.3-1.5-.7-2.3-1.5-.6-.6-1-1.2-1.2-1.6-.1-.2 0-.4.1-.5l.4-.5.3-.4v-.5l-.8-1.9c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 2.2.9 2.6.7 3.1.6.5 0 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.5-.2z"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'
SCR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><rect x="2.5" y="4" width="19" height="13" rx="2.5"/><path d="M8 21h8M12 17v4"/><path d="M10 8.2v5l4.2-2.5z" fill="currentColor" stroke="none"/></svg>'
s = (s.replace("__ICON_WA__", WA).replace("__ICON_PIN_NAVY__", PIN.replace("currentColor", "#13294D"))
      .replace("__ICON_SCREEN_NAVY__", SCR.replace("currentColor", "#13294D")).replace("__ICON_PIN__", PIN).replace("__ICON_SCREEN__", SCR))
for n, f in [("emblema", "emblema.jpg"), ("sello", "sello.jpg"), ("wilson", "wilson.jpg"), ("santiago", "santiago.jpg"), ("yuliana", "yuliana.jpg"), ("rodrigo", "rodrigo.jpg")]:
    mime = "image/png" if f.endswith("png") else "image/jpeg"
    s = s.replace(f"__IMG_{n}__", f"data:{mime};base64," + base64.b64encode(open(os.path.join(H, f), "rb").read()).decode())
assert "__" not in s.replace("__proto__", ""), [x for x in s.split("__") if len(x) < 30][:5]
out = os.path.join(os.path.dirname(H), "index.html")
open(out, "w", encoding="utf-8").write(s)
print(out, round(len(s) / 1024), "KB")
