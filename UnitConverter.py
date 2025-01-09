"""
Display's UI that allows user to convert a selected unit at a given value into another selected unit of the same type.
"""
import re
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from PIL import Image, ImageTk
from unit_dictionary import unit_dict


class UnitConverter:

    def __init__(self):
        """
        Creates window and necessary widgets to display and operate the Unit Converter.
        """
        self.unit_dict = unit_dict
        bg_color = "#79baf7"

        # window setup
        self.window = tk.Tk()
        self.window.title("Unit Converter")
        self.window.geometry("900x600")
        self.window.resizable(False, False)
        self.window.config(bg=bg_color)
        self.window.columnconfigure([0, 1, 2], weight=1)    # make columns equal width
        # --styling
        style = ttk.Style()
        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='clam', settings = {'TCombobox':
                                                                         {'configure':
                                                                          {'selectbackground': '#eee',
                                                                           'fieldbackground': '#eee',
                                                                           'selectforeground': 'black'
                                                                           }}})

        style.theme_use('combostyle')
        self.window.option_add("*TCombobox*Listbox*Font", tkFont.Font(family="Arial", size=16))

        # window title text
        tk.Label(self.window,
                 text = "Unit Converter",
                 justify="center",
                 bg=bg_color,
                 font=("Arial", 26)
                ).grid(row=0, columnspan=3, pady=25)
        
        # unit type dropdown
        self.unit_type = tk.StringVar()
        self.unit_type_dropdown = ttk.Combobox(self.window,
                                        width=15,
                                        font=("Arial", 16),
                                        justify="center",
                                        values=list(self.unit_dict.keys()),
                                        state="readonly",
                                        textvariable=self.unit_type
                                        )
        self.unit_type_dropdown.current(0)
        self.unit_type_dropdown.bind("<<ComboboxSelected>>", lambda *args: self.set_units(self.unit_type))
        self.unit_type_dropdown.place(x=352, y=155)

        # entry frame
        entry_frame = tk.Frame(self.window,
                               bg=bg_color
                            )
        entry_frame.grid(row=1, column=0, padx=80, pady=175, sticky="w")
        # --input box
        self.input_value = tk.StringVar()
        self.input_value.trace_add("write", lambda *args: self.limit_entry(self.input_value))
        self.input_box = tk.Entry(self.window,
                                  width=8,
                                  justify="right",
                                  font=("Monospace", 32),
                                  bg=bg_color,
                                  borderwidth=0,
                                  textvariable=self.input_value
                                )
        self.input_box.place(x=55, y=270)
        self.input_box.focus_set()
        # --input unit
        self.entry_display_units = tk.Label(entry_frame,
                                   text="km\u00B2",
                                   font=("Arial", 16),
                                   bg=bg_color
                                )
        self.entry_display_units.grid(row=0, pady=15, sticky="e")
        # --entry dropdown
        self.entry_unit = tk.StringVar()
        self.entry_dropdown = ttk.Combobox(entry_frame,
                                           width=18,
                                           font=("Arial", 16),
                                           textvariable=self.entry_unit
                                        )
        self.entry_dropdown.bind("<<ComboboxSelected>>", lambda *args: self.set_display_unit("entry"))
        self.entry_dropdown.grid(row=1)

        # divider
        # --arrows image
        arrows = Image.open("arrows.png")
        arrows = arrows.resize((20, 20), Image.LANCZOS)
        arrows = ImageTk.PhotoImage(arrows)
        # --divider frame
        divider_frame = tk.Frame(self.window,
                                 bg=bg_color
                                )
        divider_frame.grid(row=1, column=1, sticky="ew")
        # --top arrows
        arrows_top = tk.Label(divider_frame,
                              width=20,
                              height=20,
                              bg=bg_color,
                              image=arrows
                              )
        arrows_top.image = arrows
        arrows_top.grid(row=0, padx=(10, 0))
        # --convert button
        convert_button = tk.Button(divider_frame,
                                   font=("Arial", 16),
                                   text="Convert"
                                   )
        convert_button.grid(row=1, pady=10)
        # --bottom arrows
        arrows_bottom = tk.Label(divider_frame,
                                 width=20,
                                 height=20,
                                 bg=bg_color,
                                 image=arrows
                                 )
        arrows_bottom.grid(row=2, padx=(10, 0))
        # --design line
        canvas = tk.Canvas(self.window,
                            height=165,
                            width=10,
                            bg=bg_color,
                            highlightthickness=0
                            )
        canvas.place(x=445, y=390)
        canvas.create_line(6, 0, 6, 180, fill="#000", width=1)

        # result frame
        result_frame = tk.Frame(self.window,
                                     bg=bg_color
                                     )
        result_frame.grid(row=1, column=2, padx=80, pady=175, sticky="e") # parent fame
        # --output text
        self.result_text = tk.Label(self.window,
                                    width=8,
                                    text="0",
                                    font=("Monospace", 32),
                                    anchor="e",
                                    bg=bg_color
                                    )
        self.result_text.place(x=540, y=268)
        # --output unit
        self.result_display_units = tk.Label(result_frame,
                                    text="km/h",
                                    font=("Arial", 16),
                                    bg=bg_color
                                    )
        self.result_display_units.grid(row=0, pady=15, sticky="e")
        # --result dropdown
        self.result_unit = tk.StringVar()
        self.result_dropdown = ttk.Combobox(result_frame,
                                            width=18,
                                            font=("Arial", 16),
                                            textvariable=self.result_unit
                                            )
        self.result_dropdown.bind("<<ComboboxSelected>>", lambda *args: self.set_display_unit("result"))
        self.result_dropdown.grid(row=1)

        # set starting display and dropdown units
        self.set_units(self.unit_type)


    def set_display_unit(self, display_type: str) -> None:
        """
        Sets unit displayed next to either the entry input box or the result text to match the selected unit.

        Parameters:
            display_type (str): ["entry", "result"] - determines which display unit is changed.
        """
        # set entry side
        if display_type == "entry":
            self.entry_display_units.config(text=self.unit_dict[self.unit_type.get()][self.entry_unit.get()])
        # set result side
        elif display_type == "result":
            self.result_display_units.config(text=self.unit_dict[self.unit_type.get()][self.result_unit.get()])

    def set_units(self, unit_type: object) -> None:
        """
        Sets the units available in the entry and result dropdown menus, sets the default starting units,
        and sets the display units.

        Parameters:
            unit_type (obj): Text object representing the unit type selected in the unit type dropdown.
        """
        units = list(self.unit_dict[unit_type.get()].keys())
        # set dropdown units
        self.entry_dropdown["values"] = units
        self.result_dropdown["values"] = units
        # set default starting units
        self.entry_dropdown.current(0)
        self.result_dropdown.current(1)
        # set display units
        self.set_display_unit("entry")
        self.set_display_unit("result")
    
    def limit_entry(self, entry_text: object) -> None:
        """
        Disallows any character that is not a digit or "." from being entered.
        Limits max length to 8 characters.

        Parameters:
            entry_text (entry text obj): Object representing the text entered into the entry box. 
        """
        # allow only numbers and decimal for input
        if re.search(r"[^0-9.]", entry_text.get()):
            entry_text.set(entry_text.get()[:-1])
        # limit input to 8 characters
        if len(entry_text.get()) > 8:
            entry_text.set(entry_text.get()[:8])

    def run(self) -> None:
        """
        Runs the Unit Converter.
        """
        self.window.mainloop()


