<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://www.sublimetext.com">Sublime Text</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
    <a href="https://github.com/catppuccin/sublime-text/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/sublime-text?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/sublime-text/issues"><img src="https://img.shields.io/github/issues/catppuccin/sublime-text?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/sublime-text/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/sublime-text?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/68803793/203905911-e9569b4c-af9b-45ef-918d-f38015f1e0f0.png"/>
</p>

## Usage

### Installation

#### Package Control

1. In Sublime Text, open the command palette with <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Windows/Linux) or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (macOS).
2. Enter `Package Control Install Package` (or just `pcip`) and select it.
4. Search for and select the *Catppuccin* package.

#### Git download

1. In Sublime Text, locate the path to the `Packages` directory through the **Preferences** > **Browse Packages...** menu.
2. From the command line, go to the previously noted directory path and clone the repository into it.

```
git clone https://github.com/catppuccin/sublime-text.git Catppuccin
```

#### Manual download

1. Download [this repsoitory as a ZIP archive](https://github.com/catppuccin/sublime-text/archive/refs/heads/main.zip).
2. Unzip into a directory named `Catppuccin`.
3. In Sublime Text, open the `Packages` directory through the **Preferences** > **Browse Packages...** menu.
4. Move the unzipped `Catppuccin` directory into the `Packages` directory.

### Activation

1. In Sublime Text, select your flavor of choice through **Preferences** > **Select Color Scheme**.
2. Go to **Preferences** > **Select Theme...** and select `Adaptive`.

## Development

### Local modifications
If you're unfamiliar with Sublime Text color scheme development, see ["Color Schemes" in the Sublime Text documentation](https://www.sublimetext.com/docs/color_schemes.html).

For local editing, you can invoke `UI: Customize Color Scheme` in the command palette to open a split-pane window with the current color scheme on the left and an override file on the right. Rules you add to your override file will be processed after the rules in the official color scheme.

If you have a specific piece of code you would like to re-color, you'll need to know what scopes are being applied to the token. (Applying scopes is done by the syntax, not the color scheme.) Position your caret over the token, and use <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (or **Tools** > **Developer** > **Show Scope Name**). Then add a rule in your color scheme override to apply a color to this token.

### Contributing modifications
1. Clone this repository and open it
2. Apply your changes to `color-scheme.json`
3. Re-build the 4 flavors in build/ with `./build.js` (requires Deno to be installed)
4. Open a Pull Request!

## 💝 Thanks to

- [BrunDerSchwarzmagier](https://github.com/BrunDerSchwarzmagier)
- [ghostx31](https://github.com/ghostx31)
- [Matthias Portzel](https://github.com/MatthiasPortzel)

&nbsp;

<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
<p align="center">Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
<p align="center"><a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>
