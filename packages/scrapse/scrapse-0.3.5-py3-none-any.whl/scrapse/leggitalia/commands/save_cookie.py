from pathlib import Path


def save_cookie(cookie: str):
    """
        Save session cookies in order to extract judgments
    """
    file_path = '/'.join([str(Path.cwd().absolute()), 'ldi_cookie.txt'])
    output_file = Path(file_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(str(cookie))
