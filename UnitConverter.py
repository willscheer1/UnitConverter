"""
Display's UI that allows user to convert a selected unit at a given value into another selected unit of the same type.
"""
import re
import Units
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from PIL import Image, ImageTk
from decimal import Decimal


class UnitConverter:

    def __init__(self):
        """
        Creates window and necessary widgets to display and operate the Unit Converter.
        """
        bg_color = "#79baf7"

        # window setup
        self.window = tk.Tk()
        self.window.title("Unit Converter")
        self.window.geometry("900x600")
        self.window.resizable(False, False)
        self.window.config(bg=bg_color)
        self.window.columnconfigure(0, weight=1)    # make columns equal width
        # --styling
        self.input_size = 8
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
                ).grid(row=0, pady=25)
        
        # unit type dropdown
        self.unit_type = tk.StringVar()
        self.unit_type_dropdown = ttk.Combobox(self.window,
                                        width=15,
                                        font=("Arial", 16),
                                        justify="center",
                                        values=Units.types(),
                                        state="readonly",
                                        textvariable=self.unit_type
                                        )
        self.unit_type_dropdown.current(0)
        self.unit_type_dropdown.bind("<<ComboboxSelected>>", lambda *args: self.set_units(self.unit_type))
        self.unit_type_dropdown.grid(row=1, pady=(50, 0))

        # main frame
        main_frame = tk.Frame(self.window,
                              bg=bg_color
                              )
        main_frame.grid(row=2, sticky="nsew", padx=25)
        main_frame.columnconfigure([0, 1, 2], weight=1)

        # entry frame
        entry_frame = tk.Frame(main_frame,
                               bg=bg_color
                               )
        entry_frame.grid(row=0, column=0, pady=85, sticky="nw")
        # --input frame
        input_frame = tk.Frame(entry_frame,
                               bg=bg_color
                               )
        input_frame.grid(row=0, pady=10)
        # --input box
        self.input_value = tk.StringVar(value="1")
        self.input_value.trace_add("write", lambda *args: self.limit_entry(self.input_value))
        self.input_box = tk.Entry(input_frame,
                                  width=self.input_size,
                                  justify="right",
                                  font=("Monospace", 32),
                                  bg=bg_color,
                                  borderwidth=0,
                                  textvariable=self.input_value,
                                  
                                )
        self.input_box.grid(row=0, column=0)
        self.input_box.focus_set()
        # --input unit
        self.entry_display_units = tk.Label(input_frame,
                                   font=("Arial", 16),
                                   bg=bg_color
                                )
        self.entry_display_units.grid(row=0, column=1, padx=10, pady=(15, 0))
        # --entry dropdown
        self.entry_unit = tk.StringVar()
        self.entry_dropdown = ttk.Combobox(entry_frame,
                                           width=20,
                                           font=("Arial", 16),
                                           state="readonly",
                                           textvariable=self.entry_unit
                                        )
        self.entry_dropdown.bind("<<ComboboxSelected>>", lambda *args: self.update("entry"))
        self.entry_dropdown.grid(row=1, padx=22)

        # arrows image
        arrows = Image.open("arrows.png")
        arrows = arrows.resize((20, 20), Image.LANCZOS)
        arrows = ImageTk.PhotoImage(arrows)

        # divider frame
        divider_frame = tk.Frame(main_frame,
                                 bg=bg_color
                                )
        divider_frame.grid(row=0, column=1)
        # --design line top
        line_top = tk.Canvas(divider_frame,
                             height=55,
                             width=10,
                             bg=bg_color,
                             highlightthickness=0
                             )
        line_top.create_line(6, 0, 6, 55, fill="#000", width=1)
        line_top.grid(row=0, pady=25)
        # --top arrows
        arrows_top = tk.Label(divider_frame,
                              width=20,
                              height=20,
                              bg=bg_color,
                              image=arrows
                              )
        arrows_top.image = arrows
        arrows_top.grid(row=1, padx=(10, 0))
        # --convert button
        convert_button = tk.Button(divider_frame,
                                   font=("Arial", 16),
                                   text="Convert",
                                   command=self.set_result
                                   )
        convert_button.grid(row=2, pady=10)
        self.window.bind("<Return>", lambda e: convert_button.invoke())
        # --bottom arrows
        arrows_bottom = tk.Label(divider_frame,
                                 width=20,
                                 height=20,
                                 bg=bg_color,
                                 image=arrows
                                 )
        arrows_bottom.grid(row=3, padx=(10, 0))
        # --design line bottom
        line_bottom = tk.Canvas(divider_frame,
                           height=165,
                           width=10,
                           bg=bg_color,
                           highlightthickness=0
                           )
        line_bottom.create_line(6, 0, 6, 180, fill="#000", width=1)
        line_bottom.grid(row=4, pady=(25, 0))
        
        # result frame
        result_frame = tk.Frame(main_frame,
                                bg=bg_color
                                )
        result_frame.grid(row=0, column=2, pady=85, sticky="ne")
        # --output frame
        output_frame = tk.Frame(result_frame,
                                bg=bg_color
                                )
        output_frame.grid(row=0, pady=8)
        # --output text
        self.result_text = tk.Label(output_frame,
                                    width=self.input_size,
                                    font=("Monospace", 32),
                                    anchor="e",
                                    bg=bg_color
                                    )
        self.result_text.grid(row=0, column=0, sticky="e")
        # --output unit
        self.result_display_units = tk.Label(output_frame,
                                    font=("Arial", 16),
                                    bg=bg_color
                                    )
        self.result_display_units.grid(row=0, column=1, padx=10, pady=(15, 0))
        # --result dropdown
        self.result_unit = tk.StringVar()
        self.result_dropdown = ttk.Combobox(result_frame,
                                            width=20,
                                            font=("Arial", 16),
                                            state="readonly",
                                            textvariable=self.result_unit
                                            )
        self.result_dropdown.bind("<<ComboboxSelected>>", lambda *args: self.update("result"))
        self.result_dropdown.grid(row=1, padx=29)

        
        self.set_units(self.unit_type)  # set starting display and dropdown units
        self.set_result()               # set default result text


    def set_display_unit(self, display_type: str) -> None:
        """
        Sets unit displayed next to either the entry input box or the result text to match the selected unit.

        Parameters:
            display_type (str): ["entry", "result"] - determines which display unit is changed.
        """
        # set entry side
        if display_type == "entry":
            self.entry_display_units.config(text=Units.symbol(self.entry_unit.get()))
        # set result side
        elif display_type == "result":
            self.result_display_units.config(text=Units.symbol(self.result_unit.get()))

    def set_units(self, unit_type: object) -> None:
        """
        Sets the units available in the entry and result dropdown menus, sets the default starting units,
        and sets the display units.

        Parameters:
            unit_type (obj): Text object representing the unit type selected in the unit type dropdown.
        """
        units = Units.units(unit_type.get())
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

    def format_result(self, result: Decimal) -> str:
        """
        Converts and formats result number into a string value of the proper length.

        Parameters:
            result (Decimal): Numerical result of the unit conversion.
        Returns:
            (str): Result as string, either rounded or converted to scientific notation to fit into output box.
        """
        result_string = str(result)

        # long int value - scientific notation
        if result >= 10**self.input_size:
            result_string = "{:.3e}".format(result)

        # small decimal (max 3 leading 0's) - scientific notation
        elif result < 10**-4:
            result_string = "{:.3e}".format(result)
        
        # non-scientific notation results
        else:
            # non-decimal int
            if (result >= 1 and result % 1 == 0) or len(str(int(result))) == self.input_size:
                result_string = str(round(result))
            # decimal
            else:
                num_decimals = self.input_size - len(str(int(result))) - 1
                result_string = str(round(result, num_decimals)).rstrip("0")

        # remove trailing 0's in scientific notation value
        if re.search("e", result_string):
            base, exp = result_string.split("e")
            result_string = base.rstrip("0.") + "e" + exp[0] + exp[1:].lstrip("0")

        return result_string
        
    def update(self, display_type: str) -> None:
        """
        Changes display units for the given display type and updates output value.

        Parameters:
            display_type (str): ["entry", "result"] - determines which display units are updated.
        """
        # set display units
        self.set_display_unit(display_type)
        # update result text
        if self.input_value.get():
            self.set_result()

    def set_result(self) -> None:
        """
        Gets result of unit conversion and sets result text to that value.
        """
        result = Decimal(Units.convert(float(self.input_value.get()), self.entry_unit.get(), self.result_unit.get()))
        self.result_text["text"] = self.format_result(result)

    def run(self) -> None:
        """
        Runs the Unit Converter.
        """
        self.window.mainloop()


