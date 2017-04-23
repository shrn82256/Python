from pykeyboard import PyKeyboard
from sys import argv
import pyxhook

def getText():
	f = open(file, 'r').readlines()
	i = f.index('//START\n') + 1
	j = f.index('//END\n')
	t = ''.join(f[i:j])
	return t

def typer():
	k = PyKeyboard()
	text = getText()
	k.tap_key(k.backspace_key)
	temp = 0
	
	for i in text:
		if i == '\n':
			k.tap_key(k.return_key)
			if temp != '\n':
				k.tap_key(k.home_key)
		elif i == '\t':
			k.tap_key(k.tab_key)
		else:
			k.type_string(i)
		temp = i
		k.tap_key(k.escape_key)

	k.press_key(k.shift_key)
	k.press_key(k.control_key)
	k.press_key(k.end_key)
	k.release_key(k.shift_key)
	k.release_key(k.control_key)
	k.release_key(k.end_key)
	k.tap_key(k.backspace_key)

def OnKeyPress(event):
	if event.Ascii == 96:
		typer()
		new_hook.cancel()

script, file = argv
print(file)

new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
