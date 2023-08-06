# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

from .. import adB


def get_stuff():
    return adB.get_key("NOTE") or {}


def add_note(chat, word, msg, media, button):
    ok = get_stuff()
    if ok.get(int(chat)):
        ok[int(chat)].update({word: {"msg": msg, "media": media, "button": button}})
    else:
        ok.update({int(chat): {word: {"msg": msg, "media": media, "button": button}}})
    adB.set_key("NOTE", ok)


def rem_note(chat, word):
    ok = get_stuff()
    if ok.get(int(chat)) and ok[int(chat)].get(word):
        ok[int(chat)].pop(word)
        return adB.set_key("NOTE", ok)


def rem_all_note(chat):
    ok = get_stuff()
    if ok.get(int(chat)):
        ok.pop(int(chat))
        return adB.set_key("NOTE", ok)


def get_notes(chat, word):
    ok = get_stuff()
    if ok.get(int(chat)) and ok[int(chat)].get(word):
        return ok[int(chat)][word]


def list_note(chat):
    ok = get_stuff()
    if ok.get(int(chat)):
        return "".join(f"👉 #{z}\n" for z in ok[chat])
