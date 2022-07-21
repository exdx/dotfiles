# Darcula (IntelliJ)
Darcula theme for [Visual Studio Code](https://code.visualstudio.com) based on [IntelliJ IDEA](https://www.jetbrains.com/idea)

## Supported syntax
* Java
* JavaScript
* TypeScript
* Python
* React TSX
* Groovy
* Rust
* HTML
* CSS
* JSON
* SQL
* XML
* YAML
* Dockerfile
* Markdown
* Properties
* TOML

## Screenshots
![Java-Entity](https://github.com/rafaelrenanpacheco/darcula-theme/raw/master/screenshots/java-entity.png)

![Java-Controller](https://github.com/rafaelrenanpacheco/darcula-theme/raw/master/screenshots/java-controller.png)

![JavaScript](https://github.com/rafaelrenanpacheco/darcula-theme/raw/master/screenshots/javascript.png)

## Download
This extension is available for free in the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=rafaelrenanpacheco.darcula-theme).

## What's new?
Take a look at the [changelog](https://github.com/rafaelrenanpacheco/darcula-theme/blob/master/CHANGELOG.md).

## Theme customization
You can customize the colors to your liking, overriding the ones provided by this theme. To know how to customize, [click here](https://code.visualstudio.com/api/references/theme-color) for the official documentation.

## Contribution
It's very easy to make contributions for this project. You can follow the [official documentation](https://code.visualstudio.com/api/extension-guides/color-theme#test-a-new-color-theme) to learn more details, but to keep it short you can do this:
* Fork this project and clone to your computer.
* Open the project on Visual Studio Code.
  * If this theme is installed, disable it before following the next steps.
* Press F5 to start the `Extension Development Host` mode.
* On the development host make sure this theme is selected.
* Open a folder or a file to preview the changes you will make.
* Open the `themes/darcula.color-theme.json` where you can see the many `tokenColors` rules.
* Add new rules to improve this theme.
* Submit a PR.

In order to identify the `scope` of a token, first go to your file that you are using as reference. Then press `ctrl + shit + p`, search and execute `Developer: Inspect Editor Tokens and Scopes`. Now click on the token that you wish to customize and the inspector will show you the scopes related to that token.

## Credits
* The editor colors were based on [rokoroku/vscode-theme-darcula](https://github.com/rokoroku/vscode-theme-darcula) theme, and changed a little in order to become more like IntelliJ's.
* The token colors were made from scratch and based on IntelliJ IDEA.
