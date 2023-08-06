# ScrapSE

## Package description

ScrapSE downloads and manage the judgments.

Currently supported platforms: LEGGI D'ITALIA PA.

### Install scrapse
```
pip install scrapse
```
The package creates the `scrapse` folder in `/Users/your_username`, where it will save all judgments in the  
appropriate subfolders.

### How to use

#### Saving cookies - important!
```
scrapse leggitalia save-cookie 'your_cokies'
```
This command saves session cookies in a special file, containing  `your_cookie`.

#### Show filter values
```
scrapse leggitalia show-filters
```
This command shows the possible values to be assigned to sentence search filters.

#### Download the judgments
Make sure you have **saved** platform-related cookies before downloading the judgments!.
```
scrapse leggitalia scrap-judgments -l torino -s 'Sez. lavoro, Sez. V'
```
This command creates a folder in `/Users/your_username/scrapse/leggitalia` named `sez.lavoro&sez.v_torino` containing the judgments.

#### Dump judgments to json format
```
scrapse leggitalia dump-judgments -d 'folder_path'
```
This command creates the json files by saving them in the `/Users/your_username/scrapse/leggitalia/judgments_dump` folder.

#### For more help
For more information for each command.
```
command-name --help
```
