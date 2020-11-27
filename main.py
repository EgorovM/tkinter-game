import copy
import tkinter as tk

from game import events

def start_event(event_number):
    event = events[event_number]
    lbl_text["text"] = event['text']
    
    for widget in frm_buttons.winfo_children():
        widget.destroy()
        
    for action, event_number in zip(event['actions'], event['next_event']):
        btn_choice = tk.Button(
            master=frm_buttons,
            text=action,
            command=lambda num=event_number: start_event(num))
        
        btn_choice.pack(side=tk.LEFT, padx=5)
        
    
def start_game():
    start_event(1)
        
window = tk.Tk()

frm_character = tk.Frame(master=window)

img_character = tk.Label(
    master=frm_character,
    text='Изображение'
)

img_character.grid(row=0, column=0)

frm_character_statistic = tk.Frame(master=frm_character)

lbl_health = tk.Label(master=frm_character_statistic, text='Здоровье')
lbl_health_value = tk.Label(master=frm_character_statistic, text='100')
lbl_health.grid(row=0, column=0)
lbl_health_value.grid(row=0, column=1)

lbl_health = tk.Label(master=frm_character_statistic, text='Мана')
lbl_health_value = tk.Label(master=frm_character_statistic, text='100')
lbl_health.grid(row=1, column=0)
lbl_health_value.grid(row=1, column=1)

frm_character_statistic.grid(row=0, column=1)
frm_character.pack()

frm_game = tk.Frame(master=window)

lbl_text = tk.Label(master=frm_game, height=20, relief=tk.SUNKEN, borderwidth=2)
lbl_text.pack(fill=tk.X)

frm_buttons = tk.Frame(master=frm_game)

frm_buttons.pack(padx=5, pady=5)
frm_game.pack(fill=tk.X)

start_game()

window.mainloop()
