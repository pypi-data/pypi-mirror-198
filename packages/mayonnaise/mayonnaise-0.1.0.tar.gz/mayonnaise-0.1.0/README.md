# maya

<p align='center'>
    <img src='https://raw.githubusercontent.com/zeionara/maya/master/assets/logo.png'/>
</p>

**M**ultimedia **a**dapter for **y**outube **a**pi which allows to download content from youtube.

## Installation

Execute the following command to install using pip:

```sh
pip install mayonnaise
```

To create conda environment use the `environment.yml` file:

```sh
conda env create -f environment.yml
```

## Usage

To download a playlist as a collection of `mp3` files run the following command:

```sh
python -m maya pull https://www.youtube.com/playlist?list=PLyLY-SxMUzOgbhkUkru4esCxNUl3-DEtj -o assets/314 -a -u
```

To do the same but download the whole videos (picking the highest quality):

```sh
python -m maya pull https://www.youtube.com/playlist?list=PLyLY-SxMUzOgbhkUkru4esCxNUl3-DEtj -o assets/314 -a
```

If you are not downloading age-restricted videos, then option `-a` (authentication) can be omitted:

```sh
python -m maya pull https://www.youtube.com/playlist?list=PLyLY-SxMUzOgbhkUkru4esCxNUl3-DEtj -o assets/314
```
