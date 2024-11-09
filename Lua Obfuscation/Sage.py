import base64

def obfuscate_lua(lua_code):
    obfuscated_code = []
    for line in lua_code.split('\n'):
        for char in line:
            obfuscated_code.append(str(ord(char)))
        obfuscated_code.append('10')  # ASCII code for newline character
    obfuscated_str = 'string.char(' + ','.join(obfuscated_code) + ')'
    return obfuscated_str

def main():
    print("Enter Lua Code. Press Enter to execute the code. To exit, press Ctrl+D (or Ctrl+Z on Windows).")
    
    input_lines = []
    try:
        while True:
            line = input()
            if line.strip() == 'loadstring(string.char(4,10))()':
                print("Exiting the script due to special input.")
                break
            input_lines.append(line)
            input_lua = '\n'.join(input_lines)
            obfuscated_lua = obfuscate_lua(input_lua)
            obfuscated_lua = "loadstring(" + obfuscated_lua + ")()"
            print("\n")
            print("\n")
            print(obfuscated_lua)
            print("\n")
            print("\n")
    except EOFError:
        pass
    
    if not input_lines:
        print("No input provided.")
        return
    
    input("Press anything to exit")

if __name__ == "__main__":
    main()
