from tkinter import filedialog
from tkinter.font import families

import customtkinter as ctk
from loguru import logger

from preferences import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry("800x500")
        
        self.FONTS = families()
        
        self.create_layout()
        self.refresh_font()
    
    def create_layout(self):
        
        self.columnconfigure((0, 1), weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=1)
        
        ctk.CTkLabel(self, text="Text Editor", text_color=(BLACK, WHITE), font=ctk.CTkFont(MAIN_FONT, TITLE_SIZE)).grid(
            row=0, column=0, columnspan=2)
        
        self.text_box_layout()
        
        open_button = ctk.CTkButton(self, text="Open", command=self.open_content, fg_color=CLASSIC_T_COLORS,
                                    hover_color=REVERSED_T_COLORS)
        open_button.grid(row=2, column=0, padx=10, pady=10, sticky="we")
        
        save_button = ctk.CTkButton(self, text="Save", command=self.save_content, fg_color=CLASSIC_T_COLORS,
                                    hover_color=REVERSED_T_COLORS)
        save_button.grid(row=2, column=1, padx=10, pady=10, sticky="we")
    
    def text_box_layout(self):
        text_box_frame = ctk.CTkFrame(self, fg_color="transparent")
        
        menu_bar_frame = ctk.CTkFrame(text_box_frame, fg_color="transparent")
        
        self.selected_font: ctk.StringVar = ctk.StringVar(self, self.FONTS[0])
        font_selector = ctk.CTkOptionMenu(menu_bar_frame, values=self.FONTS, fg_color=CLASSIC_T_COLORS,
                                          button_color=REVERSED_T_COLORS, button_hover_color=REVERSED_T_COLORS,
                                          variable=self.selected_font)
        font_selector.pack(side="left")
        
        self.font_size = ctk.DoubleVar(self)
        if PREFERED_SELECTION_SIZE_FONT == "slider":
            selection_widget = ctk.CTkSlider(menu_bar_frame,variable=self.font_size, from_=FONT_SIZE_RANGE[0], to=FONT_SIZE_RANGE[1], fg_color=CLASSIC_T_COLORS, command=self.refresh_font,
                                             button_color=REVERSED_T_COLORS, button_hover_color=REVERSED_T_COLORS,
                                             progress_color=CLASSIC_T_COLORS)
        else:
            NotImplementedError("The selection method")
        
        selection_widget.pack(side="left")
        
        self.text_box = ctk.CTkTextbox(text_box_frame, font=("Arial", 12), border_width=5,
                                       border_color=CLASSIC_T_COLORS)
        
        self.text_box.tag_add("bold", 3, 5)
        self.text_box.tag_config("bold", )
        
        menu_bar_frame.pack(fill="x", side="top", pady=5)
        self.text_box.pack(expand=True, fill="both", pady=5)
        text_box_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    
    def save_content(self):
        content = self.text_box.get("1.0", ctk.END)
        
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        
        if not path:
            return
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
        self.title(f"Saved -{APP_NAME}")
        self.after(900, lambda: self.title(APP_NAME))
    
    def open_content(self):
        filename = filedialog.askopenfilename()
        if filename:
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    message = f.read()
                    self.text_box.delete("1.0", ctk.END)
                    self.text_box.insert(ctk.END, message)
            except FileNotFoundError as e:
                logger.error(f"An exception was be raised : {e}")
    
    def refresh_font(self, _=None):
        selected_font = self.selected_font.get()
        self.text_box.configure(True, font=(selected_font, self.font_size.get()))


if __name__ == '__main__':
    app = App()
    app.mainloop()
