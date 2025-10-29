# FyUTILS

Welcome to the [FyUTILS](https://github.com/noahonfyre/FyUTILS) wiki page!

We’ll walk you through the installation process of FyUTILS, how to customize your instance, and several ways to extend it.

# Table of Contents

<!-- TOC -->
* [FyUTILS](#fyutils)
* [Table of Contents](#table-of-contents)
* [Disclaimer](#disclaimer)
* [Installation](#installation)
    * [Troubleshooting Guide](#troubleshooting-guide)
  * [Used in FyUTILS](#used-in-fyutils)
    * [Languages](#languages)
    * [Tools](#tools)
  * [Terms of Service](#terms-of-service)
  * [Credits and Acknowledgement](#credits-and-acknowledgement)
<!-- TOC -->

# Disclaimer

By proceeding, you acknowledge that you have read, understood, and agreed to comply with our [terms and conditions](#terms-of-service). Failure to adhere to these terms may result in legal consequences. If you do not agree with these terms, refrain from downloading, installing, or using FyUTILS.

# Installation

To install FyUTILS, ensure you're running the latest versions of Windows and Windows Terminal. Also, you should be using an account with administrator permissions.

1. **Setting up the execution policy:**
   Open your PowerShell and paste the following command to bypass the remote code execution policy. This step is necessary for the installation to proceed.
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass -Force
   ```

2. **Installing FyUTILS:**
   Execute the following command in the current PowerShell session to start the installation:
   ```powershell
   irm https://noahonfyre.github.io/FyUTILS/get.ps1 | iex
   ```

3. **Starting FyUTILS:**
   To run FyUTILS, execute the `fyutils` command in a new shell session.


### Troubleshooting Guide
If something doesn't work, or you can't get FyUTILS to start, try the following steps:

1. **Restart your shell sessions:**

   Ensure you restart all your shell sessions. This includes closing all instances of PowerShell and Command Prompt, as they need to register the update to the system variables.

2. **Restart your PC:**

   If restarting the shell sessions doesn't resolve the issue, try restarting your PC. This will force all processes to restart and retrieve the most recent system variables.

3. **Check your PATH variable:**

   Open your search bar and search for `PATH`. Click on the section `Environment Variables`. Check the `PATH` variable for the path `C:\\Users\\%USERNAME%\\.fyutils`. If the path doesn't exist, add it to the variable.

4. **Standalone EXE:**

   If you only want to run FyUTILS standalone, just download the [latest release](https://github.com/noahzeisberg/fyutils/releases/latest).

## Terms of Service
FyUTILS is designed exclusively for ethical, legal, and authorized purposes.
If you want to test a system for vulnerabilities, make sure you are authorized to do so.
You can do so by either being the owner of the system or by getting explicit permission from the administrators.
You are fully responsible for everything you do with this tool.
The developers and contributors are not responsible for your actions.

## Credits and Acknowledgement
A huge thank you to all [contributors](https://github.com/noahzeisberg/FyUTILS/graphs/contributors) of this project and also to JetBrains for providing me with their [Open Source License](https://www.jetbrains.com/community/opensource/).

Without you, this project wouldn't be possible. ♥️
