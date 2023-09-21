import time
import psutil
import locale

def calculate_elapsed_time(start_time):
    # Calculates the elapsed time between the start and the current time.
    current_time = time.time()
    elapsed_seconds = current_time - start_time
    hours, remainder = divmod(elapsed_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}:{int(minutes)}:{int(seconds)}"

# Detects the operating system language
system_language, _ = locale.getlocale()

# String dictionary based on language
strings = {
    'pt_BR': {
        'file_name': 'registro_tempo_e_bateria.txt',
        'start_log': "Início do registro de tempo e bateria: {}",
        'elapsed_time': "Tempo decorrido: {}",
        'battery_level': "Nível de bateria: {}%",
    },
    'en_US': {
        'file_name': 'time_and_battery_log.txt',
        'start_log': "Start of time and battery log: {}",
        'elapsed_time': "Elapsed time: {}",
        'battery_level': "Battery level: {}%",
    },
}

# Verifies if the system language is available; otherwise, use English as default
if system_language in strings:
    selected_strings = strings[system_language]
else:
    selected_strings = strings['en_US']

log_file = selected_strings['file_name']

# Get the start time
start_time = time.time()

with open(log_file, "w") as file:
    start_log_message = selected_strings['start_log'].format(time.strftime("%Y-%m-%d %H:%M:%S"))
    file.write("[ " + start_log_message + " ]\n")
    print(start_log_message)

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    battery_percent = psutil.sensors_battery().percent

    elapsed_time = calculate_elapsed_time(start_time)

    with open(log_file, "a") as file:
        elapsed_time_message = selected_strings['elapsed_time'].format(elapsed_time)
        battery_level_message = selected_strings['battery_level'].format(battery_percent)
        file.write("[ " + elapsed_time_message + " ] ")
        file.write("[ " + battery_level_message + " ]")
        file.write("\n")
        print("[ " + elapsed_time_message + " ] " + "[ " + battery_level_message + " ]")

    time.sleep(60)  # Waits 60 seconds
