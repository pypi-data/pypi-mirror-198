import base64
import re
from typing import List, Dict, Union, Callable

class HELML:

    @staticmethod
    def encode(
        arr: Union[list, dict, tuple],
        url_mode: bool = False,
        val_encoder: Union[bool, Callable[[str, str], str]] = True
    ) -> str:
        """
        Encode array to HELML string.
        
        :param arr: Input data structure (list, dict, or tuple) to be encoded.
        :param url_mode: A boolean indicating if the URL mode should be used.
        :param val_encoder: A function to encode values or True for default encoding.
        :return: Encoded HELML string.
        """
        results_arr = []
        if not isinstance(arr, (list, dict, tuple)):
            raise ValueError("List or dictionary required")

        str_imp = "~" if url_mode else "\n"
        lvl_ch = "." if url_mode else ":"
        spc_ch = "_" if url_mode else " "

        HELML._encode(arr, results_arr, val_encoder, 0, lvl_ch, spc_ch)

        return str_imp.join(results_arr)
    
    @staticmethod
    def _encode(
        arr: Union[dict, list, tuple],
        results_arr: list,
        val_encoder: Union[bool, Callable[[str, str], str]] = True,
        level: int = 0,
        lvl_ch: str = ":",
        spc_ch: str = " "
    ) -> None:
        """
        Encode arr to results_arr (by reference).
        
        :param arr: Input data structure (dict, list, or tuple) to be encoded.
        :param results_arr: A list of strings representing the encoded data.
        :param val_encoder: A function to encode values or True for default encoding.
        :param level: The current level of nesting.
        :param lvl_ch: Character used for level separation.
        :param spc_ch: Character used for space.
        """

        # convert arr to dict if need
        if not isinstance(arr, dict):
            arr = {index: value for index, value in enumerate(arr)}

        for key, value in arr.items():
            if not isinstance(key, str):
                key = str(key)

            # get first char
            first_char = key[0]
            # encode key in base64url if it contains unwanted characters
            if lvl_ch in key or "~" in key or first_char == "#" or first_char == spc_ch or first_char == ' ':
                first_char = "-"
            if first_char == "-" or key[-1] == spc_ch or key[-1] == ' ' or not all(c.isprintable() for c in key):
                # add "-" to the beginning of the key to indicate it's in base64url
                key = "-" + HELML.base64url_encode(key)

            # add the appropriate number of colons to the left of the key, based on the current level
            key = lvl_ch * level + key

            if isinstance(value, (list, dict, tuple)):
                # if the value is a dictionary, call this function recursively and increase the level
                if isinstance(value, (list, tuple)):
                    key += lvl_ch
                results_arr.append(key)
                HELML._encode(value, results_arr, val_encoder,
                              level + 1, lvl_ch, spc_ch)
            else:
                # if the value is not a dictionary, run it through a value encoding function, if one is specified
                if val_encoder is True:
                    value = HELML.valueEncoder(
                        value, spc_ch)  # Default value encoder
                elif val_encoder:
                    value = val_encoder(value)
                # add the key:value pair to the output
                results_arr.append(key + lvl_ch + value)

    @staticmethod
    def decode(
        src_rows: Union[str, List[str], Dict[str, str]],
        val_decoder: Union[bool, Callable[[str, str], str]] = True
    ) -> Dict:
        """
        Decodes a HELML formatted string or list of strings into a nested dictionary.

        Args:
            src_rows: The HELML input as a string or strings-array.
            val_decoder: The custom value decoder function. For default encoder set True.

        Returns:
            Dict: The decoded nested dictionary.
        """

        lvl_ch = ":"
        spc_ch = " "
        # If the input is an array, use it. Otherwise, split the input string into an array.
        if isinstance(src_rows, (list, dict)):
            if isinstance(src_rows, dict):
                str_arr = list(src_rows)
            else:
                str_arr = src_rows

        elif isinstance(src_rows, str):
            for exploder_ch in ["\n", "\r", "~"]:
                if exploder_ch in src_rows:
                    if "~" == exploder_ch:
                        lvl_ch = "."
                        spc_ch = "_"
                    break

            str_arr = src_rows.split(exploder_ch)

        else:
            raise ValueError("Array or String required")

        # Initialize result array and stack for keeping track of current array nesting
        result = {}
        stack = []

        # array of stack stamps for delayed conversion of dict to list
        tolist = []

        # Loop through each line in the input array
        for line in str_arr:
            line = line.strip()

            # Skip empty lines and comment lines starting with '#'
            if not len(line) or line[0] == "#":
                continue

            # Calculate the level of nesting for the current line by counting the number of colons at the beginning
            level = 0
            while line[level] == lvl_ch:
                level += 1

            # If the line has colons at the beginning, remove them from the line
            if level:
                line = line[level:]

            # Split the line into a key and a value (or null if the line starts a new array)
            parts = line.split(lvl_ch, 1)
        
            key = parts[0] if parts[0] else 0
            value = parts[1] if len(parts) > 1 else None

            # Decode the key if it starts with an equals sign
            if isinstance(key, str) and key.startswith("-"):
                key = HELML.base64url_decode(key[1:])
                if not key:
                    key = "ERR"

            # Remove keys from the stack until it matches the current level
            while len(stack) > level:
                stack.pop()

            # Find the parent element in the result dictionary for the current key
            parent = result
            for parent_key in stack:
                parent = parent[parent_key]

            # If the value is null, start a new dictionary and add it to the parent dictionary
            if value is None or value == '':
                parent[key] = {}
                stack.append(key)
                if value == '':
                    tolist.append(stack.copy())
            else:
                # Decode the value if a decoder function is specified
                if val_decoder is True:
                    value = HELML.valueDecoder(value, spc_ch)
                elif val_decoder:
                    value = val_decoder(value, spc_ch)
                # Add the key-value pair to the current dictionary
                parent[key] = value

        # try convert nested arrays by keys-pathes from tolist
        for stack in tolist:
            parent = result
            for parent_key in stack[:-1]:
                parent = parent[parent_key]

            last_key = stack[-1]
            if isinstance(parent, list) and HELML.is_numeric(last_key) and int(last_key) < len(parent):
                last_key = int(last_key)
            if ((isinstance(parent, dict) and parent.get(last_key) is not None) or isinstance(last_key, int)) and isinstance(parent[last_key], dict):
                converted = [parent[last_key].get(str(i), None) for i in range(len(parent[last_key]))]
                parent[last_key] = converted
                

        # Return the result dictionary
        return result

    @staticmethod
    def valueEncoder(
        value: Union[str, int, float, bool, None],
        spc_ch: str = " "
    ) -> str:
        """
        Encodes a value into a HELML string.

        Args:
            value: The value to be encoded.
            spc_ch: The space character used for encoding. Default " ".

        Returns:
            str: The encoded HELML string.
        """

        value_type = type(value).__name__
        if value_type == "str":
            reg_str = r"^[ -~]*$"
            if spc_ch == "_": # for url-mode
                need_encode = "~" in value
            else:
                need_encode = False
                # reg_str = r"^[\p{Print}]*$"

            # if need_encode or not all(c.isprintable() for c in value) or ("_" == spc_ch and "~" in value):
            if need_encode or not re.match(reg_str, value, flags=re.UNICODE) or ("_" == spc_ch and "~" in value):
                # if the string contains special characters, encode it in base64
                return HELML.base64url_encode(value)
            elif not value or value[0] == spc_ch or value[-1] == spc_ch or value[-1] == ' ':
                # for empty strings or those that have spaces at the beginning or end
                return "'" + value + "'"
            else:
                # if the value is simple, just add one space at the beginning
                return spc_ch + value
        elif value_type == "bool":
            value = "T" if value else "F"
        elif value_type == "NoneType":
            value = "N"
        elif value_type == "float":
            value = str(value)
            if value == 'nan':
                value = 'NaN'
            elif spc_ch == "_": # for url-mode because float contain dot-inside
                return HELML.base64url_encode(value)

        return spc_ch * 2 + str(value)


    @staticmethod
    def valueDecoder(encoded_value: str, spc_ch: str = ' ') -> Union[str, int, float, bool, None]:
        """
        Decodes a HELML formatted string into its original value.

        Args:
            encoded_value (str): The HELML encoded value as a string.
            spc_ch (str, optional): The space character used for decoding. Defaults to ' '.

        Returns:
            Union[str, int, float, bool, None]: The decoded value, which can be of type str, int, float, bool, or None.
        """

        first_char = '' if not len(encoded_value) else encoded_value[0]

        if spc_ch == first_char:
            if encoded_value[:2] != spc_ch * 2:
                # if the string starts with only one space, return the string after it
                return encoded_value[1:]
            # if the string starts with two spaces, then it encodes a non-string value
            encoded_value = encoded_value[2:]  # strip left spaces
            if encoded_value == 'N':
                return None
            elif encoded_value == 'T':
                return True
            elif encoded_value == 'F':
                return False
            elif encoded_value == 'NaN':
                return float('nan')

            if HELML.is_numeric(encoded_value):
                # it's probably a numeric value
                if '.' in encoded_value:
                    # if there's a decimal point, it's a floating point number
                    return float(encoded_value)
                else:
                    # if there's no decimal point, it's an integer
                    return int(encoded_value)

            return encoded_value
        elif first_char == '"' or first_char == "'":  # it's likely that the string is enclosed in single or double quotes
            encoded_value = encoded_value[1:-1] # trim the presumed quotes at the edges and return the interior
            if first_char == "'":
                return encoded_value
            try:
                return encoded_value.encode('utf-8').decode('unicode_escape')
            except ValueError:
                return False

        # if there are no spaces or quotes at the beginning, the value should be in base64
        try:
            return HELML.base64url_decode(encoded_value)
        except ValueError:
            return encoded_value

    @staticmethod
    def base64url_encode(string: str) -> str:
         enc = base64.b64encode(string.encode())
         return enc.decode().rstrip("=").translate(str.maketrans('+/', '-_'))

    @staticmethod
    def base64url_decode(s: str) -> str:
        s += "=" * (4 - len(s) % 4)
        return base64.b64decode(s.translate(str.maketrans('-_', '+/')).encode()).decode()

    @staticmethod
    def is_numeric(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False