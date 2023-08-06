# CleanGhostImages

The Ghost blogging platform only has a naive images system management system. Images that you upload when writing a blog
post but end-up not using are stored ad vitam aeternam without a quick way to remove them.

This package helps to find images that are not used by your blog but are still stored in your images directory, and to
delete them.

The script works by parsing a Ghost json export file, finding references to images, and comparing it with the content
of the Ghost images directory.

The script works on the assumption that this is a standard installation and that the images are in the `content/images`
directory of your Ghost installation.

This was tested with Ghost 5.39.0, and comes with no warranty. Make sure to have a backup before you remove anything.

## Usage

The code requires you to export your website in Json from the administration panel / "Export your content". You can then
use the following options:

- `--json-export-file` (required): The path to your json export file. Note that you don't need to upload it from your
  server because it will be stored in the `content/data` folder of your ghost installation
- `--ghost-dir` (required): The path to your Ghost instance (e.g. `/opt/ghost/`)
- `--print-unused-images` prints the list of all the images that are present in your content directory but not used
  in the Ghost json export
- `--print-missing-images` prints the list of all the images that are listed in your Ghost json export but are not in
  the images directory
- `--statistics` prints some information about the number of images found vs used/missing
