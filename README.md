# Voxel to Blueprint Converter by Fabian Vinke

## Overview

The **Voxel to Blueprint Converter** is a handy tool that converts `.vox` files from **MagicaVoxel** into `.blueprint` files for **Scrap Mechanic**. This tool allows you to directly convert voxel models into in-game blueprints, with customizable options like **scale** and **UUID**. It is developed using Python with a user-friendly GUI provided by **CustomTkinter**.

With this tool, you can:
- Select and convert multiple `.vox` files to `.blueprint` files compatible with Scrap Mechanic.
- Set a custom **scale** and **shape UUID** for your voxel creations.
- Customize the conversion with easy-to-use interface options, including appearance mode.

## Features

- **Multi-file Selection**: Convert multiple `.vox` files at once to Scrap Mechanic blueprints.
- **Customizable Scale**: Set the conversion scale for voxel models, allowing resizing during the conversion process.
- **UUID Management**: Assign custom UUIDs to voxel creations.
- **User-Friendly GUI**: The app features a straightforward GUI with CustomTkinter, making it easy to select files, set options, and run conversions.
- **Appearance Modes**: Switch between `Light`, `Dark`, and `System` appearance modes.

## Installation
To run this tool, you need **Python 3.9+** installed on your system. Additionally, you'll need the required libraries, which can be installed via pip:

```bash
pip install customtkinter midvoxio
```

## Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/21Suspect/Voxel2BlueprintConverter.git
   ```
2. **Install Dependencies**
   ```bash
   pip install customtkinter midvoxio
   ```
3. **Run the Application**
   ```bash
   python main.py
   ```
4. The **graphical user interface (GUI)** will open, allowing you to select `.vox` files, set the conversion scale, and specify the custom UUID.

## Download Voxel2BlueprintGenerator Executable

You can download the compiled executable version of Voxel2BlueprintGenerator if you prefer not to run the Python script. This version does not require Python to be installed and can be run directly on your Windows system.

- **[Download Voxel2BlueprintGenerator.exe](https://github.com/21Suspect/Voxel2BlueprintGenerator/releases/download/v1.0/Voxel2BlueprintGenerator.exe)**

## How to Use the Application

1. **Launch the Application**: Run the Python script or executable.
2. **Select .vox Files**: Click **Browse** to select `.vox` files that you wish to convert.
3. **Set Scale and UUID**: Use the slider to set a **scale** between 0.1 and 2.0 and enter a custom **UUID** for your creations.
4. **Convert**: Click on **Convert** to start the conversion. The `.blueprint` files will be saved in `C:\Program Files (x86)\Steam\steamapps\common\Scrap Mechanic\Survival\LocalBlueprints`.
5. **Appearance Settings**: Change the appearance mode to `Light`, `Dark`, or `System` using the drop-down option.

## Screenshot
![Screenshot](https://raw.githubusercontent.com/21Suspect/Voxel2BlueprintConverter/main/screenshot.png)  
(*Example of the GUI in action*)

## Configuration
The application has several configurable parameters:

- **Scale**: Adjust the scale of voxel models during conversion (from `0.1` to `2.0`).
- **Custom UUID**: Enter a custom UUID to use for the blueprint creations. This is helpful when creating custom parts for Scrap Mechanic.

## Important Information
- Converted blueprints are saved as `.blueprint` files in the directory:
  - `C:\Program Files (x86)\Steam\steamapps\common\Scrap Mechanic\Survival\LocalBlueprints`
- To spawn `.vox` files in Scrap Mechanic:
  - Add the `-dev` flag or activate developer mode.
  - Use the command `"/import voxfilename"` in Survival mode (replace `voxfilename` with the name of your original voxel file).
  - Add and delete a block to make the creation unfreeze in-game.

## Contributing
Contributions are welcome! If you encounter any bugs, have feature requests, or wish to contribute to the project, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/21Suspect/Voxel2BlueprintConverter/blob/main/LICENSE) file for details.

## Contact
For any questions or feedback, feel free to reach out to **Fabian Vinke** at [fabivinke@gmail.com](mailto:fabivinke@gmail.com).

---
Thank you for using **Voxel to Blueprint Converter**! Feel free to leave a star on the repository if you found it useful. 😊

