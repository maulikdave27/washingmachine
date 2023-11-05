import tkinter as tk
from tkinter import ttk
import time

class WashingMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Washing Machine Simulation")

        self.water_level_label = ttk.Label(root, text="Water Level:")
        self.water_level_label.pack()

        self.water_level_entry = ttk.Entry(root)
        self.water_level_entry.pack()

        self.spin_cycles_label = ttk.Label(root, text="Spin Cycles:")
        self.spin_cycles_label.pack()

        self.spin_cycles_entry = ttk.Entry(root)
        self.spin_cycles_entry.pack()

        self.rinse_cycles_label = ttk.Label(root, text="Rinse Cycles:")
        self.rinse_cycles_label.pack()

        self.rinse_cycles_entry = ttk.Entry(root)
        self.rinse_cycles_entry.pack()

        self.start_button = ttk.Button(root, text="Start", command=self.start_washing)
        self.start_button.pack()

        self.progress_bar = ttk.Progressbar(root, length=200, mode='determinate')
        self.progress_bar.pack()

        self.status_label = ttk.Label(root, text="")
        self.status_label.pack()


        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_washing)
        self.stop_button.pack()

        self.is_washing = False

        # Durations for each stage
        self.durations = {
            'filling': 2,
            'washing': 5,
            'rinse': 3,
            'spin': 4,
        }

    def start_washing(self):
        if not self.is_washing:
            water_level = self.water_level_entry.get()
            spin_cycles = self.spin_cycles_entry.get()
            rinse_cycles = self.rinse_cycles_entry.get()

            if not water_level or not spin_cycles or not rinse_cycles:
                self.status_label.config(text="Please enter all values")
                return

            water_level = int(water_level)
            spin_cycles = int(spin_cycles)
            rinse_cycles = int(rinse_cycles)

            self.is_washing = True
            self.start_button.config(state=tk.DISABLED)

            for stage in ['filling', 'washing', 'rinse', 'spin']:
                self.update_status(f"{stage.capitalize()} in progress", water_level)

                # Simulate each stage
                time.sleep(self.durations[stage])

                if stage == 'rinse':
                    for cycle in range(1, rinse_cycles + 1):
                        self.update_status(f"Rinse cycle {cycle} of {rinse_cycles}", water_level)
                        time.sleep(self.durations[stage])

                if stage == 'spin':
                    for cycle in range(1, spin_cycles + 1):
                        self.update_status(f"Spin cycle {cycle} of {spin_cycles}", water_level)
                        time.sleep(self.durations[stage])

            self.status_label.config(text="Washing finished")
            self.progress_bar.stop()
            self.is_washing = False
            self.start_button.config(state=tk.NORMAL)

    def stop_washing(self):
        if self.is_washing:
            self.status_label.config(text="Washing stopped")
            self.progress_bar.stop()
            self.is_washing = False
            self.start_button.config(state=tk.NORMAL)

    def update_status(self, message, water_level):
        self.status_label.config(text=message)
        self.progress_bar.step(25)  # Increment progress bar
        self.root.update_idletasks()  # Update the GUI to show changes
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = WashingMachineApp(root)
    root.mainloop()
