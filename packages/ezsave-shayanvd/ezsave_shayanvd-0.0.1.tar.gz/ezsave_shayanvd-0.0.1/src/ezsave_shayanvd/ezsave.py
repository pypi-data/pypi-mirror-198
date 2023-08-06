import orjson


def ezsave(data, filename, safe=True, overwrite=True, indent=4, sort_keys=False):
    # Type checking
    if data is None:
        raise ValueError("data is None")

    if filename is None:
        raise ValueError("filename is None")

    if type(filename) is not str and type(filename) is not int and type(filename) is not float:
        raise ValueError("filename is not a String or Number")

    if type(safe) is not bool:
        raise ValueError("safe is not a Boolean")

    if type(overwrite) is not bool:
        raise ValueError("overwrite is not a Boolean")

    if type(indent) is not int:
        raise ValueError("indent is not an Integer")

    if type(sort_keys) is not bool:
        raise ValueError("sort_keys is not a Boolean")

    filename = str(filename)
    temp_filename = None

    if safe:
        if "." in filename:
            file_start = "".join(filename.split(".")[:-1])
            file_end = filename.split(".")[-1]

            temp_filename = file_start + " TEMP." + file_end
        else:
            temp_filename = filename + " TEMP"

    if overwrite:
        write_mode = "w"
    else:
        write_mode = "x"

    if type(data) is dict:
        write_mode += "b"

        if indent and not sort_keys:
            json_dump = orjson.dumps(data, option=orjson.OPT_INDENT_2)
        elif indent and sort_keys:
            json_dump = orjson.dumps(data, option=orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS)
        elif not indent and sort_keys:
            json_dump = orjson.dumps(data, option=orjson.OPT_SORT_KEYS)
        else:
            json_dump = orjson.dumps(data)

        with open(filename, write_mode) as f:
            f.write(json_dump)

        if safe:
            with open(temp_filename, write_mode) as f:
                f.write(json_dump)

    elif type(data) is list:
        with open(filename, write_mode) as f:
            for item in data:
                f.write(str(item) + "\n")

        if safe:
            with open(temp_filename, write_mode) as f:
                for item in data:
                    f.write(str(item) + "\n")

    elif type(data) is str:
        with open(filename, write_mode) as f:
            f.write(data)

        if safe:
            with open(temp_filename, write_mode) as f:
                f.write(data)
