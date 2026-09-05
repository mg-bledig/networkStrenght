# coding=UTF-8
# networkStrenght.py
# A simple NVDA add-on to know the wireless network strenght
# Author: Rui Fontes <rui.fontes@tiflotecnia.com>
# Copyright 2020

import globalPluginHandler
import inputCore
import subprocess
from ui import message
import addonHandler

addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_announceNetworkStrenght(self, gesture: inputCore.InputGesture) -> None:
		results = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"])
		ns = str(results[results.find(b"%") - 3 : results.find(b"%") + 1])
		message(str(_("Strenght of signal is: ") + ns[2:]))

	#: Now defining a dictionary with key bindings for this plugin
	__gestures = {
		"kb:Control+NVDA+n": "announceNetworkStrenght",
	}
