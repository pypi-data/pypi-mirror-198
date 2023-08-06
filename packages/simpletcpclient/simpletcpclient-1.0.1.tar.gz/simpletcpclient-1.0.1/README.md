# Simple TCP Client

[![pipeline status](https://gitlab.cylab.be/cylab/simpletcpclient/badges/main/pipeline.svg)](https://gitlab.cylab.be/cylab/simpletcpclient/-/commits/main)
[![Latest Release](https://gitlab.cylab.be/cylab/simpletcpclient/-/badges/release.svg)](https://gitlab.cylab.be/cylab/simpletcpclient/-/releases)

A simple interactive TCP client, written in Python. Basically a simple python version of netcat.

## Installation

```bash
pip3 install simpletcpclient
```

## Usage

```bash
simpletcpclient <server> <port>
```

Simple TCP client also has built-in **autocomplete**, activated using the ```tab``` key. It currently supports basic HTTP and SMTP commands: ```GET```, ```Host:```, ```MAIL FROM:```, ```RCPT TO:``` etc.

![Simple TCP Client](./stc.png)
