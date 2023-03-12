import gpiozero


def distance_finder(focal_length, real_object_width, width_in_frame):
    distance = (real_object_width * focal_length) / width_in_frame
    return distance


def generate_signal(obj):
    if obj == 'pringles':
        print('pringles detected. Sending signals to pins')
