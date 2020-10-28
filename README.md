# KivyMD Components

<img align="left" width="200" src="https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymd-components-logo.png"/>


Script for installing additional components for the `KivyMD` library.

Components is a project to centralize addons for KivyMD maintained by users.
All the components packages are centralized on the [kivymd-components](https://github.com/kivymd-components) Github repository.

The components are contributed by regular users such as yourself. The KivyMD developers do not take any responsibility for the code
hosted in the component organization repositories - we do not actively monitor these repos.

Please use at your own risk.

### Author

`Kivy Team` and other contributors.

### Installation

`pip install kivymd-components`

### Usage

`componemts install package`

### Legacy components tool instructions

Component is now distributed as a separate Python module, kivymd-components.
You can install it with pip:

    pip install kivymd-components

The components does not initially include any packages. You can download
them with the component tool installed by the pip package:

    # Installing a components
    components install SweetAlert

    # Upgrade a components
    components install --upgrade SweetAlert

    # Uninstall a components
    components uninstall SweetAlert

    # List all the components installed
    components list

    # Show the help
    components --help

All the components are installed by default in `~/.kivymd/components`.

### Packaging

If you want to include components in your application, you can add `--app`
to the `install` command. This will create a `libs/components` directory in your
current directory which will be used by `kivymd.components`. For example:

```bash
    cd myapp
    components install --app SweetAlert
 ```
