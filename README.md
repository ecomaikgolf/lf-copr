# lf

## Description

lf is a terminal file manager written in Go with a heavy inspiration from ranger file manager.

No downstream patches, built with `env CGO_ENABLED=0 go build -ldflags="-s -w"`

## Installation Instructions

```
dnf copr enable ecomaikgolf/lf
dnf install lf
```

Create an issue [1] to mark package as outdated. Report lf related issues to upstream. Report package issues (rare) on [1] too.

[1] https://github.com/ecomaikgolf/lf-copr
