import customtkinter as ctk
from tkinter import filedialog, messagebox
import json
import os
from midvoxio.voxio import vox_to_arr

# Initialize customtkinter
ctk.set_appearance_mode("System")  # Options: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")

class VoxelConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Voxel to Blueprint Converter by Fabian Vinke")
        self.geometry("730x350")
        self.resizable(True, True)

        # Variables
        self.vox_path_var = ctk.StringVar()
        self.scale_var = ctk.DoubleVar(value=0.5)
        self.uuid_var = ctk.StringVar(value='f0cba95b-2dc4-4492-8fd9-36546a4cb5aa')

        # UI Elements
        self.create_widgets()
        self.update_scale_value_label()

    def create_widgets(self):
        # File selection
        self.file_label = ctk.CTkLabel(self, text="Select .vox files:", font=("Arial", 14))
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.file_entry = ctk.CTkEntry(self, textvariable=self.vox_path_var, width=400)
        self.file_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.browse_button = ctk.CTkButton(self, text="Browse", command=self.select_vox_files)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # Scale selection
        self.scale_label = ctk.CTkLabel(self, text="Scale:", font=("Arial", 14))
        self.scale_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.scale_slider = ctk.CTkSlider(self, variable=self.scale_var, from_=0.1, to=2.0, number_of_steps=19, width=300, command=self.update_scale_value_label)
        self.scale_slider.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.scale_value_label = ctk.CTkLabel(self, text=f"{self.scale_var.get():.1f}", font=("Arial", 14))
        self.scale_value_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        # UUID input
        self.uuid_label = ctk.CTkLabel(self, text="Custom UUID:", font=("Arial", 14))
        self.uuid_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.uuid_entry = ctk.CTkEntry(self, textvariable=self.uuid_var, width=400)
        self.uuid_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        # Convert button
        self.convert_button = ctk.CTkButton(self, text="Convert", command=self.start_conversion)
        self.convert_button.grid(row=3, column=1, padx=10, pady=20, sticky="ew")

        # Appearance Mode Toggle
        self.appearance_mode_label = ctk.CTkLabel(self, text="Appearance Mode:", font=("Arial", 14))
        self.appearance_mode_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.appearance_mode_option = ctk.CTkOptionMenu(self, values=["System", "Light", "Dark"], command=self.change_appearance_mode)
        self.appearance_mode_option.set("System")
        self.appearance_mode_option.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Info button next to Appearance Mode
        self.info_button = ctk.CTkButton(self, text="Info", width=50, command=self.show_info)
        self.info_button.grid(row=4, column=2, padx=10, pady=10, sticky="w")

    def select_vox_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("MagicaVoxel Files", "*.vox")])
        self.vox_path_var.set(", ".join(file_paths))

    def start_conversion(self):
        vox_paths = self.vox_path_var.get().split(", ")
        scale = self.scale_var.get()
        shape_id = self.uuid_var.get()

        if not vox_paths or vox_paths == ['']:
            messagebox.showerror("Error", "Please select at least one .vox file!")
            return

        if not shape_id:
            messagebox.showerror("Error", "Please enter a valid UUID!")
            return

        # Call the conversion function for each selected file
        try:
            for vox_path in vox_paths:
                if os.path.exists(vox_path):
                    self.convert_voxel_to_blueprint(vox_path, scale, shape_id)
                else:
                    messagebox.showerror("Error", f"Selected .vox file does not exist: {vox_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert file: {e}")

    def convert_voxel_to_blueprint(self, vox_file, scale, shape_id):
        output_path = os.path.join(
            r"C:\Program Files (x86)\Steam\steamapps\common\Scrap Mechanic\Survival\LocalBlueprints",
            os.path.splitext(os.path.basename(vox_file))[0] + ".blueprint"
        )

        # Check if the blueprint file already exists
        if os.path.exists(output_path):
            replace = messagebox.askyesno("File Exists", f"The file {output_path} already exists. Do you want to replace it?")
            if not replace:
                return

        # Load .vox file as a numpy array using MidVoxIO
        voxel_array = vox_to_arr(vox_file)

        blueprint_data = {"bodies": [{"childs": []}], "version": 4}

        # Loop over the voxel array and convert it to blueprint format
        seen_positions = set()
        for x in range(voxel_array.shape[0]):
            for y in range(voxel_array.shape[1]):
                for z in range(voxel_array.shape[2]):
                    # Duplicate each block if scale is greater than 1.0
                    positions_to_add = [(0, 0, 0)]
                    if scale > 1.0:
                        positions_to_add = [(dx, dy, dz) for dx in range(-1, 2) for dy in range(-1, 2) for dz in range(-1, 2)]
                    color = voxel_array[x, y, z]
                    if color[3] == 0:  # Skip empty/transparent voxels
                        continue

                    # Scale the coordinates
                    for dx, dy, dz in positions_to_add:
                        scaled_x = int(x * scale) + dx
                        scaled_y = int(y * scale) + dy
                        scaled_z = int(z * scale) + dz

                    # Skip if the position is already occupied
                    if (scaled_x, scaled_y, scaled_z) in seen_positions:
                        continue

                    seen_positions.add((scaled_x, scaled_y, scaled_z))

                    # Ensure color values are integers and scaled properly (if normalized)
                    red = int(color[0] * 255) if color[0] <= 1 else int(color[0])
                    green = int(color[1] * 255) if color[1] <= 1 else int(color[1])
                    blue = int(color[2] * 255) if color[2] <= 1 else int(color[2])

                    # Convert color values to hexadecimal
                    color_hex = f'{red:02X}{green:02X}{blue:02X}'

                    block_entry = {
                        "bounds": {"x": 1, "y": 1, "z": 1},
                        "color": color_hex,
                        "pos": {"x": scaled_x, "y": scaled_y, "z": scaled_z},
                        "shapeId": shape_id,  # Custom shapeId
                        "xaxis": 1,  # Example axis
                        "zaxis": 3  # Example axis
                    }

                    blueprint_data["bodies"][0]["childs"].append(block_entry)

        # Save as a .blueprint file
        with open(output_path, 'w') as blueprint_file:
            json.dump(blueprint_data, blueprint_file, indent=4)

        messagebox.showinfo("Success", f"Conversion complete for {vox_file}!")

    def update_scale_value_label(self, *args):
        self.scale_value_label.configure(text=f"{self.scale_var.get():.1f}")

    def change_appearance_mode(self, mode):
        ctk.set_appearance_mode(mode)

    def show_info(self):
        info_text = ("The Blueprints are saved as .blueprint files in this directory: "
                     "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Scrap Mechanic\\Survival\\LocalBlueprints" "\n\n"
                     "To spawn the vox files in-game you have to add the -dev flag or activate developer mode and then "
                     "you can spawn it in Survival using \"/import voxfilename\". voxfilename is the name of the original voxel file you converted. " "\n\n"
                     "Add and delete a single block to the creation to make it unfreeze in-game.")
        messagebox.showinfo("More Information", info_text)

if __name__ == "__main__":
    app = VoxelConverterApp()
    app.mainloop()
