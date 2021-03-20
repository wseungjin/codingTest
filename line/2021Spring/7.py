import re

# flag rules를 객체에 매핑해서 쉽게 사용
# alias 규칙을 추가해서 얼라이싱의 경우 변환해서 사용할 수 있도록 alias rules 추가


def parse_rules(flag_rules):
    rules = {}
    alias_rules = {}
    alias_pairs = []
    for flag_rule in flag_rules:
        flag_name = flag_rule.split(" ")[0].replace("-", "")
        flag_argument_type = flag_rule.split(" ")[1]

        if flag_argument_type == "ALIAS":
            alter_flag_name = flag_rule.split(" ")[2].replace("-", "")
            alias_pairs.append((flag_name, alter_flag_name))
        else:
            rules[flag_name] = flag_argument_type

    # 새로 alias 규칙을 찾아서 넣어줍니다.
    for key in rules:
        for alias_pair in alias_pairs:
            if key == alias_pair[0]:
                alias_rules[alias_pair[1]] = key
            if key == alias_pair[1]:
                alias_rules[alias_pair[0]] = key

    return [rules, alias_rules]

# alias 되어 있다면 오리진으로 변환


def alias_to_origin(flag_name, alias_rules):
    for key in alias_rules:
        if key == flag_name:
            return alias_rules[key]
    return flag_name

# 커맨드를 파싱해 원하는 형태로 만듭니다.


def parse_command(command):
    first_parsed_command = command.split(" -")
    command_program = first_parsed_command[0]

    flag_array = []
    for flag_sentence in first_parsed_command[1:]:
        splited_flag_sentence = flag_sentence.split(" ")
        flag_array.append(
            (splited_flag_sentence[0], splited_flag_sentence[1:]))

    return (command_program, flag_array)

# 프로그램명이 옳은지 판단합니다


def is_right_program(program, parsed_command_program):
    if program != parsed_command_program:
        return False
    return True

# flag name이 옳은지 판단


def is_exist_flag(rules, flag_name):
    for key in rules:
        if key == flag_name:
            return True
    return False


string_regex = re.compile(r'[a-zA-Z]')
# 스트링 regex를 기준으로 옳바른 스트링인지 판별합니다


def is_string(string):
    result = string_regex.findall(string)
    if len(result) != len(string):
        return False
    return True

# type이 STRING일때 올바른지 판별합니다


def check_string(flag_arguments):
    if len(flag_arguments) != 1:
        raise SyntaxError("STRING type은 1개의 argument만 필요합니다")
    if not is_string(flag_arguments[0]):
        raise SyntaxError("argument가 STRING type이 아닙니다")

# type이 STRINGS일때 올바른지 판별합니다


def check_strings(flag_arguments):
    if len(flag_arguments) < 1:
        raise SyntaxError("STRINGS type은 1개 이상의 argument가 필요합니다")
    for flag_argument in flag_arguments:
        if not is_string(flag_argument):
            raise SyntaxError("argument가 STRINGS type이 아닙니다")


number_regex = re.compile(r'[\d]')
# 넘버 regex를 기준으로 옳바른 넘버인지 판별합니다


def is_number(number_string):
    result = number_regex.findall(number_string)
    if len(result) != len(number_string):
        return False
    return True

# type이 NUMBER일때 올바른지 판별합니다


def check_number(flag_arguments):
    if len(flag_arguments) != 1:
        raise SyntaxError("NUMBER type은 1개의 argument만 필요합니다")
    if not is_number(flag_arguments[0]):
        raise SyntaxError("argument가 NUMBER type이 아닙니다")

# type이 NUMBERS일때 올바른지 판별합니다


def check_numbers(flag_arguments):
    if len(flag_arguments) < 1:
        raise SyntaxError("NUMBERS type은 1개 이상의 argument가 필요합니다")
    for flag_argument in flag_arguments:
        if not is_number(flag_argument):
            raise SyntaxError("argument가 NUMBERS type이 아닙니다")

# type이 NULL일때 올바른지 판별합니다


def check_null(flag_arguments):
    if len(flag_arguments) != 0:
        raise SyntaxError("NULL type은 argument가 없어야 합니다")

# flag rule을 확인하고, 그 규칙에 맞도록 판별을 진행합니다.


def check_right_arguments(flag_rule, flag_arguments):
    if flag_rule == "STRING":
        check_string(flag_arguments)
    elif flag_rule == "STRINGS":
        check_strings(flag_arguments)
    elif flag_rule == "NUMBER":
        check_number(flag_arguments)
    elif flag_rule == "NUMBERS":
        check_numbers(flag_arguments)
    elif flag_rule == "NULL":
        check_null(flag_arguments)
    else:
        raise SyntaxError("이미 정의된 Flag 규칙이 아닙니다")

# flag 하나 하나를 확인하고 올바른지 판별합니다.


def check_right_flag(rules, alias_rules, parse_command_flags):
    flag_name_store = []
    for flag in parse_command_flags:
        flag_name = alias_to_origin(flag[0], alias_rules)
        flag_arguments = flag[1]
        if not is_exist_flag(rules, flag_name):
            raise SyntaxError('옳바른 Flag name이 아닙니다')
        if flag_name in flag_name_store:
            raise SyntaxError('동일 한 Flag가 여러번 올 수 없습니다')

        flag_name_store.append(flag_name)
        check_right_arguments(rules[flag_name], flag_arguments)

# 커맨드 하나 하나가 옳은지 판별합니다.


def check_right_command(program, rules, alias_rules, parsed_command):

    if not is_right_program(program, parsed_command[0]):
        raise SyntaxError('옳바른 명령이 아닙니다')

    check_right_flag(rules, alias_rules, parsed_command[1])


def solution(program, flag_rules, commands):
    rules = parse_rules(flag_rules)[0]
    alias_rules = parse_rules(flag_rules)[1]
    answer = []
    for command in commands:
        try:
            parsed_command = parse_command(command)
            check_right_command(program, rules, alias_rules, parsed_command)
            answer.append(True)
        except SyntaxError as err:
            # print('Syntax Error : ', err)
            answer.append(False)
    return answer


def main():
    print(solution("line", ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"],
                   ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
    print(solution("bank", 	["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], [
          "bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))


main()
