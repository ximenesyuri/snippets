# About

`mnt` is a helper bash function to deal with mountpoints.

# Install

Just source `mnt` in your `.bashrc`.

# Dependencies

1. `jq`
2. `bash`

# Usage

1. `mnt list`: list the user created mountpoints
2. `mnt new`: creates a new mountpoint
3. `mnt rm`: remove a mountpoint

The script includes a completion script:

1. `mnt <tab>`: suggests `list new rm`
2. `mnt new <tab>`: suggests the user inserted disks that were not mounted
3. `mnt rm <tab>`: suggests  the user mounted disks

# How it works

It is essentially a wrapper for the builtin commands `mount` and `umount` with the completion scripts constructed from `lsblk --json`.
