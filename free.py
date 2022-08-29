import subprocess
import re


def get_list_from_command_output(output):
    normalized = re.sub(' +', ' ', output)
    values = normalized.split(" ")
    return values


def get_mem_from_free_command_output(output):
    return output.split("\n")[1]


def get_free_command_output():
    free_command = subprocess.Popen(["free", "-t", "--mega"], stdout=subprocess.PIPE)
    free_output = free_command.communicate()[0].decode("utf-8")
    mem_output = get_mem_from_free_command_output(free_output)
    mem_values = get_list_from_command_output(mem_output)
    return {"total": mem_values[1], "used": mem_values[2],
            "free": mem_values[3], "shared": mem_values[4],
            "buff/cache": mem_values[5], "available": mem_values[6]}


