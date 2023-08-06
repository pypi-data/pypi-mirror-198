import IPython
import re
def find_cell_text(expected_id):
    """
    Tìm kiếm và trả về chỉ mục của ô có ID mong đợi.

    Args:
        expected_id (str): ID của ô cần tìm.

    Returns:
        int: Chỉ mục của ô có ID mong đợi.
    """
    texts = []
    # Get a reference to the current InteractiveShell object
    shell = IPython.get_ipython()

    # Get the input history
    input_history = shell.history_manager.get_range()
    # Print the input history
    for i, (session, line_num, input_text) in enumerate(input_history):
        for line in input_text.split('\n'):
            if line.startswith('#__cell_id__: '):
                cell_id = line.strip()[len('#__cell_id__: '):]
                if cell_id == expected_id:
                    texts.append(input_text)
                    break
    if len(texts):
        return texts[-1]
    return -1


def cell_content(expected_id):
    """
    Trả về nội dung của ô có ID mong đợi mà không có những comment.

    Args:
        expected_id (str): ID của ô cần tìm.

    Returns:
        str: Nội dung của ô được xử lý (loại bỏ comment và dòng trống).
    """
    text = find_cell_text(expected_id)
    # Remove single-line comments
    pattern = re.compile(r'(?m)^\s*#.*\n')
    text = re.sub(pattern, '', text)

    # Remove multi-line comments and triple-quoted strings
    pattern = re.compile(r'(?s)(\'\'\'|""").*?\1|/\*.*?\*/')
    text = re.sub(pattern, '', text)

    # Remove blank lines
    pattern = re.compile(r'(?m)^\s*\n')
    text = re.sub(pattern, '', text)
    # Print the code without comments
    # Remove whitespace in each line
    python_code = re.sub(r'\s+', lambda m: '\n' if '\n' in m.group(0) else '', text)

    # Print the modified code
    return python_code
