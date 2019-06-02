# DeezerPy
Simple wrapper for Deezer API supporting authenticated calls.

## 1) Installation
If you have Python already installed on your device, you should be all set to install DeezerPy
using pip

    pip install DeezerPy
    
## 2) Dependencies

* requests - DeezerPy requires the requests package to be installed on the system

## 3) Quick Start
Simply import 'deezerpy' to your project, create a deezerpy object and start calling
its methods passing the relevant data (i.e. album id, artist id...)

    import deezerpy
    
    album_id = "72839592"
    # album_id = "https://www.deezer.com/en/album/72839592"

    dz = deezerpy.Deezer()
    album = dz.get_album(album_id)
    print(album)

## 4) Testing environment used

Python 3.7

## 5) Reporting issues
If you find bugs, issues, or methods that could be implemented or improved,
please raise them [here](https://github.com/NcVillalobos/DeezPy/issues). Alternatively, you can contact me to my email address
'developmentvilla@gmail.com'

## 6) Feedback 

If this library is helpful for your projects, please don't hesitate reaching out
at 'developmentvilla@gmail.com', any feedback is highly appreciated.


